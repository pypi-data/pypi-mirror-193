import httpx
import logging
import re

from ripandtear.extractors.common import Common
from ripandtear.utils import color, rat_info

log = logging.getLogger(__name__)

re_content_link = re.compile(r"(https?://)(gfycat\.(com)/)(\w+)")

gfycat_api_url = 'https://api.gfycat.com'

prefix = 'gfycat'


class Gfycat(Common):

    async def run(self, url_dictionary):

        if re_content_link.match(url_dictionary['url']):
            content_id = re_content_link.match(url_dictionary['url']).group(4)
            await self.download_individual_gfy(content_id, url_dictionary.copy())

    async def call(self, endpoint):

        api_url = gfycat_api_url + endpoint

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(api_url, timeout=None)

        except Exception:
            return
            # log.exception("Error calling api")

        if response.status_code != 200:
            log.error(f"Bad status code: {response.status_code} - {api_url}")
            return

        data = response.json()

        return data

    async def download_individual_gfy(self, content_id, url_dictionary):
        endpoint = f"/v1/gfycats/{content_id}"
        data = await self.call(endpoint)

        try:
            url_dictionary['url_to_download'] = data['gfyItem']['mp4Url']

        except TypeError:
            log.info(f"Video deleted: {url_dictionary['url']}")
            rat_info.add_entry(category_1="urls_downloaded",
                               entry=f"url_dictionary['url']")
            color.output('red', f"{url_dictionary['url']}")
            return

        url_dictionary['prefix'] = prefix
        url_dictionary['name'] = content_id
        url_dictionary['date'] = data['gfyItem']['createDate']
        url_dictionary['file_size'] = data['gfyItem']['mp4Size']
        url_dictionary['extension'] = 'mp4'
        url_dictionary['filename'] = self.common_filename_creator(
            url_dictionary.copy())

        await self.common_file_downloader(url_dictionary.copy())
