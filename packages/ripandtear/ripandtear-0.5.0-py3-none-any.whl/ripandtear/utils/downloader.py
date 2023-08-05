import aiofiles
import httpx
import logging
import os

import yt_dlp
from tqdm import tqdm
from pathlib import Path

from ripandtear.utils import color
from ripandtear.utils import rat_info
from ripandtear.utils.custom_types import UrlDictionary

log = logging.getLogger(__name__)


async def download_file(url_dictionary: UrlDictionary) -> None:

    log.debug("Inside downloader")

    url_to_download = str(url_dictionary['url_to_download'])
    url_dictionary['url_to_download'] = url_to_download

    if url_dictionary.get("file_size"):
        file_size = int(url_dictionary['file_size'])

    else:
        file_size = 0

    log.debug("Checking if url has already been downloaded")
    if url_dictionary.get('url_to_record'):

        if rat_info.check_existence(category_1='urls_downloaded', entry=url_dictionary['url_to_record']):
            log.info(
                f"Url already recorded: {url_dictionary['url_to_record']}")
            color.output("blue", f"\n{url_dictionary['url_to_record']}")
            return
    else:

        if rat_info.check_existence(category_1='urls_downloaded', entry=url_dictionary['url_to_download']):
            log.info(f"Url already recorded: {url_to_download}")
            color.output("blue", f"\n{url_dictionary['url_to_download']}")
            return

    log.debug("url has not been downloaded yet")

    if url_dictionary.get('ytdlp_required'):
        ytdlp_download(url_dictionary)
        return

    # is_file_local returns a tuple that says if the file exists in the
    # first position and many bytes have been downloaded in the second
    # Ex: (True, 8473)

    log.debug("Checking if file exists locally")
    filename = url_dictionary['filename']
    is_file_local = local_file_exists(filename, file_size)

    try:
        if is_file_local[0] == "True":

            if is_file_local[1] == "done":

                color.output("cyan", filename)
                return

            else:

                mode = 'ab'
                initial_position = is_file_local[1]
        else:

            mode = 'wb'
            initial_position = 0

    except TypeError:
        log.error("Filename too long. Skipping")
        color.output('red', f"\n{url_dictionary['url']}")
        rat_info.add_entry(category_1='urls_downloaded',
                           entry=str(url_dictionary['url']))
        return

    headers = {'Range': f'bytes={initial_position}-'}

    if url_dictionary.get('headers'):

        for key, value in url_dictionary['headers'].items():
            headers[key] = value

    if url_dictionary.get('response') is None:
        try:
            log.debug("Sending request")

            cookies = None
            if url_dictionary.get('cookies'):
                cookies = url_dictionary['cookies']

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{url_to_download}", headers=headers, timeout=None, cookies=cookies)

        except Exception as e:
            log.exception(e)
            return
    else:
        response = url_dictionary['response']

    log.debug(f"Status Code: {response.status_code}")

    if response.status_code >= 300:
        errors(response, url_dictionary)
        return

    if file_size == 0:
        file_size = response.headers.get('content-length')

    try:

        log.debug("Preparing to download")
        async with aiofiles.open(filename, mode) as file:
            bar = tqdm(bar_format='{l_bar}{bar:40}|{n_fmt}/{total_fmt}{postfix}',
                       initial=int(initial_position),
                       total=int(file_size),
                       unit='B',
                       unit_scale=True,
                       unit_divisor=1024,
                       colour='green')

            for chunk in response.iter_bytes(chunk_size=8192):
                size = await file.write(chunk)
                bar.update(size)
                bar.set_postfix_str(f"{filename}")

    except FileNotFoundError:
        log.exception(
            f"Unable to download: {url_dictionary['url_to_download']}")
        color.output('red', f"\n{url_dictionary['url_to_download']}")
        return

    try:
        if url_dictionary.get('url_to_record'):
            rat_info.add_entry(category_1='urls_downloaded',
                               entry=url_dictionary['url_to_record'])
        else:
            rat_info.add_entry(category_1='urls_downloaded',
                               entry=url_dictionary['url_to_download'])

    except ValueError as identifier:
        log.info(identifier)


def errors(response, url_dictionary):
    if response.status_code == 403:
        log.warn(
            f"403 Authorization Error: {url_dictionary['url_to_download']}")
        color.output('red', f"\n{url_dictionary['url_to_download']}")

    elif response.status_code == 404:
        log.warn(
            f"404 Not Found: {url_dictionary['url_to_download']}")
        color.output('red', f"\n{url_dictionary['url_to_download']}")
        rat_info.add_entry(category_1='urls_downloaded',
                           entry=url_dictionary['url_to_download'])

    elif response.status_code == 429:
        log.warn(f"{response.status_code}: Too Many Requests")
        rat_info.add_error_dictionary(url_dictionary)
        color.output('red', f"\n{url_dictionary['url_to_download']}")

    elif 500 <= response.status_code < 600:
        log.warn(
            f"500 error. Saving the url to be attempted later: {response.status_code} - {url_dictionary['url_to_download']}")
        rat_info.add_error_dictionary(url_dictionary)
        color.output('red', f"\n{url_dictionary['url_to_download']}")


def local_file_exists(filename, online_file_size):

    try:
        if Path(filename).exists():

            temp = open(filename)
            temp.seek(0, os.SEEK_END)
            local_file_size = temp.tell()

            if online_file_size > 0:

                if local_file_size != online_file_size:
                    return ("True", local_file_size)

                else:
                    return ("True", "done")

            else:
                return ("False")
        else:
            return ("False")

    except OSError:
        return


def ytdlp_download(url_dictionary):

    try:
        log.info("Attempting yt_dlp download")

        ytdlp_options = {"outtmpl": url_dictionary['filename']}

        with yt_dlp.YoutubeDL(ytdlp_options) as ytdlp:
            ytdlp.download(url_dictionary['url_to_download'])

        rat_info.add_entry(category_1='urls_downloaded',
                           entry=url_dictionary['url_to_download'])
        return

    except yt_dlp.utils.DownloadError:
        log.info(
            f"Problem downloading url. Saving for later: {url_dictionary['url_to_download']}")
        rat_info.add_error_dictionary(url_dictionary)
        return
