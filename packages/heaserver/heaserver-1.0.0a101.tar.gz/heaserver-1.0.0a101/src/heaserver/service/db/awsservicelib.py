"""
Functions for interacting with Amazon Web Services.

This module supports management of AWS accounts, S3 buckets, and objects in S3 buckets. It uses Amazon's boto3 library
behind the scenes.

In order for HEA to access AWS accounts, buckets, and objects, there must be a volume accessible to the user through
the volumes microservice with an AWSFileSystem for its file system. Additionally, credentials must either be stored
in the keychain microservice and associated with the volume through the volume's credential_id attribute,
or stored on the server's file system in a location searched by the AWS boto3 library. Users can only see the
accounts, buckets, and objects to which the provided AWS credentials allow access, and HEA may additionally restrict
the returned objects as documented in the functions below. The purpose of volumes in this case is to supply credentials
to AWS service calls. Support for boto3's built-in file system search for credentials is only provided for testing and
should not be used in a production setting. This module is designed to pass the current user's credentials to AWS3, not
to have application-wide credentials that everyone uses.

The request argument to these functions is expected to have a OIDC_CLAIM_sub header containing the user id for
permissions checking. No results will be returned if this header is not provided or is empty.

In general, there are two flavors of functions for getting accounts, buckets, and objects. The first expects the id
of a volume as described above. The second expects the id of an account, bucket, or bucket and object. The latter
attempts to match the request up to any volumes with an AWSFileSystem that the user has access to for the purpose of
determine what AWS credentials to use. They perform the
same except when the user has access to multiple such volumes, in which case supplying the volume id avoids a search
through the user's volumes.
"""
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from botocore.exceptions import ClientError, ParamValidationError
from aiohttp import web, hdrs

from .awss3bucketobjectkey import KeyDecodeException, encode_key, decode_key, is_folder, join
from heaserver.service.heaobjectsupport import new_heaobject_from_type
from .. import response, client
from ..heaobjectsupport import PermissionGroup
from ..oidcclaimhdrs import SUB
from ..aiohttp import StreamResponseFileLikeWrapper, RequestFileLikeWrapper
from ..mimetypes import guess_mime_type
from ..appproperty import HEA_DB
from ..uritemplate import tvars
from typing import Any, Optional, List, Dict, Callable, AsyncIterator, Generator
from collections.abc import Awaitable
from aiohttp.web import Request, Response, Application
from heaobject.volume import AWSFileSystem
from heaobject.user import NONE_USER, ALL_USERS
from heaobject.bucket import AWSBucket
from heaobject.root import DesktopObjectDict, ShareImpl, EnumAutoName
from heaobject.folder import AWSS3Folder, AWSS3FolderFileItem, Folder, AWSS3BucketItem
from heaobject.data import AWSS3FileObject
from heaobject.account import AWSAccount
from heaobject.aws import S3StorageClass
from heaobject.error import DeserializeException
from heaobject.activity import Status, AWSActivity
from yarl import URL
from asyncio import gather, AbstractEventLoop
from heaobject.root import Tag
from enum import auto
from functools import partial

from ..sources import AWS_S3, HEA
from mypy_boto3_s3.client import S3Client
from mypy_boto3_s3.service_resource import S3ServiceResource
from mypy_boto3_s3.type_defs import TagTypeDef
from datetime import datetime

from heaobject.storage import AWSStorage
from aiohttp.helpers import ETag

"""
Available functions
AWS object
- get_account
- post_account                    NOT TESTED
- put_account                     NOT TESTED
- delete_account                  CANT https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html
                                  One solution would be to use beautiful soup : https://realpython.com/beautiful-soup-web-scraper-python/

- users/policies/roles : https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/

- change_storage_class            TODO
- copy_object
- delete_bucket_objects
- delete_bucket
- delete_folder
- delete_object
- download_object
- download_archive_object         TODO
- generate_presigned_url
- get_object_meta
- get_object_content
- get_all_buckets
- get all
- opener                          TODO -> return file format -> returning metadata containing list of links following collection + json format
-                                         need to pass back collection - json format with link with content type, so one or more links, most likely
- post_bucket
- post_folder
- post_object
- post_object_archive             TODO
- put_bucket
- put_folder
- put_object
- put_object_archive              TODO
- transfer_object_within_account
- transfer_object_between_account TODO
- rename_object
- update_bucket_policy            TODO

TO DO
- accounts?
"""
MONGODB_BUCKET_COLLECTION = 'buckets'

CLIENT_ERROR_NO_SUCH_BUCKET = 'NoSuchBucket'
CLIENT_ERROR_ACCESS_DENIED = 'AccessDenied'
CLIENT_ERROR_FORBIDDEN = '403'
CLIENT_ERROR_404 = '404'
CLIENT_ERROR_ALL_ACCESS_DISABLED = 'AllAccessDisabled'

ROOT_FOLDER = Folder()
ROOT_FOLDER.id = 'root'
ROOT_FOLDER.name = 'root'
ROOT_FOLDER.display_name = 'Root'
ROOT_FOLDER.description = "The root folder for an AWS S3 bucket's objects."
_root_share = ShareImpl()
_root_share.user = ALL_USERS
_root_share.permissions = PermissionGroup.POSTER_PERMS.perms
ROOT_FOLDER.shares = [_root_share]
ROOT_FOLDER.source = HEA


def change_storage_class():
    """
    change storage class (Archive, un-archive) (copy and delete old)

    S3 to archive -> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.upload_archive
        save archive id for future access?
        archived gets charged minimum 90 days
        buckets = vault?
        delete bucket
    archive to S3
        create vault? link vault to account as attribute?
        delete vault
    """


async def copy_object(request: Request) -> Response:
    """
    copy/paste (duplicate), throws error if destination exists, this so an overwrite isn't done
    throws another error is source doesn't exist
    https://medium.com/plusteam/move-and-rename-objects-within-an-s3-bucket-using-boto-3-58b164790b78
    https://stackoverflow.com/questions/47468148/how-to-copy-s3-object-from-one-bucket-to-another-using-python-boto3

    :param request: the aiohttp Request, with the body containing the target bucket and key, and the match_info
    containing the source volume, bucket, and key. (required).
    :return: the HTTP response.
    """
    logger = logging.getLogger(__name__)
    volume_id = request.match_info['volume_id']
    source_bucket_name = request.match_info['bucket_id']
    try:
        source_key_name = decode_key(request.match_info['id']) if 'id' in request.match_info else None
    except KeyDecodeException as e:
        return response.status_bad_request(str(e))
    if source_bucket_name is None or source_key_name is None:
        return response.status_bad_request(f'Invalid request URL')
    try:
        request_json = await request.json()
        destination_url = next(
            item['value'] for item in request_json['template']['data'] if item['name'] == 'target')
        destination_display_name = next(
            item['value'] for item in request_json['template']['data'] if item['name'] == 'display_name')
        if destination_display_name and destination_display_name.endswith('/'):
            return response.status_bad_request('THe name cannot end with a slash')
        vars_ = tvars(route='http{prefix}/volumes/{volume_id}/buckets/{bucket_id}/awss3folders/{id}',
                      url=destination_url)
        destination_bucket_name = vars_['bucket_id']
        destination_folder_name = decode_key(vars_['id']) if 'id' in vars_ else ''
        if destination_folder_name and not is_folder(destination_folder_name):
            return response.status_bad_request(f'Target property {destination_url} is not a folder')
        destination_key_name = join(destination_folder_name, destination_display_name) if destination_folder_name else destination_display_name
        if is_folder(source_key_name):
            destination_key_name += '/'
    except (KeyError, ValueError, KeyDecodeException) as e:
        logger.exception(f'Invalid target property {destination_url}')
        return response.status_bad_request(f'Invalid target property {destination_url}: {e}')
    logger.debug('Copy requested from %s/%s to %s/%s', source_bucket_name, source_key_name, destination_bucket_name, destination_key_name)
    try:
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        s3_client.head_object(Bucket=destination_bucket_name,
                              Key=destination_key_name)  # check if destination object exists, if not throw an exception
        return response.status_bad_request(f'Object {destination_key_name} already exists')
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':  # object doesn't exist
            try:
                s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
                s3_client.head_object(Bucket=source_bucket_name,
                                      Key=source_key_name)  # check if source object exists, if not throws an exception
                thread_pool_executor = ThreadPoolExecutor(max_workers=10)
                loop = asyncio.get_running_loop()

                async def _do_copy() -> AsyncIterator[asyncio.Future[None]]:
                    async for obj in _list_objects(s3_client, source_bucket_name, prefix=source_key_name):
                        destination_key_ = join(destination_key_name, obj['Key'].removeprefix(source_key_name))
                        p = partial(s3_client.copy,
                                    {'Bucket': source_bucket_name, 'Key': obj['Key']},
                                    destination_bucket_name, destination_key_)
                        logger.debug('Copying %s/%s to %s/%s', source_bucket_name, obj['Key'], destination_bucket_name, destination_key_)
                        yield loop.run_in_executor(thread_pool_executor, p)
                async for coro in _do_copy():
                    await coro
                return web.HTTPCreated(headers={hdrs.LOCATION: destination_url})
            except ClientError as e_:
                logger.exception(f'Bad request: {e_}')
                return response.status_bad_request(str(e_))
        else:
            logger.exception(f'Bad request: {e}')
            return response.status_bad_request(str(e))


async def get_folder(request: Request) -> web.Response:
    """
    Gets the requested folder. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. Either The folder id must be
    in the id entry of the request's match_info dictionary, or the folder name must be in the name entry of the
    request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response containing a heaobject.folder.AWSS3Folder object in the body.
    """
    try:
        folder = await _get_folder_helper(request)
        return await response.get(request, folder.to_dict())
    except ClientError as e:
        return handle_client_error(e)
    except web.HTTPClientError as e:
        return e


async def get_folder_opener(request: Request) -> web.Response:
    """
    Gets the requested folder. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. Either The folder id must be
    in the id entry of the request's match_info dictionary, or the folder name must be in the name entry of the
    request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response containing a heaobject.folder.AWSS3Folder object in the body.
    """
    try:
        folder = await _get_folder_helper(request)
        return await response.get_multiple_choices(request, folder.to_dict())
    except ClientError as e:
        return handle_client_error(e)
    except web.HTTPClientError as e:
        return e


async def get_file(request: Request) -> Response:
    """
    Gets the requested file. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The file id must be in
    the id entry of the request's match_info dictionary, or the file name must be in the name entry of the request's
    match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response containing a heaobject.data.AWSS3FileObject object in the body.
    """
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info and 'name' not in request.match_info:
        return response.status_bad_request('either id or name is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['name']

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    try:
        file_id: Optional[str] = decode_key(file_name)
        if is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None
    try:
        if file_id is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            s3_client.head_bucket(Bucket=bucket_name)
            return response.status_not_found()
        response_ = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=file_id, MaxKeys=1)
        logging.debug('Result of get_file: %s', response_)
        if file_id is None or response_['KeyCount'] == 0:
            return response.status_not_found()
        contents = response_['Contents'][0]
        key = contents['Key']
        encoded_key = encode_key(key)
        display_name = key[key.rfind('/', 1) + 1:]
        file = _get_file(bucket_name, contents, display_name, key, encoded_key, request)
        return await response.get(request, file.to_dict())
    except ClientError as e:
        return handle_client_error(e)


async def has_folder(request: Request) -> web.Response:
    """
    Checks for the existence of the requested folder. The volume id must be in the volume_id entry of the request's
    match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info dictionary. The
    folder id must be in the id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the folder exists, 403 if access was denied, 404 if the folder
    was not found, or 500 if an internal error occurred.
    """
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info and 'folder_id' not in request.match_info:
        return response.status_bad_request('id or folder_id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    folder_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['folder_id']

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    if folder_name == ROOT_FOLDER.id:
        return response.status_ok()
    else:
        try:
            folder_id: Optional[str] = decode_key(folder_name)
            if not is_folder(folder_id):
                folder_id = None
        except KeyDecodeException:
            # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
            # for the bucket.
            folder_id = None

    try:
        if folder_id is None:
            # We couldn't decode the folder_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            s3_client.head_bucket(Bucket=bucket_name)
            return response.status_not_found()
        response_ = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_id, MaxKeys=1)
        logging.debug('Result of has_folder: %s', response_)
        if response_['KeyCount'] == 0:
            return response.status_not_found()
        return response.status_ok()
    except ClientError as e:
        return handle_client_error(e)


async def get_all_folders(request: Request) -> web.Response:
    """
    Gets all folders in a bucket. The volume id must be in the volume_id entry of the request's
    match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and a Collection+JSON document in the body
    containing any heaobject.folder.AWSS3Folder objects, 403 if access was denied, or 500 if an internal error occurred. The
    body's format depends on the Accept header in the request.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    try:
        logger.debug('Getting all folders from bucket %s', bucket_name)
        folders = []
        async for obj in _list_objects(s3, bucket_name, loop=loop):
            key = obj['Key']
            if is_folder(key):
                encoded_key = encode_key(key)
                logger.debug('Found folder %s in bucket %s', key[:-1], bucket_name)
                folder = _get_folder(bucket_name, obj, key, encoded_key, request)
                folders.append(folder.to_dict())
        return await response.get_all(request, folders)
    except ClientError as e:
        return handle_client_error(e)


async def get_all_files(request: Request) -> web.Response:
    """
    Gets all files in a bucket. The volume id must be in the volume_id entry of the request's
    match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and a Collection+JSON document in the body
    containing any heaobject.data.AWSS3FileObject objects, 403 if access was denied, or 500 if an internal error occurred. The
    body's format depends on the Accept header in the request.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    try:
        logger.debug('Getting all files from bucket %s', bucket_name)
        files: list[dict] = []
        async for obj in _list_objects(s3, bucket_id=bucket_name, loop=loop):
            key = obj['Key']
            if not is_folder(key):
                encoded_key = encode_key(key)
                logger.debug('Found file %s in bucket %s', key, bucket_name)
                display_name = key.split('/')[-1]
                file = _get_file(bucket_name, obj, display_name, key, encoded_key, request)
                files.append(file.to_dict())
        return await response.get_all(request, files)
    except ClientError as e:
        return handle_client_error(e)


async def get_folder_by_name(request: Request) -> web.Response:
    """
    Gets the requested folder. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The folder name must be in the
    name entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and the heaobject.folder.AWSS3Folder in the body,
    403 if access was denied, 404 if no such folder was found, or 500 if an internal error occurred. The body's format
    depends on the Accept header in the request.
    """
    return await get_folder(request)


async def get_file_by_name(request: Request) -> web.Response:
    """
    Gets the requested file. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The file name must be in the
    name entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and the heaobject.data.AWSS3FileObject in the body,
    403 if access was denied, 404 if no such file was found, or 500 if an internal error occurred. The body's format
    depends on the Accept header in the request.
    """
    return await get_file(request)


async def get_items(request: Request) -> web.Response:
    """
    Gets the requested folder items. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The folder id must be in the
    folder_id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and a list of
    heaobject.folder.AWSS3FileFolderItem objects in the body, 403 if access was denied, or 500 if an internal error
    occurred. The body's format depends on the Accept header in the request.
    """

    logger = logging.getLogger(__name__)

    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'folder_id' not in request.match_info:
        return response.status_bad_request('folder_id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    folder_id_ = request.match_info['folder_id']

    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    folder_id = _decode_folder(folder_id_)
    loop = asyncio.get_running_loop()
    try:
        if folder_id is None:
            # We couldn't decode the folder_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            return await _return_bucket_status_or_not_found(bucket_name, loop, s3)
        logger.debug('Getting all folders in item %s in bucket %s', folder_id, bucket_name)
        folders: Dict[str, AWSS3FolderFileItem] = {}
        async for obj in _list_objects(s3, bucket_id=bucket_name, prefix=folder_id, loop=loop):
            id_ = obj['Key']
            id__ = id_.removeprefix(folder_id)
            try:
                if id__ == '':  # The folder
                    continue
                actual_id = id__[:id__.index('/') + 1]  # A folder
                is_folder_ = True
                display_name = actual_id[:-1]
            except ValueError:
                actual_id = id__  # Not a folder
                is_folder_ = False
                display_name = actual_id
            id_encoded = encode_key(folder_id + actual_id)
            logger.debug('Found item %s in bucket %s', actual_id, bucket_name)
            item = AWSS3FolderFileItem()
            item.id = id_encoded
            item.name = id_encoded
            item.display_name = display_name
            item.modified = obj['LastModified']
            item.created = obj['LastModified']
            item.owner = request.headers.get(SUB, NONE_USER)
            item.actual_object_id = id_encoded
            item.folder_id = folder_id_
            item.storage_class = S3StorageClass[obj['StorageClass']]
            item.bucket_id = bucket_name
            item.key = id_
            item.source = AWS_S3
            item.volume_id = volume_id
            if is_folder_:
                item.actual_object_uri = str(
                    URL('/volumes') / volume_id / 'buckets' / bucket_name / 'awss3folders' / id_encoded)
                item.actual_object_type_name = AWSS3Folder.get_type_name()
            else:
                item.actual_object_uri = str(
                    URL('/volumes') / volume_id / 'buckets' / bucket_name / 'awss3files' / id_encoded)
                item.actual_object_type_name = AWSS3FileObject.get_type_name()
                item.size = obj['Size']
            if actual_id in folders:
                item_ = folders[actual_id]
                if item_.modified is not None and item.modified is not None:
                    item_.modified = max(item_.modified, item.modified)
                elif item.modified is not None:
                    item_.modified = item.modified
            else:
                folders[actual_id] = item
        return await response.get_all(request, list(i.to_dict() for i in folders.values()))
    except ClientError as e:
        return handle_client_error(e)
    except ParamValidationError as e:
        return response.status_bad_request(str(e))


async def has_file(request: Request) -> Response:
    """
    Checks for the existence of the requested file object. The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The file id must be in the id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the file exists, 403 if access was denied, or 500 if an
    internal error occurred.
    """
    logger = logging.getLogger(__name__)

    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')

    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']

    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)

    try:
        file_id: Optional[str] = decode_key(request.match_info['id'])
        if is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None
    loop = asyncio.get_running_loop()
    try:
        if file_id is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
        logger.debug('Checking if file %s in bucket %s exists', file_id, bucket_name)
        response_ = await loop.run_in_executor(None, partial(s3.list_objects_v2, Bucket=bucket_name, Prefix=file_id,
                                                             MaxKeys=1))
        if response_['KeyCount'] > 0:
            return response.status_ok()
        return await response.get(request, None)
    except ClientError as e:
        return handle_client_error(e)
    except KeyDecodeException:
        return response.status_not_found()


async def has_item(request: Request) -> web.Response:
    """
    Checks for the existence of the requested folder item. The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The folder id must be in the folder_id entry of the request's match_info dictionary. The item id must
    be in the id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the item exists, 403 if access was denied, or 500 if an
    internal error occurred.
    """
    logger = logging.getLogger(__name__)

    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'folder_id' not in request.match_info:
        return response.status_bad_request('folder_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')

    volume_id = request.match_info['volume_id']
    folder_id_ = request.match_info['folder_id']
    bucket_name = request.match_info['bucket_id']

    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)

    loop = asyncio.get_running_loop()

    if folder_id_ == ROOT_FOLDER.id:
        folder_id = ''
    else:
        try:
            folder_id = decode_key(folder_id_)
            if not is_folder(folder_id):
                folder_id = None
        except KeyDecodeException:
            # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
            # for the bucket.
            folder_id = None
    try:
        if folder_id is None:
            # We couldn't decode the folder_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
        item_id = decode_key(request.match_info['id'])
        if item_id.startswith(folder_id):
            item_id_ = item_id.removeprefix(folder_id)
            if len(item_id_) > 1 and '/' in item_id_[:-1]:
                return response.status_not_found()
        else:
            return response.status_not_found()
        logger.debug('Checking if item %s in folder %s in bucket %s exists', item_id, folder_id, bucket_name)
        response_ = await loop.run_in_executor(None, partial(s3.list_objects_v2, Bucket=bucket_name, Prefix=item_id,
                                                             MaxKeys=1))
        if response_['KeyCount'] > 0:
            return response.status_ok()
        return await response.get(request, None)
    except ClientError as e:
        return handle_client_error(e)
    except KeyDecodeException:
        return response.status_not_found()


async def get_item(request: Request) -> web.Response:
    """
    Gets the requested folder item. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The folder id must be in the
    folder_id entry of the request's match_info dictionary. The item id must be in the id entry of the request's
    match_info dictionary.

    :param request: the HTTP request (required).
    :param add_actions_hook: a callable for adding run-time actions to the returned JSON document. Use this for WeSTL
    actions that may be optionally added to the WeSTL document depending on the value of the item's
    actual_object_type_name. The callable should call heaserver.service.wstl.add_run_time_action to add actions.
    :return: the HTTP response with a 200 status code if the bucket exists and the heaobject.folder.AWSS3FileFolderItem
    object in the body, 403 if access was denied, or 500 if an internal error occurred. The body's format depends on
    the Accept header in the request.
    """
    logger = logging.getLogger(__name__)

    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'folder_id' not in request.match_info:
        return response.status_bad_request('folder_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')

    volume_id = request.match_info['volume_id']
    folder_id_ = request.match_info['folder_id']
    bucket_name = request.match_info['bucket_id']

    decoded_folder_key, decoded_key, folder_or_item_not_found = _check_folder_and_object_keys(folder_id_, request)

    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)

    try:
        loop = asyncio.get_running_loop()

        if folder_or_item_not_found:
            return await _return_bucket_status_or_not_found(bucket_name, loop, s3)

        logger.debug('Getting item %s in folder %s in bucket %s', decoded_key, decoded_folder_key, bucket_name)
        response_ = await loop.run_in_executor(None, partial(s3.list_objects_v2, Bucket=bucket_name, Prefix=decoded_key,
                                                             MaxKeys=1))
        if response_['KeyCount'] > 0:
            for obj in response_['Contents']:
                id_ = obj['Key']
                is_folder_ = is_folder(id_)
                id_encoded = encode_key(id_)
                if is_folder_:
                    display_name = id_[_second_to_last(id_, '/') + 1:][:-1]
                else:
                    display_name = id_[id_.rfind('/') + 1:]
                logger.debug('Found item %s in bucket %s', id_, bucket_name)

                item = AWSS3FolderFileItem()
                item.id = id_encoded
                item.name = id_encoded
                item.display_name = display_name
                item.modified = obj['LastModified']
                item.created = obj['LastModified']
                item.owner = request.headers.get(SUB, NONE_USER)
                item.folder_id = folder_id_
                item.actual_object_id = id_encoded
                item.storage_class = S3StorageClass[obj['StorageClass']]
                item.bucket_id = bucket_name
                item.key = id_
                item.source = AWS_S3
                item.volume_id = volume_id
                if is_folder_:
                    item.actual_object_uri = str(
                        URL('/volumes') / volume_id / 'buckets' / bucket_name / 'awss3folders' / id_encoded)
                    item.actual_object_type_name = AWSS3Folder.get_type_name()
                else:
                    item.actual_object_uri = str(
                        URL('/volumes') / volume_id / 'buckets' / bucket_name / 'awss3files' / id_encoded)
                    item.actual_object_type_name = AWSS3FileObject.get_type_name()
                    item.size = obj['Size']
                return await response.get(request, item.to_dict())
        return await response.get(request, None)
    except ClientError as e:
        return handle_client_error(e)


class ObjectType(EnumAutoName):
    """
    Divides the world of AWS S3 bucket objects into files and folders.
    """
    FILE = auto()
    FOLDER = auto()
    ANY = auto()


async def delete_folder(request: Request, recursive=False) -> Response:
    """
    Deletes the requested folder and optionally all contents. The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The folder id must be in the id entry of the request's match_info dictionary.

    :param request: the aiohttp Request (required).
    :param recursive: if True, this function will delete the folder and all of its contents, otherwise it will return
    a 400 error if the folder is not empty.
    :return: the HTTP response with a 204 status code if the folder was successfully deleted, 403 if access was denied,
    404 if the folder was not found, or 500 if an internal error occurred.
    """
    # https://izziswift.com/amazon-s3-boto-how-to-delete-folder/
    return await delete_object(request, object_type=ObjectType.FOLDER, recursive=recursive)


async def delete_file(request: Request) -> Response:
    """
    Deletes the requested file. The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The file id must be in the id entry of the request's match_info dictionary.

    :param request: the aiohttp Request (required).
    :return: the HTTP response with a 204 status code if the file was successfully deleted, 403 if access was denied,
    404 if the file was not found, or 500 if an internal error occurred.
    """
    return await delete_object(request, object_type=ObjectType.FILE)


async def delete_object(request: Request, object_type: Optional[ObjectType] = None, recursive=False,
                        activity_cb: Optional[
                            Callable[[Application, AWSActivity], Awaitable[None]]] = None) -> Response:
    """
    Deletes a single object. The volume id must be in the volume_id entry of the request's match_info dictionary. The
    bucket id must be in the bucket_id entry of the request's match_info dictionary. The item id must be in the id
    entry of the request's match_info dictionary. An optional folder id may be passed in the folder_id entry of the
    request's match_info_dictinary.

    :param request: the aiohttp Request (required).
    :param object_type: only delete the requested object only if it is a file or only if it is a folder. Pass in
    ObjectType.ANY or None (the default) to signify that it does not matter.
    :param recursive: if True, and the object is a folder, this function will delete the folder and all of its
    contents, otherwise it will return a 400 error if the folder is not empty. If the object to delete is not a folder,
    this flag will have no effect.
    :param activity_cb: optional coroutine that is called when potentially relevant activity occurred.
    :return: the HTTP response with a 204 status code if the item was successfully deleted, 403 if access was denied,
    404 if the item was not found, or 500 if an internal error occurred.
    """
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object
    # TODO: bucket.object_versions.filter(Prefix="myprefix/").delete()     add versioning option like in the delete bucket?
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')

    bucket_name = request.match_info['bucket_id']
    encoded_key = request.match_info['id']
    volume_id = request.match_info['volume_id']
    encoded_folder_key = request.match_info.get('folder_id', None)
    try:
        key: Optional[str] = decode_key(encoded_key)
        if object_type == ObjectType.FOLDER and not is_folder(key):
            key = None
        elif object_type == ObjectType.FILE and is_folder(key):
            key = None
    except KeyDecodeException:
        key = None
    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    try:
        if key is None:
            return await _return_bucket_status_or_not_found(bucket_name, loop, s3_client)
        if encoded_folder_key is not None:
            folder_key = _decode_folder(encoded_folder_key)
            if folder_key is None or not _key_in_folder(key, folder_key):
                return await _return_bucket_status_or_not_found(bucket_name, loop, s3_client)

        response_ = await loop.run_in_executor(None, partial(s3_client.list_objects_v2, Bucket=bucket_name,
                                                             Prefix=key))
        # A key count of 0 means the folder doesn't exist. A key count of 1 just has the folder itself. A key count > 1
        # means the folder has contents.
        key_count = response_['KeyCount']
        if key_count == 0:
            return await _return_bucket_status_or_not_found(bucket_name, loop, s3_client)
        if is_folder(key):
            if not recursive and key_count > 1:
                return response.status_bad_request(f'The folder {encoded_key} is not empty')
            for object_f in response_['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=object_f['Key'])
        else:
            s3_client.delete_object(Bucket=bucket_name, Key=key)
        if activity_cb:
            activity = AWSActivity()
            activity.owner = request.headers.get(SUB, NONE_USER)
            activity.user_id = activity.owner
            activity.status = Status.COMPLETE
            activity.action = f'Deleted {key}'
            await activity_cb(request.app, activity)
        return await response.delete(True)
    except ClientError as e:
        return handle_client_error(e)


def download_archive_object(length=1):
    """

    """


def get_archive():
    """
    Don't think it is worth it to have a temporary view of data, expensive and very slow
    """


async def generate_presigned_url(request: Request):
    """Generate a presigned URL to share an S3 object

    :param request: the aiohttp Request (required).
    :param volume_id: the id string of the volume representing the user's AWS account.
    :param path_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as a string. If error, returns 404.

    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    """
    # Generate a presigned URL for the S3 object
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    object_id = request.match_info['id']
    # three days default for expiration
    expiration = request.rel_url.query.get("expiration", 259200)

    try:
        object_id = decode_key(object_id)
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        return response.status_not_found()
    try:
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        loop = asyncio.get_running_loop()
        url = await loop.run_in_executor(None, partial(s3_client.generate_presigned_url, 'get_object',
                                                       Params={'Bucket': bucket_id, 'Key': object_id},
                                                       ExpiresIn=expiration))
        logging.info(response)
    except ClientError as e:
        return handle_client_error(e)
    # The response contains the presigned URL
    file = AWSS3FileObject()
    file.presigned_url = url
    return await response.get(request, file.to_dict())


async def get_object_content(request: Request) -> web.StreamResponse:
    """
    preview object in object explorer
    :param request: the aiohttp Request (required).
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id']

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)

    try:
        key: Optional[str] = decode_key(file_name)
        if is_folder(key):
            key = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        key = None

    try:
        loop = asyncio.get_running_loop()
        if key is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
        resp = await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_name, Key=key))
        etag = resp['ETag'].strip('"')
        last_modified = resp['LastModified']
        if request.if_none_match and ETag(etag) in request.if_none_match:
            return web.HTTPNotModified()
        if request.if_modified_since and last_modified and request.if_modified_since >= last_modified:
            return web.HTTPNotModified()
        logger.debug('Downloading object %s', resp)

        response_ = web.StreamResponse(status=200, reason='OK',
                                       headers={hdrs.CONTENT_DISPOSITION: f'attachment; filename={key.split("/")[-1]}'})
        mime_type = guess_mime_type(key)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        response_.content_type = mime_type
        response_.last_modified = last_modified
        response_.content_length = resp['ContentLength']
        response_.etag = etag
        await response_.prepare(request)
        async with StreamResponseFileLikeWrapper(response_) as fileobj:
            logger.debug('After initialize')
            await loop.run_in_executor(None, s3_client.download_fileobj, bucket_name, key, fileobj)
        logger.debug('Content length is %d bytes', response_.content_length)
        return response_
    except ClientError:
        logger.exception('Error getting object content')
        return response.status_not_found()


async def get_volume_id_for_account_id(request: web.Request) -> str | None:
    """
    Gets the id of the volume associated with an AWS account. The account id is expected to be in the request object's
    match_info mapping, with key 'id'.

    :param request: an aiohttp Request object (required).
    :return: a volume id string, or None if no volume was found associated with the AWS account.
    """

    async def get_one(request, volume_id):
        return volume_id, await get_account(request, volume_id)

    return next((volume_id for (volume_id, a) in await gather(
        *[get_one(request, v.id) async for v in request.app[HEA_DB].get_volumes(request, AWSFileSystem)])
                 if
                 a['id'] == request.match_info['id']), None)


async def get_account(request: Request, volume_id: str) -> DesktopObjectDict | None:
    """
    Gets the current user's AWS account dict associated with the provided volume_id.

    :param request: the HTTP request object (required).
    :param volume_id: the volume id (required).
    :return: the AWS account dict, or None if not found.
    """
    aws_object_dict = {}
    sts_client = await request.app[HEA_DB].get_client(request, 'sts', volume_id)
    iam_client = await request.app[HEA_DB].get_client(request, 'iam', volume_id)
    account = AWSAccount()

    loop = asyncio.get_running_loop()
    identity_future = loop.run_in_executor(None, sts_client.get_caller_identity)
    # user_future = loop.run_in_executor(None, iam_client.get_user)
    await asyncio.wait([identity_future])  # , user_future])
    aws_object_dict['account_id'] = identity_future.result().get('Account')
    # aws_object_dict['alias'] = next(iam_client.list_account_aliases()['AccountAliases'], None)  # Only exists for IAM accounts.
    # user = user_future.result()['User']
    # aws_object_dict['account_name'] = user.get('UserName')  # Only exists for IAM accounts.

    account.id = aws_object_dict['account_id']
    account.name = aws_object_dict['account_id']
    account.display_name = aws_object_dict['account_id']
    account.owner = request.headers.get(SUB, NONE_USER)
    # account.created = user['CreateDate']
    # FIXME this info coming from Alternate Contact(below) gets 'permission denied' with IAMUser even with admin level access
    # not sure if only root account user can access. This is useful info need to investigate different strategy
    # alt_contact_resp = account_client.get_alternate_contact(AccountId=account.id, AlternateContactType='BILLING' )
    # alt_contact =  alt_contact_resp.get("AlternateContact ", None)
    # if alt_contact:
    # account.full_name = alt_contact.get("Name", None)

    return account.to_dict()


async def post_folder(request: Request) -> web.Response:
    """
    Creates a new folder in a bucket. The volume id must be in the volume_id entry of the request.match_info dictionary.
    The bucket id must be in the bucket_id entry of request.match_info. The folder id must be in the id entry of
    request.match_info.

    :param request: the HTTP request (required).
    :return: the HTTP response, with a 201 status code if successful with the URL to the new item in the Location
    header, 403 if access was denied, 404 if the volume or bucket could not be found, or 500 if an internal error
    occurred.
    """
    logger = logging.getLogger(__name__)

    try:
        folder = await new_heaobject_from_type(request, AWSS3Folder)
    except DeserializeException as e:
        logger.exception('Invalid new folder')
        return response.status_bad_request(f'Invalid new folder: {str(e)}')
    if folder.display_name is None:
        return response.status_bad_request("display_name is required")
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')
    if folder is None:
        return response.status_bad_request('folder is a required field')
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    id_ = request.match_info['id']

    if id_ is None:
        return response.status_bad_request('folder_id cannot be None')

    if '/' in folder.display_name:
        return response.status_bad_request(f"The item's display name may not have slashes in it")
    if id_ == ROOT_FOLDER.id:
        item_folder_id = ''
    else:
        try:
            item_folder_id = decode_key(id_)
            if not is_folder(item_folder_id):
                item_folder_id = None
        except KeyDecodeException:
            item_folder_id = None
    item_name = join(item_folder_id, folder.display_name)
    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    try:
        if item_folder_id is None:
            await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_id))
            return response.status_not_found()
        if folder.type == AWSS3Folder.get_type_name():
            item_name += '/'
        else:
            return response.status_bad_request(f'Unsupported type {folder.get_type_name()}')
        response_ = await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_id,
                                                             Key=item_name))  # check if folder exists, if not throws an exception
        logger.debug('Result of post_object: %s', response_)
        return response.status_bad_request(body=f"Item {item_name} already exists")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == CLIENT_ERROR_404:  # folder doesn't exist
            await loop.run_in_executor(None, partial(s3_client.put_object, Bucket=bucket_id, Key=item_name))
            logger.info('Added folder %s', item_name)
            return await response.post(request, encode_key(item_name),
                                       f"volumes/{volume_id}/buckets/{bucket_id}/awss3folders")
        elif error_code == CLIENT_ERROR_NO_SUCH_BUCKET:
            return response.status_not_found()
        else:
            return response.status_bad_request(str(e))


async def post_object(request: Request, item: AWSS3FolderFileItem) -> web.Response:
    """
    Creates a new object in a bucket. The volume id must be in the volume_id entry of the request.match_info dictionary.
    The bucket id must be in the bucket_id entry of request.match_info. The folder id must be in the folder_id entry of
    request.match_info.

    :param request: the HTTP request (required).
    :param item: the heaobject.folder.AWSS3FileFolderItem to create (required).
    :return: the HTTP response, with a 201 status code if successful with the URL to the new item in the Location
    header, 403 if access was denied, 404 if the volume or bucket could not be found, or 500 if an internal error
    occurred.
    """
    logger = logging.getLogger(__name__)
    if item.display_name is None:
        return response.status_bad_request("display_name is required")
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'folder_id' not in request.match_info:
        return response.status_bad_request('folder_id is required')
    if item is None:
        return response.status_bad_request('item is a required field')
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    folder_id = request.match_info['folder_id']

    if item.folder_id is not None and folder_id != item.folder_id:
        return response.status_bad_request(
            f'folder_id in object was {item.folder_id} but folder_id in URL was {folder_id}')
    if folder_id is None:
        return response.status_bad_request('folder_id cannot be None')
    if item.folder_id is not None and item.folder_id != folder_id:
        return response.status_bad_request(
            f'Inconsistent folder_id in URL versus item: {folder_id} vs {item.folder_id}')
    if '/' in item.display_name:
        return response.status_bad_request(f"The item's display name may not have slashes in it")
    if folder_id == ROOT_FOLDER.id:
        item_folder_id = ''
    else:
        try:
            item_folder_id = decode_key(folder_id)
            if not is_folder(item_folder_id):
                item_folder_id = None
        except KeyDecodeException:
            item_folder_id = None

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()
    try:
        if item_folder_id is None:
            await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_id))
            return response.status_not_found()
        item_name = f'{item_folder_id}{item.display_name}'
        if item.actual_object_type_name == AWSS3Folder.get_type_name():
            item_name += '/'
        elif item.actual_object_type_name == AWSS3FileObject.get_type_name():
            pass
        else:
            return response.status_bad_request(f'Unsupported actual_object_type_name {item.actual_object_type_name}')
        response_ = await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_id,
                                                             Key=item_name))  # check if item exists, if not throws an exception
        logger.debug('Result of post_object: %s', response_)
        return response.status_bad_request(body=f"Item {item_name} already exists")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == CLIENT_ERROR_404:  # folder doesn't exist
            await loop.run_in_executor(None, partial(s3_client.put_object, Bucket=bucket_id, Key=item_name))
            logger.info('Added folder %s', item_name)
            return await response.post(request, encode_key(item_name),
                                       f"volumes/{request.match_info['volume_id']}/buckets/{request.match_info['bucket_id']}/awss3folders/{folder_id}/items")
        elif error_code == CLIENT_ERROR_NO_SUCH_BUCKET:
            return response.status_not_found()
        else:
            return response.status_bad_request(str(e))


async def put_object_content(request: Request) -> web.Response:
    """
    Upload a file to an S3 bucket. Will fail if the file already exists.
    See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html for more information.

    The following information must be specified in request.match_info:
    volume_id (str): the id of the target volume,
    bucket_id (str): the name of the target bucket,
    id (str): the name of the file.

    :param request: the aiohttp Request (required).
    :return: the HTTP response, with a 204 status code if successful, 400 if one of the above values was not specified,
    403 if uploading access was denied, 404 if the volume or bucket could not be found, or 500 if an internal error
    occurred.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request("volume_id is required")
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request("bucket_id is required")
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id']

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    loop = asyncio.get_running_loop()

    try:
        file_id: Optional[str] = decode_key(file_name)
        if is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None

    try:
        if file_id is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
    except ClientError as e:
        return handle_client_error(e)

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    try:
        await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_name, Key=file_id))
        fileobj = RequestFileLikeWrapper(request)
        done = False
        try:
            fileobj.initialize()
            from concurrent.futures import ThreadPoolExecutor
            upload_response = await loop.run_in_executor(None, s3_client.upload_fileobj, fileobj, bucket_name, file_id)
            fileobj.close()
            done = True
        except Exception as e:
            if not done:
                try:
                    fileobj.close()
                except:
                    pass
                done = True
                raise e

        logger.info(upload_response)
    except ClientError as e:
        return handle_client_error(e)
    return response.status_no_content()


def post_object_archive():
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html
    """


# def put_object_archive():
#     """
#     https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html
#     """


# async def transfer_object_within_account(request: Request, volume_id: str, object_path, new_path):
#     """
#     same as copy_object, but also deletes the object
#
#     :param request: the aiohttp Request (required).
#     :param volume_id: the id string of the volume representing the user's AWS account.
#     :param object_path (str) gives the old location of the object, input as the bucket and key together
#     :param new_path: (str) gives the new location to put the object
#     """
#     await copy_object(request, volume_id, object_path, new_path)
#     await delete_object(request, volume_id, object_path)


# def transfer_object_between_account():
#     """
#     https://markgituma.medium.com/copy-s3-bucket-objects-across-separate-aws-accounts-programmatically-323862d857ed
#     """
#     # TODO: use update_bucket_policy to set up "source" bucket policy correctly
#     """
#     {
#     "Version": "2012-10-17",
#     "Id": "Policy1546558291129",
#     "Statement": [
#         {
#             "Sid": "Stmt1546558287955",
#             "Effect": "Allow",
#             "Principal": {
#                 "AWS": "arn:aws:iam::<AWS_IAM_USER>"
#             },
#             "Action": [
#               "s3:ListBucket",
#               "s3:GetObject"
#             ],
#             "Resource": "arn:aws:s3:::<SOURCE_BUCKET>/",
#             "Resource": "arn:aws:s3:::<SOURCE_BUCKET>/*"
#         }
#     ]
#     }
#     """
#     # TODO: use update_bucket_policy to set up aws "destination" bucket policy
#     """
#     {
#     "Version": "2012-10-17",
#     "Id": "Policy22222222222",
#     "Statement": [
#         {
#             "Sid": "Stmt22222222222",
#             "Effect": "Allow",
#             "Principal": {
#                 "AWS": [
#                   "arn:aws:iam::<AWS_IAM_DESTINATION_USER>",
#                   "arn:aws:iam::<AWS_IAM_LAMBDA_ROLE>:role/
#                 ]
#             },
#             "Action": [
#                 "s3:ListBucket",
#                 "s3:PutObject",
#                 "s3:PutObjectAcl"
#             ],
#             "Resource": "arn:aws:s3:::<DESTINATION_BUCKET>/",
#             "Resource": "arn:aws:s3:::<DESTINATION_BUCKET>/*"
#         }
#     ]
#     }
#     """
#     # TODO: code
#     source_client = boto3.client('s3', "SOURCE_AWS_ACCESS_KEY_ID", "SOURCE_AWS_SECRET_ACCESS_KEY")
#     source_response = source_client.get_object(Bucket="SOURCE_BUCKET", Key="OBJECT_KEY")
#     destination_client = boto3.client('s3', "DESTINATION_AWS_ACCESS_KEY_ID", "DESTINATION_AWS_SECRET_ACCESS_KEY")
#     destination_client.upload_fileobj(source_response['Body'], "DESTINATION_BUCKET",
#                                       "FOLDER_LOCATION_IN_DESTINATION_BUCKET")


# async def rename_object(request: Request, volume_id: str, object_path: str, new_name: str):
#     """
#     BOTO3, the copy and rename is the same
#     https://medium.com/plusteam/move-and-rename-objects-within-an-s3-bucket-using-boto-3-58b164790b78
#     https://stackoverflow.com/questions/47468148/how-to-copy-s3-object-from-one-bucket-to-another-using-python-boto3
#
#     :param request: the aiohttp Request (required).
#     :param volume_id: the id string of the volume representing the user's AWS account.
#     :param object_path: (str) path to object, includes both bucket and key values
#     :param new_name: (str) value to rename the object as, will only replace the name not the path. Use transfer object for that
#     """
#     # TODO: check if ACL stays the same and check existence
#     try:
#         s3_resource = await request.app[HEA_DB].get_resource(request, 's3', volume_id)
#         copy_source = {'Bucket': object_path.partition("/")[0], 'Key': object_path.partition("/")[2]}
#         bucket_name = object_path.partition("/")[0]
#         old_name = object_path.rpartition("/")[2]
#         s3_resource.meta.client.copy(copy_source, bucket_name,
#                                      object_path.partition("/")[2].replace(old_name, new_name))
#     except ClientError as e:
#         logging.error(e)


# def update_bucket_policy():
#     """
#
#     """


def _from_aws_tags(aws_tags: List[TagTypeDef]) -> List[Tag]:
    """
    :param aws_tags: Tags obtained from boto3 Tags api
    :return: List of HEA Tags
    """
    hea_tags = []
    for t in aws_tags:
        tag = Tag()
        tag.key = t['Key']
        tag.value = t['Value']
        hea_tags.append(tag)
    return hea_tags


async def get_bucket(volume_id: str, s3_resource: S3ServiceResource, s3_client: S3Client,
                     bucket_name: Optional[str] = None, bucket_id: Optional[str] = None,
                     creation_date: Optional[datetime] = None) -> Optional[AWSBucket]:
    """
    :param volume_id: the volume id
    :param s3_client:  the boto3 client
    :param bucket_name: str the bucket name (optional)
    :param bucket_id: str the bucket id (optional)
    :param creation_date: str the bucket creation date (optional)
    :return: Returns either the AWSBucket or None for Not Found or Forbidden, else raises ClientError
    """
    logger = logging.getLogger(__name__)
    try:
        loop = asyncio.get_running_loop()
        if not volume_id or (not bucket_id and not bucket_name):
            raise ValueError("volume_id is required and either bucket_name or bucket_id")
        # id_type = 'id' if bucket_id else 'name'
        # user = request.headers.get(SUB)
        # bucket_dict = await request.app[HEA_DB].get(request, MONGODB_BUCKET_COLLECTION, var_parts=id_type, sub=user)
        # if not bucket_dict:
        #     return web.HTTPBadRequest()

        b = AWSBucket()
        b.name = bucket_id if bucket_id else bucket_name
        b.id = bucket_id if bucket_id else bucket_name
        if bucket_id is not None:
            b.display_name = bucket_id
        elif bucket_name is not None:
            b.display_name = bucket_name
        async_bucket_methods = []
        b_from_boto = await loop.run_in_executor(None, s3_resource.Bucket, b.name)
        b.created = creation_date if creation_date else b_from_boto.creation_date
        b.bucket_id = b.name
        b.source = AWS_S3

        async def _get_version_status(b: AWSBucket):
            logger.debug('Getting version status of bucket %s', b.name)
            try:
                bucket_versioning = await loop.run_in_executor(None,
                                                               partial(s3_client.get_bucket_versioning, Bucket=b.name))
                logger.debug('bucket_versioning=%s', bucket_versioning)
                if 'Status' in bucket_versioning:
                    b.versioned = bucket_versioning['Status'] == 'Enabled'
                    logger.debug('Got version status of bucket %s successfully', b.name)
                else:
                    logger.debug('No version status information for bucket %s', b.name)
            except ClientError as ce:
                logger.exception('Error getting the version status of bucket %s')
                raise ce

        async_bucket_methods.append(_get_version_status(b))

        async def _get_region(b: AWSBucket):
            logger.debug('Getting region of bucket %s', b.name)
            try:
                loc = await loop.run_in_executor(None, partial(s3_client.get_bucket_location, Bucket=b.name))
                b.region = loc['LocationConstraint'] or 'us-east-1'
            except ClientError as ce:
                logging.exception('Error getting the region of bucket %s', b.name)
                raise ce
            logger.debug('Got region of bucket %s successfully', b.name)

        async_bucket_methods.append(_get_region(b))

        # todo how to find partition dynamically. The format is arn:PARTITION:s3:::NAME-OF-YOUR-BUCKET
        # b.arn = "arn:"+"aws:"+":s3:::"

        async def _get_tags(b: AWSBucket):
            logger.debug('Getting tags of bucket %s', b.name)
            try:
                tagging = await loop.run_in_executor(None, partial(s3_client.get_bucket_tagging, Bucket=b.name))
                b.tags = _from_aws_tags(aws_tags=tagging['TagSet'])
            except ClientError as ce:
                if ce.response['Error']['Code'] != 'NoSuchTagSet':
                    logging.exception('Error getting the tags of bucket %s', b.name)
                    raise ce
            logger.debug('Got tags of bucket %s successfully', b.name)

        async_bucket_methods.append(_get_tags(b))

        async def _get_encryption_status(b: AWSBucket):
            logger.debug('Getting encryption status of bucket %s', b.name)
            try:
                encrypt = await loop.run_in_executor(None, partial(s3_client.get_bucket_encryption, Bucket=b.name))
                rules: list = encrypt['ServerSideEncryptionConfiguration']['Rules']
                b.encrypted = len(rules) > 0
            except ClientError as e:
                if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                    b.encrypted = False
                else:
                    logger.exception('Error getting the encryption status of bucket %s', b.name)
                    raise e
            logger.debug('Got encryption status of bucket %s successfully', b.name)

        async_bucket_methods.append(_get_encryption_status(b))

        async def _get_bucket_policy(b: AWSBucket):
            logger.debug('Getting bucket policy of bucket %s', b.name)
            try:
                bucket_policy = await loop.run_in_executor(None, partial(s3_client.get_bucket_policy, Bucket=b.name))
                b.permission_policy = bucket_policy['Policy']
            except ClientError as e:
                if e.response['Error']['Code'] != 'NoSuchBucketPolicy':
                    logging.exception('Error getting the bucket policy of bucket %s', b.name)
                    raise e
            logger.debug('Got bucket policy of bucket %s successfully', b.name)

        async_bucket_methods.append(_get_bucket_policy(b))

        async def _get_bucket_lock_status(b: AWSBucket):
            logger.debug('Getting bucket lock status of bucket %s', b.name)
            try:
                lock_config = await loop.run_in_executor(None, partial(s3_client.get_object_lock_configuration,
                                                                       Bucket=b.name))
                b.locked = lock_config['ObjectLockConfiguration']['ObjectLockEnabled'] == 'Enabled'
            except ClientError as e:
                if e.response['Error']['Code'] != 'ObjectLockConfigurationNotFoundError':
                    logger.exception('Error getting the lock status of bucket %s', b.name)
                    raise e
                b.locked = False
            logger.debug('Got bucket lock status of bucket %s successfully', b.name)

        async_bucket_methods.append(_get_bucket_lock_status(b))

        # todo need to lazy load this these metrics
        total_size = None
        obj_count = None
        mod_date = None
        # FIXME need to calculate this metric data in a separate call. Too slow
        # s3bucket = s3_resource.Bucket(b.name)
        # for obj in s3bucket.objects.all():
        #     total_size += obj.size
        #     obj_count += 1
        #     mod_date = obj.last_modified if mod_date is None or obj.last_modified > mod_date else mod_date
        b.size = total_size
        b.object_count = obj_count
        b.modified = mod_date
        await asyncio.gather(*async_bucket_methods)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code in ('403', '404', 'NoSuchBucket'):
            return None
        logger.exception(f'Error getting bucket %s', b.name)
        raise e
    return b


async def to_aws_tags(hea_tags: List[Tag]) -> List[Dict[str, str]]:
    """
    :param hea_tags: HEA tags to converted to aws tags compatible with boto3 api
    :return: aws tags
    """
    aws_tag_dicts = []
    for hea_tag in hea_tags:
        aws_tag_dict = {}
        aws_tag_dict['Key'] = hea_tag.key
        aws_tag_dict['Value'] = hea_tag.value
        aws_tag_dicts.append(aws_tag_dict)
    return aws_tag_dicts


def _second_to_last(text, pattern):
    return text.rfind(pattern, 0, text.rfind(pattern))


def handle_client_error(e) -> Response:
    logger = logging.getLogger(__name__)
    error_code = e.response['Error']['Code']
    if error_code in (CLIENT_ERROR_404, CLIENT_ERROR_NO_SUCH_BUCKET):  # folder doesn't exist
        logger.debug('Error from boto3: %s', exc_info=True)
        return response.status_not_found()
    elif error_code in (CLIENT_ERROR_ACCESS_DENIED, CLIENT_ERROR_FORBIDDEN, CLIENT_ERROR_ALL_ACCESS_DISABLED):
        logger.debug('Error from boto3: %s', exc_info=True)
        return response.status_forbidden()
    else:
        logger.exception('Error from boto3')
        return response.status_internal_error(str(e))


def _get_file(bucket_name: str, contents: Dict[str, Any], display_name: str, key: str, encoded_key: str,
              request: Request) -> AWSS3FileObject:
    file = AWSS3FileObject()
    file.id = encoded_key
    file.name = encoded_key
    file.display_name = display_name
    file.modified = contents['LastModified']
    file.created = contents['LastModified']
    file.owner = request.headers.get(SUB, NONE_USER)
    file.mime_type = guess_mime_type(display_name)
    file.size = contents['Size']
    file.storage_class = S3StorageClass[contents['StorageClass']]
    file.source = AWS_S3
    file.bucket_id = bucket_name
    file.key = key
    return file


def _get_folder(bucket_name: str, contents: Dict[str, Any], key: str, encoded_key: str,
                request: Request) -> AWSS3Folder:
    folder = AWSS3Folder()
    folder.id = encoded_key
    folder.name = encoded_key
    folder.display_name = key[_second_to_last(key, '/') + 1:-1]
    folder.modified = contents['LastModified']
    folder.created = contents['LastModified']
    folder.owner = request.headers.get(SUB, NONE_USER)
    folder.storage_class = S3StorageClass[contents['StorageClass']]
    folder.bucket_id = bucket_name
    folder.key = key
    folder.source = AWS_S3
    return folder


def _decode_folder(folder_id_) -> str | None:
    if folder_id_ == ROOT_FOLDER.id:
        folder_id = ''
    else:
        try:
            folder_id = decode_key(folder_id_)
            if not is_folder(folder_id):
                folder_id = None
        except KeyDecodeException:
            # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
            # for the bucket.
            folder_id = None
    return folder_id


def _key_in_folder(decoded_key, decoded_folder_key) -> bool:
    if decoded_key.startswith(decoded_folder_key):
        item_id_ = decoded_key.removeprefix(decoded_folder_key)
        if len(item_id_) > 1 and '/' in item_id_[:-1]:
            return False
    else:
        return False
    return True


async def _return_bucket_status_or_not_found(bucket_name, loop, s3):
    try:
        await loop.run_in_executor(None, partial(s3.head_bucket, Bucket=bucket_name))
        return response.status_not_found()
    except ClientError as e:
        return handle_client_error(e)


def _check_folder_and_object_keys(folder_id_: Optional[str], request: Request) -> tuple[str | None, str | None, bool]:
    folder_or_item_not_found = False
    decoded_folder_key = _decode_folder(folder_id_)
    if decoded_folder_key is None:
        folder_or_item_not_found = True
    try:
        decoded_key = decode_key(request.match_info['id'])
        if not _key_in_folder(decoded_key, decoded_folder_key):
            folder_or_item_not_found = True
    except KeyDecodeException as e:
        decoded_key = None
        folder_or_item_not_found = True

    return decoded_folder_key, decoded_key, folder_or_item_not_found


async def _list_objects(s3: S3Client, bucket_id: str, prefix: str = None, loop: AbstractEventLoop = None) -> AsyncIterator[
    dict[str, Any]]:
    if not loop:
        loop_ = asyncio.get_running_loop()
    else:
        loop_ = loop
    first_time = True
    continuation_token = None
    thread_pool_executor = ThreadPoolExecutor(max_workers=10)
    while first_time or continuation_token:
        first_time = False
        list_partial = partial(s3.list_objects_v2, Bucket=bucket_id)
        if continuation_token is not None:
            list_partial = partial(list_partial, ContinuationToken=continuation_token)
        if prefix is not None:
            list_partial = partial(list_partial, Prefix=prefix)
        response_ = await loop_.run_in_executor(thread_pool_executor, list_partial)
        continuation_token = response_['NextContinuationToken'] if response_['IsTruncated'] else None
        if response_['KeyCount'] > 0:
            for obj in response_['Contents']:
                yield obj


async def _get_folder_helper(request: web.Request) -> Folder:
    if 'volume_id' not in request.match_info:
        raise web.HTTPBadRequest(text='volume_id is required')
    if 'bucket_id' not in request.match_info:
        raise web.HTTPBadRequest(text='bucket_id is required')
    if 'id' not in request.match_info and 'name' not in request.match_info:
        raise web.HTTPBadRequest(text='either id or name is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    folder_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['name']

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    try:
        folder_id: Optional[str] = decode_key(folder_name)
        if not is_folder(folder_id):
            folder_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        folder_id = None
    if folder_id is None:
        # We couldn't decode the folder_id, and we need to check if the user can access the bucket in order to
        # decide which HTTP status code to respond with (Forbidden vs Not Found).
        s3_client.head_bucket(Bucket=bucket_name)
        raise web.HTTPNotFound
    response_ = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_id, MaxKeys=1)
    logging.debug('Result of get_folder: %s', response_)
    if folder_id is None or response_['KeyCount'] == 0:
        raise web.HTTPNotFound
    contents = response_['Contents'][0]
    key = response_['Prefix']
    encoded_key = encode_key(key)
    return _get_folder(bucket_name, contents, key, encoded_key, request)
