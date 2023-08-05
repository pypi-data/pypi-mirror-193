import asyncio
import logging
import sys

from ripandtear.__init__ import __version__
from ripandtear.extractors.common import Common
from ripandtear.utils.custom_types import UrlDictionary
from ripandtear.utils import cli_arguments
from ripandtear.utils import conductor
from ripandtear.utils import logger
from ripandtear.utils import rat_info
from ripandtear.utils import file_sorter
from ripandtear.utils import file_hasher


async def main():

    try:

        parser = cli_arguments.make_args()
        args = parser.parse_args()

        if args.version:
            print(f"version: {__version__}")

        if args.log_level:

            if args.log_level == '1' or args.log_level.lower() == 'debug':
                level = logging.DEBUG
                logger.create_logger(level)
                log = logging.getLogger(__name__)
                log.debug("logging working")

            elif args.log_level == '2' or args.log_level.lower() == 'info':
                level = logging.INFO
                logger.create_logger(level)
                log = logging.getLogger(__name__)
                log.info("logging working")

            elif args.log_level == '3' or args.log_level.lower() == 'warning':
                level = logging.WARNING
                logger.create_logger(level)
                log = logging.getLogger(__name__)
                log.warning("logging working")

            elif args.log_level == '4' or args.log_level.lower() == 'error':
                level = logging.ERROR
                logger.create_logger(level)
                log = logging.getLogger(__name__)
                log.error("logging working")

            elif args.log_level == '5' or args.log_level.lower() == 'critical':
                level = logging.CRITICAL
                logger.create_logger(level)
                log = logging.getLogger(__name__)
                log.critical("logging working")

            else:
                print("Incorrect input to get logging")
        else:
            level = logging.CRITICAL
            logger.create_logger(level)

        if args.print_chaturbate:
            rat_info.print_rat('names', 'chaturbate')

        if args.print_coomer:
            rat_info.print_rat('links', 'coomer')

        if args.print_errors:
            rat_info.print_rat('errors')

        if args.print_fansly:
            rat_info.print_rat('names', 'fansly')

        if args.print_instagram:
            rat_info.print_rat('names', 'instagram')

        if args.print_myfreecams:
            rat_info.print_rat('names', 'myfreecams')

        if args.print_reddit:
            rat_info.print_rat('names', 'reddit')

        if args.print_redgifs:
            rat_info.print_rat('names', 'redgifs')

        if args.print_onlyfans:
            rat_info.print_rat('names', 'onlyfans')

        if args.print_patreon:
            rat_info.print_rat('names', 'patreon')

        if args.print_pornhub:
            rat_info.print_rat('names', 'pornhub')

        if args.print_simpcity:
            rat_info.print_rat('links', 'simpcity')

        if args.print_tiktok:
            rat_info.print_rat('names', 'tiktok')

        if args.print_tumblr:
            rat_info.print_rat('names', 'tumblr')

        if args.print_twitter:
            rat_info.print_rat('names', 'twitter')

        if args.print_twitch:
            rat_info.print_rat('names', 'twitch')

        if args.print_urls_downloaded:
            rat_info.print_rat('urls_downloaded')

        if args.print_urls_to_download:
            rat_info.print_rat('urls_to_download')

        if args.print_youtube:
            rat_info.print_rat('names', 'youtube')

        if args.reddit:
            for entry in args.reddit:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'reddit', name)

        if args.redgifs:
            for entry in args.redgifs:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'redgifs', name)

        if args.onlyfans:
            for entry in args.onlyfans:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'onlyfans', name)

        if args.fansly:
            for entry in args.fansly:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'fansly', name)

        if args.pornhub:
            for entry in args.pornhub:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'pornhub', name)

        if args.twitter:
            for entry in args.twitter:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'twitter', name)

        if args.instagram:
            for entry in args.instagram:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'instagram', name)

        if args.youtube:
            for entry in args.youtube:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'youtube', name)

        if args.tiktok:
            for entry in args.tiktok:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'tiktok', name)

        if args.twitch:
            for entry in args.twitch:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'twitch', name)

        if args.patreon:
            for entry in args.patreon:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'patreon', name)

        if args.tumblr:
            for entry in args.tumblr:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'tumblr', name)

        if args.myfreecams:
            for entry in args.myfreecams:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'myfreecams', name)

        if args.chaturbate:
            for entry in args.chaturbate:
                for name in entry.split(','):
                    rat_info.update_rat('names', 'chaturbate', name)

        if args.simp:
            for entry in args.simp:
                for url in entry.split(','):
                    rat_info.update_rat('links', 'simpcity', url)

        if args.coomer:
            for entry in args.coomer:
                for url in entry.split(','):
                    rat_info.update_rat('links', 'coomer', url)

        if args.url_add:
            for entry in args.url_add:
                for url in entry.split(','):
                    rat_info.update_rat('urls_to_download', None, url)

        if args.urls_downloaded:
            for entry in args.urls_downloaded:
                for url in entry.split(','):
                    rat_info.update_rat('urls_downloaded', None, url)

        if args.erase_errors:
            rat_info.erase_error_dictionaries()

        if args.get_urls:

            await print_urls(args)

        if args.download:

            await download_urls(args)

        if args.generic_download:

            for entry in args.generic_download:
                for url in entry.split(','):
                    if args.output:
                        filename: str = args.output.split(',')[0]
                    else:
                        common = Common()
                        await common.common_generic_downloader(url.strip())

        if args.sync_all:
            await sync_all()

        if args.sync_errors:
            await sync_errors()

        if args.sync_reddit:
            await sync_reddit()

        if args.sync_redgifs:
            await sync_redgifs()

        if args.sync_urls_to_download:
            await sync_urls_to_download()

        if args.hash_files:
            await file_hasher.file_hasher()

        if args.sort_files:

            await file_sorter.sort()

    except KeyboardInterrupt:
        print()
        print("Cancelled via keyboard")


def url_dictionary_constructor(url: str, download: bool) -> UrlDictionary:

    url_dictionary: UrlDictionary = {}
    url_dictionary['url'] = url

    url_dictionary['download'] = download

    return url_dictionary


async def download_urls(args):

    tasks = []

    for entry in args.download:
        for url in entry.split(','):

            url_dictionary: UrlDictionary = url_dictionary_constructor(
                url.strip(), download=True)

            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))

    await asyncio.gather(*tasks)


async def print_urls(args):

    tasks = []

    for entry in args.get_urls:
        for url in entry.split(','):

            url_dictionary: UrlDictionary = url_dictionary_constructor(
                url.strip(), download=False)

            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))

    await asyncio.gather(*tasks)


async def sync_reddit() -> None:

    reddit_names: list[str] = rat_info.print_rat(
        'names', 'reddit', respond=True)

    if len(reddit_names) >= 1:

        tasks = []
        for name in reddit_names:
            url: str = f"https://www.reddit.com/user/{name}/submitted"
            url_dictionary: UrlDictionary = url_dictionary_constructor(
                url, download=True)
            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))
        await asyncio.gather(*tasks)

    else:
        return


async def sync_redgifs() -> None:

    redgifs_names: list[str] = rat_info.print_rat(
        'names', 'redgifs', respond=True)

    if len(redgifs_names) >= 1:

        tasks = []
        for name in redgifs_names:
            url: str = f"https://www.redgifs.com/users/{name}"
            url_dictionary: UrlDictionary = url_dictionary_constructor(
                url, download=True)
            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))
        await asyncio.gather(*tasks)

    else:
        return


async def sync_urls_to_download() -> None:

    urls_to_download = rat_info.get_urls_to_download()

    if len(urls_to_download) >= 1:

        tasks = []
        for url in urls_to_download:
            url_dictionary: UrlDictionary = url_dictionary_constructor(
                url, download=True)
            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))
        await asyncio.gather(*tasks)

    else:
        return


async def sync_errors() -> None:

    error_dictionaries = rat_info.get_error_dictionaries()

    if len(error_dictionaries) >= 1:

        tasks = []
        for url_dictionary in error_dictionaries:
            tasks.append(asyncio.create_task(
                conductor.validate_url(url_dictionary.copy())))
        await asyncio.gather(*tasks)

    else:
        return


async def sync_all() -> None:
    await sync_reddit()
    await sync_redgifs()
    await sync_urls_to_download()


def launch():

    try:
        sys.exit(asyncio.run(main()))

    except KeyboardInterrupt:
        sys.exit("\nCancelled via keyboard")

    except RuntimeError:
        pass


if __name__ == "__main__":
    launch()
