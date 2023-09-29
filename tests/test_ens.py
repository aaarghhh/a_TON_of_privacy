import pytest
from src.atop.atop import Ton_retriever
from src.atop.modules.telegramhelper import TelegramHelper

@pytest.fixture
def domains_ens_test():
    return ["vitalik.eth", "ahahahahahjdhassjkgsdajkhsdga.eth"]


def test_ipf2ens_ok(domains_ens_test):
    ipfs = Ton_retriever.ipf_ens(domains_ens_test[0])
    assert ipfs != ""

def test_ipf2ens_no(domains_ens_test):
    ipfs = Ton_retriever.ipf_ens(domains_ens_test[1])
    assert ipfs == ""

def test_web_client():
    result =  TelegramHelper.parse_html_page("https://t.me/aaarghhh")
    assert "user" == result["kind"]
    result = TelegramHelper.parse_html_page("https://t.me/testcanalebla")
    assert "channel" == result["kind"]
    result = TelegramHelper.parse_html_page("https://t.me/gruppotest01")
    assert "group" == result["kind"]

def test_telegram_api():
    current_parser = Ton_retriever("+888...", True, False, True, True, None, "0000",
                                   "000000000", None, "000=")
    current_parser.start_searching()
    found = False
    if current_parser.nfts:
        if "data" in current_parser.nfts.keys():
            print(current_parser.nfts["data"])
            if "nftItemsByOwner" in current_parser.nfts["data"].keys():
                found = True
    assert found == True


