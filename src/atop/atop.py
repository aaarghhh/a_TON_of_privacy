from colorama import Fore, Style
import requests

import re
import json
import argparse
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from atop.modules.telegramhelper import TelegramHelper
from atop.modules.const import user_agent
import os

delays = [0.2, 0.5, 0.6, 0.5, 0.1, 0.4, 1]


def gdelay():
    return random.choice(delays)


def print_banner():
    print(
        """
Welcome in the realm of....."""
        + Fore.RED
        + """

 ▄▄▄         ▄▄▄█████▓ ▒█████   ███▄    █     ▒█████    █████▒   
▒████▄       ▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █    ▒██▒  ██▒▓██   ▒    
▒██  ▀█▄     ▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒   ▒██░  ██▒▒████ ░    
░██▄▄▄▄██    ░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒   ▒██   ██░░▓█▒  ░    
 ▓█   ▓██▒     ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░   ░ ████▓▒░░▒█░       
 ▒▒   ▓▒█░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▒░▒░  ▒ ░       
  ▒   ▒▒ ░       ░      ░ ▒ ▒░ ░ ░░   ░ ▒░     ░ ▒ ▒░  ░         
  ░   ▒        ░      ░ ░ ░ ▒     ░   ░ ░    ░ ░ ░ ▒   ░ ░       
      ░  ░                ░ ░           ░        ░ ░             
                                                                 
 ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄       ▄████▄▓██   ██▓        
▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄    ▒██▀ ▀█ ▒██  ██▒        
▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄  ▒▓█    ▄ ▒██ ██░        
▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▐██▓░        
▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒▒ ▓███▀ ░░ ██▒▓░        
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░░ ░▒ ▒  ░ ██▒▒▒         
░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░  ░  ▒  ▓██ ░▒░         
░░         ░░   ░  ▒ ░     ░░    ░   ▒   ░       ▒ ▒ ░░          
            ░      ░        ░        ░  ░░ ░     ░ ░             
                           ░             ░       ░ ░             
v 0.1.8 """
        + Style.RESET_ALL
    )


class Ton_retriever:
    telegram_pivot = False
    silent = False
    step = 10000
    offset = 0
    target = ""
    tor_proxy = False

    comprehensive = False
    currentua = ""
    address = ""
    nft_name = ""
    is_scam = ""
    owner_name = ""
    info = None
    transactions = None
    nfts = None
    type = ""
    kind = ""
    ens_detail = None
    session = None

    asset_in_sale = False

    # pivoting Telegram account
    api_hash = None
    api_id = None
    api_telephone = None
    sessionstring = None
    tgchecker = None
    outputdir = None

    proxy = False
    s_proto = "socks5"
    s_proxy = "127.0.0.1"
    s_port = "9050"

    @staticmethod
    def sleeping_time():
        time.sleep(gdelay())

    @staticmethod
    def ipf_ens(domain, session=None):
        ipfs_url = ""
        request_api = f"https://{domain}.limo"
        try:
            if not session:
                res = requests.get(request_api, timeout=5)
            else:
                res = session.get(request_api, timeout=5)
            if res.status_code == 200:
                ipfs_url = res.headers["X-Ipfs-Path"]
        except Exception as exx:
            pass
        time.sleep(0.3)
        return ipfs_url

    def get_session(self):
        ## session stora i cookie
        self.session = requests.session()
        if self.proxy:
            self.session.proxies = {
                "http": f"{self.s_proto}://{self.s_proxy}:{self.s_port}",
                "https": f"{self.s_proto}://{self.s_proxy}:{self.s_port}",
            }
            self.user_agent_retrieve(self)
            self.session.headers = {"User-Agent": self.ua()}

    def __init__(
        self,
        _telephone_num,
        _comprehensive,
        _tor,
        _silent,
        _telegram_pivot,
        outputdir=None,
        telegram_api_hash=None,
        telegram_api_id=None,
        telegram_api_telephone=None,
        sessionstring=None,
    ):
        if _telegram_pivot:
            load_dotenv()
            try:
                self.api_id = os.getenv("API_ID")
                self.api_hash = os.getenv("API_HASH")
                self.api_telephone = os.getenv("PHONE_NUMBER")
                self.sessionstring = os.getenv("SESSION_STRING")
                if not self.api_id and telegram_api_id:
                    self.api_id = telegram_api_id
                if not self.api_hash and telegram_api_hash:
                    self.api_hash = telegram_api_hash
                if not self.api_telephone and telegram_api_telephone:
                    self.api_telephone = telegram_api_telephone
                if not self.sessionstring and sessionstring:
                    self.sessionstring = sessionstring
                self.outputdir = outputdir
                if not (
                    (self.api_telephone != "" or self.sessionstring)
                    and (self.api_hash != "" and self.api_telephone != "")
                ):
                    print(
                        "You have to setup your sockpuppet.. you haven't compiled your env data.. "
                    )
                    exit(0)
                else:
                    self.telegram_pivot = True
                self.tgchecker = TelegramHelper(
                    self.api_hash,
                    self.api_id,
                    self.api_telephone,
                    self.outputdir,
                    self.sessionstring,
                )
            except Exception as exx:
                pass

        self.comprehensive = _comprehensive
        if not self.check_format(_telephone_num):
            if not self.silent:
                print("\n [!] WRONG INPUT FORMAT")
            return 1
        self.stop_cycle = False
        self.proxy = _tor
        self.silent = _silent
        self.get_session()
        if not self.silent:
            print(f"\n [!] START CRAWLING.... {self.kind}: {self.target} \n")

    """
        TON DNS 0:b774d95eb20543f186c06b371ab88ad704f7e256130caf96189368a7d0cb6ccf
        TON NICKNAME 0:80d78a35f955a14b679faa887ff4cd5bfc0f43b4a4eea2a7e6927f3701b273c2
        TON NUMBERS 0:0e41dc1dc3c9067ed24248580e12b3359818d83dee0304fabcf80845eafafdb2
    """

    def check_format(self, _string):
        status = False
        if re.match(r"\+?888[0-9\s]{0,12}", _string.strip()):
            status = True
            if _string[0] != "+":
                _string = "+" + _string
            self.target = _string.replace(" ", "")
            self.kind = "NUMBER"
            self.type = (
                "0e41dc1dc3c9067ed24248580e12b3359818d83dee0304fabcf80845eafafdb2"
            )
        if re.match(r"[a-z0-9-_]+\.ton", _string.strip()):
            status = True
            self.target = _string.strip()
            self.kind = "DOMAIN"
            self.type = (
                "b774d95eb20543f186c06b371ab88ad704f7e256130caf96189368a7d0cb6ccf"
            )
        if re.match(r"@[a-z0-9]", _string.strip()):
            status = True
            self.target = _string.strip()
            self.kind = "NICKNAME"
            self.type = (
                "80d78a35f955a14b679faa887ff4cd5bfc0f43b4a4eea2a7e6927f3701b273c2"
            )
        return status

    def user_agent_retrieve(self):
        try:
            for browser in ["chrome", "edge", "firefox", "safari", "opera"]:
                with self.session.get(
                    f"http://useragentstring.com/pages/useragentstring.php?name={browser}"
                ) as response:
                    tt = response.content.decode("utf-8")
                    count = 10
                    for ua in re.findall(r"<li><a[^>]*>([^<]*)<\/a><\/li>", tt):
                        if ua not in self.user_agents:
                            self.user_agents.append(ua)
                        count -= 1
                        if count == 0:
                            break
        except Exception as exx:
            self.user_agents = user_agent

    def ua(self):
        return random.choice(self.user_agents)

    def print_info(self):
        if not self.address:
            print(f" [-] {self.kind} NOT FOUND, {self.offset} {self.kind} PROCESSED...")
            return
        else:
            balance = "N/A"
            last_date = datetime.min
            print(
                """
      ░▒████████████████████ TON ██████████████████████▒░                   
                    """
            )

            header = f" [+] Details for {self.kind.lower()}: " + self.target
            if self.asset_in_sale:
                header = header + " ( asset in sale! )"
            print(header)
            print("  ├  Owner address: ", str(self.address))
            print("  ├  Is scam: ", str(self.is_scam))
            if self.owner_name != "":
                print("  ├  Owner name: ", str(self.owner_name))

            if self.info:
                if "result" in self.info.keys():
                    balance = str(int(self.info["result"]["balance"]) / 1000000000)

            if self.transactions and len(self.transactions):
                last_date = datetime.fromtimestamp(self.transactions[0]["utime"])

            print("  ├  Last activity: ", last_date.strftime("%Y-%m-%d %H:%M:%S"))
            print("  ├  Balance: ", str(balance))
            print("  └  ------------------------------------\n")

            processnft = False
            if self.nfts:
                if "data" in self.nfts.keys():
                    if "nftItemsByOwner" in self.nfts["data"].keys():
                        print(
                            " [+] ",
                            "NFTs found: %s"
                            % len(self.nfts["data"]["nftItemsByOwner"]["items"]),
                        )
                        processnft = True
            if processnft:
                first = True
                for nftff in self.nfts["data"]["nftItemsByOwner"]["items"]:
                    if not first:
                        print("  |")
                    print("  ├  Address: %s" % (nftff["address"]))
                    print("  |  Name: %s, Kind: %s" % (nftff["name"], nftff["kind"]))
                    is_collection = ""
                    if "collection" in nftff.keys() and nftff["collection"]:
                        is_collection = nftff["collection"]["name"]
                        print("  |  Collection: %s" % (is_collection))
                        ## pivoting Telegram account
                        if (
                            "tg-data" in nftff.keys()
                            and self.telegram_pivot
                            and nftff["tg-data"]
                        ):
                            if nftff["tg-data"][1] and nftff["tg-data"][1] > 0:
                                TelegramHelper.print_entity(nftff["tg-data"])

                    if "image" in nftff.keys() and nftff["image"]:
                        if (
                            "originalUrl" in nftff["image"].keys()
                            and nftff["image"]["originalUrl"]
                        ):
                            print("  |  Url: %s" % (nftff["image"]["originalUrl"]))
                    first = False
                print("  └  ------------------------------------")

            if self.comprehensive and self.ens_detail:
                print(
                    """
      ░▒████████████████████ ETH ██████████████████████▒░                   
                    """
                )
                if "data" in self.ens_detail.keys():
                    if "domains" in self.ens_detail["data"].keys():
                        if len(self.ens_detail["data"]["domains"]) == 1:
                            print(
                                " [+] ",
                                f"Details for related {self.kind.lower()} ENS domain: "
                                + self.ens_detail["data"]["domains"][0]["name"],
                            )
                            print(
                                "  ├  Owner address: ",
                                self.ens_detail["data"]["domains"][0]["owner"]["id"],
                            )
                            date = datetime.fromtimestamp(
                                int(
                                    self.ens_detail["data"]["domains"][0][
                                        "registration"
                                    ]["registrationDate"]
                                )
                            )
                            print(
                                "  ├  Registration: ",
                                date.strftime("%Y-%m-%d %H:%M:%S"),
                            )
                            date = datetime.fromtimestamp(
                                int(
                                    self.ens_detail["data"]["domains"][0][
                                        "registration"
                                    ]["expiryDate"]
                                )
                            )
                            print("  ├  Expiry: ", date.strftime("%Y-%m-%d %H:%M:%S"))
                            print("  └  ------------------------------------")

                first = True
                for domain in self.ens_detail["data"]["domains"][0]["owner"]["domains"]:
                    if not first:
                        print("  |")
                    else:
                        addr = self.ens_detail["data"]["domains"][0]["owner"]["id"]
                        print("\n [+] ", f"Domains related to the ETH address: {addr}")
                    print("  ├  Address: %s" % (domain["id"]))
                    date = datetime.fromtimestamp(int(domain["createdAt"]))
                    print(
                        "  |  Name: %s, created at: %s"
                        % (domain["name"], date.strftime("%Y-%m-%d %H:%M:%S"))
                    )
                    if domain["resolver"]:
                        print("  |  Resolver: %s" % (domain["resolver"]["address"]))
                    current_ipfs = Ton_retriever.ipf_ens(
                        domain["name"], session=self.session
                    )
                    if current_ipfs != "":
                        print("  |  IPFS root: %s" % current_ipfs)
                    first = False
                print("  └  ------------------------------------")

    def enrich_telegram_asset(self):
        try:
            for currentnft in self.nfts["data"]["nftItemsByOwner"]["items"]:
                currentnft["tg-data"] = None
                if "collection" in currentnft.keys() and currentnft["collection"]:
                    if (
                        currentnft["collection"]["name"].strip()
                        == "Anonymous Telegram Numbers"
                        and self.telegram_pivot
                    ):
                        if self.tgchecker:
                            currentnft[
                                "tg-data"
                            ] = self.tgchecker.check_telegram_number(currentnft["name"])
                    if (
                        currentnft["collection"]["name"].strip() == "Telegram Usernames"
                        and self.telegram_pivot
                    ):
                        if self.tgchecker:
                            nickname_data = self.tgchecker.check_telegram_nickname(
                                currentnft["name"]
                            )
                            if nickname_data:
                                if nickname_data["apidetail"]:
                                    currentnft["tg-data"] = [
                                        currentnft["name"],
                                        nickname_data["apidetail"].id,
                                        nickname_data,
                                    ]
                                else:
                                    currentnft["tg-data"] = [
                                        currentnft["name"],
                                        -1,
                                        None,
                                    ]
                            else:
                                currentnft["tg-data"] = [currentnft["name"], -1, None]
        except Exception as exx:
            if not self.silent:
                print(f"[-] AN ISSUE OCCURRED DURING RETRIEVING TELEGRAM INFO... {exx}")
            exit(1)

    def pivot_ens(self):
        ens_domain = self.target.split(".")[0] + ".eth"
        request_api = "https://api.thegraph.com/subgraphs/name/ensdomains/ens"
        req_body = {
            "query": '{  domains(where: {name: "%s"}) {    name    owner {      id      domains {        id        name        createdAt        parent {          labelName        }        resolver {          texts          address        }      }    }    registration {      registrationDate      expiryDate    }  }}'
            % ens_domain,
            "variables": {},
        }
        try:
            res = self.session.post(request_api, json=req_body).text
            self.ens_detail = json.loads(res)
        except Exception as exx:
            if not self.silent:
                print(f"[-] AN ISSUE OCCURRED DURING RETRIEVING ENS INFO... {exx}")
            exit(1)

    def request_address_nft(self, addr):
        request_api = "https://api.getgems.io/graphql"
        req_body = {
            "query": "\nquery NftItemConnection($ownerAddress: String!, $first: Int!, $after: String) {\n nftItemsByOwner(ownerAddress: $ownerAddress, first: $first, after: $after) {\n cursor\n items {\n id\n name\n address\n index\n kind\n image: content {\n type: __typename\n ... on NftContentImage {\n originalUrl\n thumb: image {\n sized(width: 480, height: 480)\n }\n }\n ... on NftContentLottie {\n preview: image {\n sized(width: 480, height: 480)\n }\n }\n ... on NftContentVideo {\n cover: preview(width: 480, height: 480)\n }\n }\n collection {\n address\n name\n isVerified\n }\n sale {\n ... on NftSaleFixPrice {\n fullPrice\n }\n }\n }\n }\n}",
            "variables": {"first": 100, "ownerAddress": addr},
        }
        try:
            res = self.session.post(request_api, json=req_body).text
            self.nfts = json.loads(res)
            if self.tgchecker:
                self.enrich_telegram_asset()
        except Exception as exx:
            if not self.silent:
                print("[-] AN ISSUE OCCURRED DURING RETRIEVING NFT INFO...")
            exit(1)

    def request_address_info(self, addr):
        c_addr = addr.split(":")[1]
        request_api = (
            "https://api.ton.cat/v2/explorer/getWalletInformation?address=0%3A" + c_addr
        )
        try:
            res = self.session.get(request_api).text
            self.info = json.loads(res)
        except Exception as exx:
            if not self.silent:
                print(" [-] AN ISSUE OCCURRED DURING RETRIEVING ADDRESS INFO...")
            exit(1)

    def request_address_transctions(self, addr):
        c_addr = addr.split(":")[1]
        request_api = f"https://toncenter.com/api/index/getTransactionsByAddress?address=0%3A{c_addr}&limit=20&offset=0&include_msg_body=true"
        try:
            res = self.session.get(request_api).text
            self.transactions = json.loads(res)
        except Exception as exx:
            if not self.silent:
                print(" [-] AN ISSUE OCCURRED DURING RETRIEVING TRANSACTIONS INFO...")
            exit(1)

    def request_info(self):
        count = 0
        request_api = f"https://tonapi.io/v1/nft/searchItems?collection=0%3A{self.type}&include_on_sale=false&limit={self.step}&offset={self.offset}"
        try:
            res = self.session.get(request_api).text
            obj = json.loads(res)
            if "message" in obj.keys():
                if obj["message"] == "rate limit exceeded":
                    print(
                        f" [-] RATE LIMIT EXCEEDED... {self.offset} NUMBERS CHECKED.."
                    )
                    exit(1)

            for element in obj["nft_items"]:
                count += 1
                search_field = ""
                if "name" in element["metadata"].keys():
                    search_field = element["metadata"]["name"].replace(" ", "")

                    if self.kind == "NICKNAME":
                        search_field = "@" + element["metadata"]["name"]

                elif "dns" in element.keys():
                    if element["dns"]:
                        search_field = element["dns"]

                if search_field == self.target:
                    self.nft_name = search_field
                    _owner = element["owner"]["address"]
                    _is_scam = element["owner"]["is_scam"]

                    # handling auction smartcontract
                    if (
                        "sale" in element.keys()
                        and element["owner"]["address"]
                        != element["sale"]["owner"]["address"]
                    ):
                        self.asset_in_sale = True
                        _owner = element["sale"]["owner"]["address"]
                        _is_scam = element["sale"]["owner"]["is_scam"]
                        if "name" in element["sale"]["owner"]:
                            self.owner_name = element["sale"]["owner"]["name"]
                    elif "name" in element["owner"].keys():
                        self.owner_name = element["owner"]["name"]

                    self.address = _owner
                    self.is_scam = _is_scam
                    self.request_address_info(_owner)
                    self.request_address_transctions(_owner)
                    self.request_address_nft(_owner)
                    self.stop_cycle = True
                    break

        except Exception as exx:
            if not self.silent:
                print(
                    f" [-] THERE WAS SOME ISSUE DURING REQUESTING INFO ABOUT TON {self.kind} ..."
                )
            exit(1)
        return count

    def start_searching(self):
        self.offset = 0
        current_finding = self.step
        while not self.stop_cycle and current_finding == self.step:
            current_finding = self.request_info()
            self.offset += current_finding
            time.sleep(gdelay())
        if self.comprehensive:
            if self.kind == "DOMAIN":
                self.pivot_ens()

    @staticmethod
    def telegram_generate_session():
        TelegramHelper.generate_string_session()


def run():
    parser = argparse.ArgumentParser(
        description="Launch me, and you'll receive a TON of privacy..."
    )
    parser.add_argument(
        "--target",
        required=False,
        help=" [?] TON number, nickname or domain to analyze ...",
    )
    parser.add_argument(
        "-l",
        "--login",
        default=False,
        help=" [?] Create session string for Telegram login ...",
        action="store_true",
    )
    """
    if a flag comprehensive is True
    a deep inspection will be done:
    -  domain -> pivoting on ENS domain
    -  nickname -> Telepathy check nickname details
    -  telephone -> TBA? 
    """
    parser.add_argument(
        "-c",
        "--comprehensive",
        required=False,
        default=False,
        help=" [?] Comprehensive research which includes pivoting on ENS domains ...",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--tor",
        required=False,
        default=False,
        help=" [?] Use TOR as SOCK5 proxy ...",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        "--phonepivot",
        required=False,
        default=False,
        help=" [?] Pivot Telegram account ...",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--silent",
        required=False,
        default=False,
        help=" [?] Disable any print, useful if you don't want to print on stdout ...",
        action="store_true",
    )
    parser.add_argument(
        "--picpath",
        required=False,
        help="[?] where to store profile pics ...",
    )
    try:
        print_banner()
        args = parser.parse_args()

        if not args.target and not args.login:
            parser.print_help()
            exit(0)

        if args.login:
            Ton_retriever.telegram_generate_session()
            exit(0)
        else:
            ton_ret = Ton_retriever(
                args.target,
                args.comprehensive,
                args.tor,
                args.silent,
                args.phonepivot,
                args.picpath,
            )
            ton_ret.start_searching()
            if not args.silent:
                ton_ret.print_info()

    except KeyboardInterrupt:
        print("[-] ATOP was killed ...")
        exit(1)


if __name__ == "__main__":
    run()
