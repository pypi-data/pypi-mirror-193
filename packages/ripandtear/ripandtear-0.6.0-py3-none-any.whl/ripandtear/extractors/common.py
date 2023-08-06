import httpx

from datetime import datetime
from ripandtear.utils import downloader
from ripandtear.utils.custom_types import UrlDictionary


class Common():

    def common_filename_creator(self, url_dictionary: UrlDictionary) -> str:
        '''
        Builds out the general standard filename format. It adds receives the information from
        url_dictionary and adds it to the filename string where appropriate. The standard format is:

        prefix-date_uploaded-album_name-count-id-description.ext

        prefix - name of the website
        date_uploaded - if a datetime from when it is uploaded is provided it is added
        album - add the album name the file belongs to (if it applies)
        count - applies if the file is apart of an album. Tries to keep the files in order
        name - name of the file. usually the id from the the url
        description - usually the title given to the file from the orignal site it was uploaded
        to. typically a sentence
        extension - the extension of the file
        '''
        # Template of all information that should be passed
        # in the url_dictionary. Copy and past into the extractor

        # if 'prefix' in url_dictionary:
        #     prefix = url_dictionary['prefix']
        # else:
        #     prefix = self.prefix
        #
        # if 'album_name' in url_dictionary:
        #     album_name = url_dictionary['album_name']
        # else:
        #     album_name = None
        #
        # if 'count' in url_dictionary:
        #     count = url_dictionary['count']
        # else:
        #     count = None
        #
        # if 'description' in url_dictionary:
        #     description = url_dictionary['description']
        # else:
        #     description = None

        # url_dictionary['name'] = name
        # url_dictionary['date'] = date
        # url_dictionary['url_to_download'] = url_to_download
        # url_dictionary['url_to_record'] = url_to_record
        # url_dictionary['file_size'] = file_size
        # url_dictionary['extension'] = extension
        # url_dictionary['filename'] = self.common_filename_creator(url_dictionary)

        filename = ''

        if url_dictionary.get('prefix'):
            filename += f"{url_dictionary['prefix']}-"

        if url_dictionary.get('date'):
            dt = datetime.fromtimestamp(
                url_dictionary['date']).strftime('%Y-%m-%d')
            filename += f"{dt}-"

        if url_dictionary.get('album_name'):
            filename += f"{url_dictionary['album_name']}-"

        if url_dictionary.get('count'):
            filename += f"{url_dictionary['count']:03}-"

        if url_dictionary.get('name'):
            filename += f"{url_dictionary['name']}"

        if url_dictionary.get('description'):
            filename += f"-{url_dictionary['description']}"

        extension = self.common_find_extension(
            url_dictionary['extension']).lower()

        filename = filename.replace('\n', '  ').replace('\r', '  ')

        invalid_characters = ['/', '\\']
        filename = ''.join(
            c for c in filename if c not in invalid_characters)

        if len(str(filename)) > 220:
            filename = filename[:220]

        filename += f".{extension.lower()}"

        return filename

    async def common_file_downloader(self, url_dictionary: UrlDictionary) -> None:

        if url_dictionary.get("download"):

            await downloader.download_file(url_dictionary)

        else:

            if url_dictionary.get('url_to_record'):

                print(url_dictionary['url_to_record'])

            else:
                print(url_dictionary['url_to_download'])

    async def common_generic_downloader(self, url: str) -> None:

        response = httpx.get(url, verify=False)

        # print(response.headers)
        file_size: int = int(response.headers.get('content-length', 1))
        filename: str = url.split('/')[-1]

        url_dictionary: UrlDictionary = {}
        url_dictionary['url_to_download'] = url
        url_dictionary['filename'] = filename
        url_dictionary['file_size'] = file_size
        url_dictionary['response'] = response

        await downloader.download_file(url_dictionary.copy())

    def common_find_extension(self, extension: str) -> str:

        if extension in MIME_TYPES:
            return MIME_TYPES[extension]

        elif extension in MIME_TYPES.values():
            return extension

        else:
            return '???'


MIME_TYPES = {
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/png": "png",
    "image/gif": "gif",
    "image/bmp": "bmp",
    "image/x-bmp": "bmp",
    "image/x-ms-bmp": "bmp",
    "image/webp": "webp",
    "image/avif": "avif",
    "image/svg+xml": "svg",
    "image/ico": "ico",
    "image/icon": "ico",
    "image/x-icon": "ico",
    "image/vnd.microsoft.icon": "ico",
    "image/x-photoshop": "psd",
    "application/x-photoshop": "psd",
    "image/vnd.adobe.photoshop": "psd",

    "video/webm": "webm",
    "video/ogg": "ogg",
    "video/mp4": "mp4",
    "video/x-m4v": "m4v",
    "video/x-matroska": "mkv",
    "video/x-ms-asf": "wmv",
    "video/x-msvideo": "avi",
    "video/x-flv": "flv",
    "video/quicktime": "mov",
    "video/x-wav": "wav",

    "audio/wav": "wav",
    "audio/x-wav": "wav",
    "audio/webm": "webm",
    "audio/ogg": "ogg",
    "audio/mpeg": "mp3",
    "audio/x-m4a": "m4a",
    "audio/mpeg": "mp3",

    "application/zip": "zip",
    "application/x-zip": "zip",
    "application/x-zip-compressed": "zip",
    "application/rar": "rar",
    "application/x-rar": "rar",
    "application/x-rar-compressed": "rar",
    "application/x-7z-compressed": "7z",

    "application/pdf": "pdf",
    "application/x-pdf": "pdf",
    "application/x-shockwave-flash": "swf",

    "application/ogg": "ogg",
    # https://www.iana.org/assignments/media-types/model/obj
    "model/obj": "obj",
    "application/octet-stream": "bin",
}
