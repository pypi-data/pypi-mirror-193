import logging
import re

from ripandtear.extractors.bunkr import Bunkr
from ripandtear.extractors.cyberdrop import Cyberdrop
from ripandtear.extractors.imgur import Imgur
from ripandtear.extractors.jpg import Jpg
from ripandtear.extractors.gofile import Gofile
from ripandtear.extractors.gfycat import Gfycat
from ripandtear.extractors.reddit import Reddit
from ripandtear.extractors.redgifs import Redgifs
from ripandtear.utils.custom_types import UrlDictionary

log = logging.getLogger(__name__)


stored_class_instances = dict()


bunkr_re = re.compile(r"(https?://)([\w\-]+\.)?(bunkr\.(ru|la|su|is))")

cyberdrop_re = re.compile(
    r"(https?://)(www\.|[\w\-]+\.)?(cyberdrop\.(me|cc|to))")

gofile_re = re.compile(r"(https?://)(gofile\.io)")

gfycat_re = re.compile(r"(https?://)(gfycat\.com(/))")

imgur_re = re.compile(r"(https?://)?(www\.|[im]\.)?imgur\.(?:com|io)")

jpg_re = re.compile(r"(https?://)(\w+\.)?(jpg\.(church|fish))")

reddit_re = re.compile(r"(https?://)([iv]\.|www\.)?(reddit|redd\.it)")

redgifs_re = re.compile(r"(https?://)(v3\.|www\.|i.)?(redgifs.com)")


async def validate_url(url_dictionary: UrlDictionary) -> None:

    # elif _re.search(url_dictionary['url']):
    #     log.info('[] Attempting Extraction')
    #     await (url_dictionary)
    #     return

    if bunkr_re.search(url_dictionary['url']):
        log.info('[BUNKR] Attempting Extraction')
        await bunkr(url_dictionary)
        return

    elif cyberdrop_re.search(url_dictionary['url']):
        log.info('[CYBERDROP] Attempting Extraction')
        await cyberdrop(url_dictionary)
        return

    elif gofile_re.search(url_dictionary['url']):
        log.info('[GOFILE] Attempting Extraction')
        await gofile(url_dictionary)
        return

    elif gfycat_re.search(url_dictionary['url']):
        log.info('[GFYCAT] Attempting Extraction')
        await gfycat(url_dictionary)
        return

    elif imgur_re.search(url_dictionary['url']):
        log.info('[IMGUR] Attempting Extraction')
        await imgur(url_dictionary)
        return

    elif jpg_re.search(url_dictionary['url']):
        log.info('[JPG] Attempting Extraction')
        await jpg(url_dictionary)
        return

    elif redgifs_re.search(url_dictionary['url']):
        log.info('[REDGIFS] Attempting Extraction')
        await redgifs(url_dictionary)
        return

    elif reddit_re.search(url_dictionary['url']):
        log.info('[REDDIT] Attempting Extraction')
        await reddit(url_dictionary)
        return

    else:
        log.info(f"No extractor found for: {url_dictionary['url']}")


async def template(url_dictionary: UrlDictionary) -> None:

    if "" not in stored_class_instances.keys():
        log.debug("Creating  class")
        stored_class_instances[""] = Imgur()

    log.debug("Passing to ")
    await stored_class_instances[""].run(url_dictionary)


async def bunkr(url_dictionary: UrlDictionary) -> None:

    if "bunkr" not in stored_class_instances.keys():
        log.debug("Creating bunkr class")
        stored_class_instances["bunkr"] = Bunkr()

    log.debug("Passing to bunkr")
    await stored_class_instances["bunkr"].run(url_dictionary)


async def cyberdrop(url_dictionary: UrlDictionary) -> None:

    if "cyberdrop" not in stored_class_instances.keys():
        log.debug("Creating cyberdrop class")
        stored_class_instances["cyberdrop"] = Cyberdrop()

    log.debug("Passing to cyberdrop")
    await stored_class_instances["cyberdrop"].run(url_dictionary)


async def gofile(url_dictionary: UrlDictionary) -> None:

    if "gofile" not in stored_class_instances.keys():
        log.debug("Creating gofile class")
        stored_class_instances["gofile"] = Gofile()

    log.debug("Passing to gofile")
    await stored_class_instances["gofile"].run(url_dictionary)


async def gfycat(url_dictionary: UrlDictionary) -> None:

    if "gfycat" not in stored_class_instances.keys():
        log.debug("Creating gfycat class")
        stored_class_instances["gfycat"] = Gfycat()

    log.debug("Passing to gfycat")
    await stored_class_instances["gfycat"].run(url_dictionary)


async def imgur(url_dictionary: UrlDictionary) -> None:

    if "imgur" not in stored_class_instances.keys():
        log.debug("Creating imgur class")
        stored_class_instances["imgur"] = Imgur()

    log.debug("Passing to imgur")
    await stored_class_instances["imgur"].run(url_dictionary)


async def jpg(url_dictionary: UrlDictionary) -> None:

    if "jpg" not in stored_class_instances.keys():
        log.debug("Creating jpg class")
        stored_class_instances["jpg"] = Jpg()

    log.debug("Passing to jpg")
    await stored_class_instances["jpg"].run(url_dictionary)


async def reddit(url_dictionary: UrlDictionary) -> None:

    if "reddit" not in stored_class_instances.keys():
        log.debug("Creating reddit class")
        stored_class_instances["reddit"] = Reddit()

    log.debug("Passing to reddit")
    await stored_class_instances["reddit"].run(url_dictionary)


async def redgifs(url_dictionary: UrlDictionary) -> None:

    if "redgifs" not in stored_class_instances.keys():
        log.debug("Creating redgifs class")
        stored_class_instances["redgifs"] = Redgifs()

    log.debug("Passing to redgifs")
    await stored_class_instances["redgifs"].run(url_dictionary)
