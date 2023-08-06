import logging
import sys


def create_logger(level=50):

    logging.basicConfig(level=level,
                        stream=sys.stdout,
                        format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
                        datefmt='%Y/%m/%d %H:%M:%S'
                        )
    httpx = logging.getLogger('httpx')
    httpx.setLevel(logging.WARNING)
