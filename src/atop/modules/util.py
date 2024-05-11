import os
import re
import sys
import errno
import math
import binascii
import base64
import requests
import time

from colorama import Fore, Style

ERROR_INVALID_NAME = 123

class Util:
    def __init__(self):
        pass

    @staticmethod
    def is_pathname_valid(pathname: str) -> bool:
        """
        `True` if the passed pathname is a valid pathname for the current OS;
        `False` otherwise.
        """
        try:
            if not isinstance(pathname, str) or not pathname:
                return False

            _, pathname = os.path.splitdrive(pathname)
            root_dirname = (
                os.environ.get("HOMEDRIVE", "C:")
                if sys.platform == "win32"
                else os.path.sep
            )
            assert os.path.isdir(root_dirname)
            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, "winerror"):
                        if exc.winerror == ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True

    @staticmethod
    def get_file_size(self, path):
        return os.path.getsize(path)

    @staticmethod
    def get_file_size_human(self, path):
        size = self.get_file_size(path)
        return self.convert_size(size)

    @staticmethod
    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    @staticmethod
    def convert_ton_address(address):
        return (
            "0:" + (binascii.hexlify(base64.b64decode(address)).decode("utf-8")[4:68])
        )

    @staticmethod
    def retrieve_nft_type(address):
        tt = None
        if not re.match(r"0:[0-9a-f]{64}", address):
            address = Util.convert_ton_address(address)
        if (
            address
            == "0:b774d95eb20543f186c06b371ab88ad704f7e256130caf96189368a7d0cb6ccf"
        ):
            tt = "Ton-dns"
        if (
            address
            == "0:80d78a35f955a14b679faa887ff4cd5bfc0f43b4a4eea2a7e6927f3701b273c2"
        ):
            tt = "Telegram-nick"
        if (
            address
            == "0:0e41dc1dc3c9067ed24248580e12b3359818d83dee0304fabcf80845eafafdb2"
        ):
            tt = "Telegram-number"
        if (
            address
            == "0:e1955aba7249f23e4fd2086654a176516d98b134e0df701302677c037c358b17"
        ):
            tt = "Getgems-nick"
        return tt

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

    @staticmethod
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
    v 0.2.2 """
            + Style.RESET_ALL
        )
