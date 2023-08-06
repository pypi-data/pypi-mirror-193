import re
from bs4 import BeautifulSoup
import httpx
import logging

from yt_dlp.utils import asyncio

from ripandtear.extractors.common import Common
from ripandtear.utils import color
from ripandtear.utils import rat_info
from ripandtear.utils.custom_types import UrlDictionary

log = logging.getLogger(__name__)

sem = asyncio.Semaphore(6)

root_url = "https://tiktits.com/"

re_user_profile = re.compile(
    r"(users/)([\w\-_\(\)]+)")

re_video_page = re.compile(r"video/([\w\-_\(\)]+)")

re_direct_video_url = re.compile(
    r"(assets/)(uploads/)([\w\-_\(\)]+)\.(\w+)")

prefix = 'tiktits'


class Tiktits(Common):

    def __init__(self):

        self.already_downloaded_urls = rat_info.get_downloaded_urls()

    async def run(self, url_dictionary):
        log.debug("Inside tiktits")

        if re_user_profile.search(url_dictionary['url']):
            await self.user_profile_download(url_dictionary.copy())

        elif re_video_page.search(url_dictionary['url']):
            await self.video_page_download(url_dictionary.copy())

        elif re_direct_video_url.search(url_dictionary['url']):
            await self.direct_video_download(url_dictionary.copy())

        else:
            log.info(f"No regex pattern matches: {url_dictionary['url']}")
            color.output('red', f"{url_dictionary['url']}")

    async def call(self, endpoint) -> httpx.Response | None:

        url = f"https://tiktits.com/{endpoint}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=None)

        except Exception:
            log.exception(f"Problem downloading: {url}")
            return

        if response.status_code >= 300:
            log.error(f"Bad status code: {response.status_code} - {url} ")
            return

        return response

    async def user_profile_download(self, url_dictionary: UrlDictionary) -> None:
        endpoint = re_user_profile.search(url_dictionary['url']).group()

        response = await self.call(endpoint)

        soup = BeautifulSoup(response.text, 'html.parser')

        all_videos = soup.find('div', {'class': 'categories__list'})

        all_video_containers = all_videos.find_all('a')

        tasks = []
        for container in all_video_containers:

            url_dictionary['url'] = f"{root_url}{container['href']}"

            tasks.append(asyncio.create_task(self.run(url_dictionary.copy())))

        await asyncio.gather(*tasks)

    async def video_page_download(self, url_dictionary: UrlDictionary) -> None:

        async with sem:

            if url_dictionary['url'] in self.already_downloaded_urls:
                return

            endpoint = re_video_page.search(url_dictionary['url']).group()
            response = await self.call(endpoint)

            soup = BeautifulSoup(response.text, 'html.parser')

            video = soup.find('video', {'class': 'lazy-video'})
            video_sources = video.find_all('source')
            highest_quality_video = video_sources[0]['src']

            url = f"{root_url}{highest_quality_video}"
            url_dictionary['url'] = url
            url_dictionary['url_to_record'] = str(response.url)

            await self.run(url_dictionary.copy())

    async def direct_video_download(self, url_dictionary: UrlDictionary) -> None:

        endpoint = re_direct_video_url.search(url_dictionary['url']).group()

        response = await self.call(endpoint)

        if response is None:
            return

        url_dictionary['response'] = response
        url_dictionary['prefix'] = prefix
        url_dictionary['url_to_download'] = str(response.url)

        if response.headers.get('content-length'):
            url_dictionary['file_size'] = response.headers.get(
                'content-length')
        else:
            url_dictionary['file_size'] = None

        url_dictionary['name'] = re_direct_video_url.search(
            url_dictionary['url']).group(3)
        url_dictionary['extension'] = response.headers.get('content-type')

        url_dictionary['filename'] = self.common_filename_creator(
            url_dictionary.copy())

        await self.common_file_downloader(url_dictionary.copy())
