import logging
import re

import bs4
import requests

_logger = logging.getLogger(__name__)

pat = re.compile(
    r"https://efa-installer.amazonaws.com/aws-efa-installer-(?P<version>[\.\d]+).tar.gz"
)


def get_efa_version(url: str) -> str:
    _logger.debug(f"fetching {url}")
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    _logger.debug(f"parsing html from {url}")
    text = soup.get_text()

    mo = pat.search(text, re.IGNORECASE)

    version = None
    if mo:
        version = mo.group("version")
        _logger.debug(f"found version {version}")

    if not mo:
        _logger.fatal(f"couldn't find version number in html page {url}")

    return version


def to_int(version: str) -> int:
    lst = [int(x, 10) for x in version.split(".")]
    lst.reverse()
    version = sum(x * (10**i) for i, x in enumerate(lst))
    return version
