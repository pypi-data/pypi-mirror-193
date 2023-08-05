import asyncio
import httpx
import logging
import re

from bs4 import BeautifulSoup
from ripandtear.extractors.common import Common
from ripandtear.utils.custom_types import UrlDictionary
from ripandtear.utils import color
from ripandtear.utils import rat_info

log = logging.getLogger(__name__)

sem = asyncio.Semaphore(6)

re_cyberdrop_album = re.compile(
    r"(https?://)(www\.)?(cyberdrop\.(me))(/a/)(\w+)")

re_cyberdrop_single = re.compile(
    r"(https?://)([\w-]+\.)(cyberdrop\.(cc|to))/([\w\-_\(\)\%\+]+)\.(\w+)")


class Cyberdrop(Common):

    async def run(self, url_dictionary: UrlDictionary) -> None:

        if re_cyberdrop_single.match(url_dictionary['url']):
            await self.single_downloader(url_dictionary)

        if re_cyberdrop_album.match(url_dictionary['url']):
            await self.album_downloader(url_dictionary)

    async def single_downloader(self, url_dictionary: UrlDictionary) -> None:

        async with sem:
            log.info(
                f"Individual file found. Attempting download: {url_dictionary['url']}")
            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.get(url_dictionary['url'], timeout=None, follow_redirects=True)
            except httpx.ReadError:
                log.warn(
                    f"Problem downloading url. Saving for later: {url_dictionary['url']}")
                rat_info.add_error_dictionary(url_dictionary.copy())
                return

            # print(response.headers)
            url_dictionary['response'] = response
            url_dictionary['name'] = re_cyberdrop_single.match(
                url_dictionary['url']).group(5)
            url_dictionary['extension'] = response.headers.get('content-type')
            url_dictionary['url_to_download'] = url_dictionary['url']
            url_dictionary['file_size'] = int(
                response.headers.get('content-length'))
            url_dictionary['filename'] = self.common_filename_creator(
                url_dictionary.copy())

            # print(url_dictionary)
            await self.common_file_downloader(url_dictionary.copy())

    async def album_downloader(self, url_dictionary: UrlDictionary) -> None:

        log.info(
            f"Cyberdrop album found. Attempting download: {url_dictionary['url']}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url_dictionary['url'], timeout=None)

        log.debug("Got response. Parsing for individual file urls")
        try:
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('div', {"id": "table"})
            hrefs = table.find_all('a', {"class": "image"})

        except AttributeError:
            log.info(f"Album deleted: {url_dictionary['url']}")
            color.output('red', f"{url_dictionary['url']}")
            rat_info.add_entry(category_1='urls_downloaded',
                               entry=url_dictionary['url'])
            return

        tasks = []
        already_downloaded_urls = rat_info.get_downloaded_urls()

        log.info("Preparing to download individual files")
        for link in hrefs:
            url = str(link['href'])
            url = url.replace(" ", "%20")

            if already_downloaded_urls is not None:
                if url in already_downloaded_urls and url_dictionary['download'] is True:
                    continue

                elif url not in already_downloaded_urls and url_dictionary['download'] is True:
                    url_dictionary['url'] = url
                    tasks.append(asyncio.create_task(
                        self.run(url_dictionary.copy())))

                elif url_dictionary['download'] is False:
                    print(url)

            elif url_dictionary['download'] is False:
                print(url)

            else:
                url_dictionary['url'] = url
                tasks.append(asyncio.create_task(
                    self.run(url_dictionary.copy())))

        await asyncio.gather(*tasks)
