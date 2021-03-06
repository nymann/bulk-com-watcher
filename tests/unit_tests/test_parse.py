import json

from bs4 import BeautifulSoup
from bs4.element import NavigableString
from bs4.element import Tag
from devtools import debug
import requests

from bulk_com_watcher.model import Model
from bulk_com_watcher.model import Offer

TEST_URL = "https://www.bulk.com/dk/pure-whey-proteinpulver-dk.html"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"


def test_download():
    response = requests.get(url=TEST_URL, headers={"User-Agent": USER_AGENT})
    html = response.text
    soup = BeautifulSoup(html, features="html.parser")
    relevant_soup: Tag | None | NavigableString = soup.find("script", type="application/ld+json")
    if relevant_soup is None:
        raise Exception("Couldn't find application/ld+json")
    data = json.loads(relevant_soup.text)
    b_model = Model(**data)
    assert len(b_model.offers) > 0
    looking_for = "BPB-WPC8-CCOO-"
    s: list[Offer] = []
    for offer in b_model.offers:
        if looking_for in offer.sku:
            s.append(offer)
            debug(offer, offer.price_per_gram)
    debug(b_model)

    assert False
