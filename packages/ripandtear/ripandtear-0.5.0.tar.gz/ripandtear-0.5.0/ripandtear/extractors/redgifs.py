import asyncio
import httpx
import logging
import re

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

from ripandtear.extractors.common import Common
from ripandtear.utils.custom_types import UrlDictionary
from ripandtear.utils import color
from ripandtear.utils import rat_info

log = logging.getLogger(__name__)


prefix = "redgifs"
url_root = "https://www.redgifs.com/"
url_root_v3 = "https://v3.redgifs.com/"

single_uid_api = "https://api.redgifs.com/v2/gifs/"

re_extension = re.compile(
    r"(https?://)(\w+\.)(redgifs.com/)(\w+)(-\w+)?\.(\w+)")

re_watch_uid = re.compile(
    r"(/watch/)(\w+)#")

# 'https://i.redgifs.com/i/kosherpurehairstreak.jpg'
# https://v3.redgifs.com/watch/heavyimperfectkookaburra#rel=user%3Alamsinka89
re_single_uid = re.compile(
    r"(https?://)(\w+\.)?(redgifs.com/)(watch|i)/(\w+)")

re_url_to_record = re.compile(
    r"((https?://)(\w+\.)?(redgifs.com/)(watch|i)/(\w+))")

# https://v3.redgifs.com/users/lamsinka89
re_user = re.compile(
    r"((https?://)(\w+\.)?(redgifs\.com)/(users)/(\w+))")

sem = asyncio.Semaphore(6)


class Redgifs(Common):

    async def get_token(self) -> None:

        log.debug("Requesting auth token")
        headers = {'token': ''}

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.redgifs.com/v2/auth/temporary", headers=headers, timeout=None)

        data = response.json()

        self.headers = {'authorization': f"Bearer {data['token']}"}

        log.debug("Auth token set")

    async def run(self, url_dictionary: UrlDictionary) -> None:

        await self.get_token()

        if re_single_uid.match(url_dictionary['url']):

            log.debug("Single image found. Sending to single single_download")
            await self.single_download(re_single_uid.match(
                url_dictionary['url']).group(5), url_dictionary.copy())

        elif re_user.match(url_dictionary['url']):

            log.debug("User found. Sending to user_download_v3")
            await self.user_download_v3(re_user.match(
                url_dictionary['url']).group(6), url_dictionary.copy())

    async def single_download(self, uid: str, url_dictionary: UrlDictionary) -> None:

        async with sem:

            log.debug("Single image given. Attempting download")

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{single_uid_api}{uid}", headers=self.headers, timeout=None)

            data = response.json()
            # print(data)

            if 'error' in data:

                log.info(f"File Deleted: {url_dictionary['url']}")
                color.output('red', url_dictionary['url'])
                rat_info.add_entry(category_1='urls_downloaded',
                                   entry=url_dictionary['url'])

            else:

                url_dictionary['prefix'] = prefix
                url_dictionary['name'] = data['gif']['id']
                url_dictionary['date'] = data['gif']['createDate']
                url_dictionary['url_to_download'] = data['gif']['urls']['hd']
                url_dictionary['url_to_record'] = re_url_to_record.match(
                    url_dictionary['url']).group(1)

                url_dictionary['file_size'] = None
                url_dictionary['extension'] = re_extension.match(
                    url_dictionary['url_to_download']).group(6)
                url_dictionary['filename'] = self.common_filename_creator(
                    url_dictionary)

                log.debug("url_dictionary built. Sending to downloader")

                await self.common_file_downloader(url_dictionary.copy())

    async def user_download_v3(self, username: str, url_dictionary: UrlDictionary) -> None:

        log.info(f"Redgifs user Found: {username}")

        user_url = f"https://v3.redgifs.com/users/{username}"

        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            page = await browser.new_page()
            await page.goto(user_url)

            log.info("Searching for videos")
            content = await page.query_selector_all('a.tile')

            stop_scolling = False
            while stop_scolling is False:

                for x in range(5):
                    await page.keyboard.down('PageDown')
                    await page.wait_for_timeout(200)

                new_content = await page.query_selector_all('a.tile')

                if len(new_content) > len(content):

                    content = new_content
                    log.info(f"Gifs found: {len(new_content)}")

                else:

                    content = new_content
                    stop_scolling = True

            html = await page.locator('div.gifList').inner_html()
            await page.close()
            await browser.close()

            soup = BeautifulSoup(html, features='html.parser')

            already_downloaded_urls: list[str] = rat_info.get_downloaded_urls()
            tasks = []
            for links in soup.find_all('a'):

                link = links.get('href')

                uid = re_watch_uid.match(link).group(2)
                url = f"https://v3.redgifs.com/watch/{uid}"

                if url in already_downloaded_urls and url_dictionary['download'] is True:
                    log.info(f"Already downloaded: {url}")
                    continue

                elif url_dictionary['download'] is False:
                    print(url)

                else:
                    log.info(f"Creating task out of {uid}")

                    url_dictionary['url'] = url
                    tasks.append(asyncio.create_task(
                        self.single_download(uid, url_dictionary.copy())))

            log.info("Executing tasks")
            await asyncio.gather(*tasks)
