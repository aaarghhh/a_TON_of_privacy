import re
import time

from telethon import TelegramClient, errors, events, sync
from telethon.tl.types import InputPhoneContact
from telethon import functions, types
from telethon.errors import FloodWaitError
from getpass import getpass
from bs4 import BeautifulSoup

from telethon.sessions import StringSession
from atop.modules.const import user_agent
from atop.modules.util import Util

import requests
import random
import os

from telethon.tl.types import PeerChat, PeerChannel, Channel, User, Chat


class TelegramHelper:
    _api_hash = ""
    _api_id = ""
    _telephone_sock = ""
    _client = None
    _outdir = ""
    _sessionstring = None

    @staticmethod
    def generate_string_session(path):
        api_id = input(" [!] Please enter your API ID:\n")
        api_hash = input(" [!] Please enter your API Hash:\n")
        phone_number = input(" [!] Please enter your phone number:\n")
        # validate with regex phone number
        _api_id = 0
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number.replace(" ", "")
            if not re.compile(r"^(\+)[0-9]{11,12}$").match(phone_number):
                print(" [-] Phone number is valid.")
                return -1
        if not re.compile(r"^\d+$").match(api_id):
            print(" [-] App id is valid.")
            return -1
        else:
            _api_id = int(api_id)
        with TelegramClient(StringSession(), _api_id, api_hash) as client:
            saved = False
            if path and path != "":
                if Util.is_pathname_valid(path):
                    sessionstring = client.session.save()
                    with open(path, "w+") as f:
                        f.write("API_ID=" + api_id + "\n")
                        f.write("API_HASH=" + api_hash + "\n")
                        f.write("PHONE_NUMBER=" + phone_number + "\n")
                        f.write("SESSION_STRING=" + sessionstring + "\n")
                    print(f" [!] Sessionstring saved to {path}")
                    saved = True
                else:
                    print(" [-] Path is not valid.")
                    return -1
            if not saved:
                print(client.session.save())
            return 0

    @staticmethod
    def parse_html_page(url, session=None):
        data_web = {
            "nickname": "@" + url.replace("https://t.me/", ""),
            "participants": "N/A",
            "image": "N/A",
            "kind": "N/A",
            "description": "N/A",
            "name": "N/A",
        }
        if not session:
            s = requests.Session()
        else:
            s = session
        s.max_redirects = 10
        s.headers["User-Agent"] = random.choice(user_agent)
        URL = s.get(url)
        URL.encoding = "utf-8"
        html_content = URL.text
        soup = BeautifulSoup(html_content, "html.parser")

        try:
            action = soup.find("div", {"class": ["tgme_page_additional"]}).text
            if not "you can view and join" in action:
                data_web["kind"] = "user"
        except:
            pass
        try:
            data_web["name"] = soup.find("div", {"class": ["tgme_page_title"]}).text
        except:
            data_web["name"] = "N/A"
        try:
            data_web["image"] = soup.find("div", {"class": ["tgme_page_photo"]}).find(
                "img"
            )["src"]
        except:
            data_web["description"] = "N/A"
        try:
            data_web["description"] = (
                soup.find("div", {"class": ["tgme_page_description"]})
                .getText(separator="\n")
                .replace("\n", " ")
            )
        except:
            data_web["description"] = "N/A"
        try:
            if data_web["kind"] != "user":
                group_participants = soup.find(
                    "div", {"class": ["tgme_page_extra"]}
                ).text
                if "member" in group_participants:
                    sep = "member"
                    stripped = group_participants.split(sep, 1)[0]
                    data_web["participants"] = stripped.replace(" ", "")
                    data_web["kind"] = "group"
                else:
                    sep = "subscriber"
                    stripped = group_participants.split(sep, 1)[0]
                    data_web["participants"] = stripped.replace(" ", "")
                    data_web["kind"] = "channel"
        except:
            data_web["participants"] = "N/A"
        return data_web

    def __init__(self, api_hash, api_id, telephone_sock, outdir, sessionstring=None):
        if not api_hash or not api_id or (not telephone_sock and not sessionstring):
            print(
                "You have to setup your sockpuppet.. you haven't compiled your .env data.. "
            )
        if not sessionstring:
            self._api_hash = api_hash
            self._api_id = api_id
            self._outdir = outdir
            self._telephone_sock = telephone_sock
        else:
            self._api_hash = api_hash
            self._api_id = api_id
            self._sessionstring = sessionstring
        self.create_client()

    def create_client(self):
        if self._sessionstring:
            self._client = TelegramClient(
                StringSession(self._sessionstring), self._api_id, self._api_hash
            )
            self._client.connect()
            if not self._client.is_user_authorized():
                print(
                    f"[-] TELEGRAM ISN'T AUTHENTICATE PLS RECREATE A SESSIONSTRING..."
                )
                exit(1)
        else:
            self._client = TelegramClient(
                self._telephone_sock, self._api_id, self._api_hash
            )
            self._client.connect()
            if not self._client.is_user_authorized():
                self._client.send_code_request(self._telephone_sock)
                try:
                    self._client.sign_in(
                        self._telephone_sock,
                        input("Enter the code (sent on telegram): "),
                    )
                except errors.SessionPasswordNeededError:
                    pw = getpass(
                        "Two-Step Verification enabled. Please enter your account password: "
                    )
                    self._client.sign_in(password=pw)

    def retrieve_entity(self, _target):
        current_entity = None
        try:
            current_entity = self._client.get_entity(_target)
        except Exception as exx:
            try:
                current_entity = self._client.get_entity(int(_target))
            except:
                pass
            pass
        """if not current_entity:
            try:
                current_entity = self._client.get_entity(PeerChannel(_target))
            except Exception as exx:
                pass
        if not current_entity:
            try:
                current_entity = self._client.get_entity(PeerChat(_target))
            except Exception as exx:
                pass"""
        return current_entity

    @staticmethod
    def create_tg_url(handle):
        return "https://t.me/{}".format(handle.split("@")[1])

    @staticmethod
    def print_entity(entity_data):
        if entity_data[1] > 0:
            if type(entity_data[2]["apidetail"]) == Channel:
                print(
                    "  |  Found Channel id: {}, title: {}, forum: {}, creation date: {}".format(
                        entity_data[2]["apidetail"].id,
                        entity_data[2]["apidetail"].title,
                        str(entity_data[2]["apidetail"].forum),
                        entity_data[2]["apidetail"].date.strftime("%d/%m/%Y, %H:%M:%S"),
                    )
                )
            if type(entity_data[2]["apidetail"]) == Chat:
                print(
                    "  |  Found Group id: {}, title:{}, forum{}, creation date {}".format(
                        entity_data[2]["apidetail"].id,
                        entity_data[2]["apidetail"].title,
                        str(entity_data[2]["apidetail"].forum),
                        entity_data[2]["apidetail"].date.strftime("%m/%d/%Y, %H:%M:%S"),
                    )
                )
            if type(entity_data[2]["apidetail"]) == User:
                print(
                    "  |  Found User id: {}, first name:{}, last name:{}, lang code: {}".format(
                        entity_data[2]["apidetail"].id,
                        entity_data[2]["apidetail"].first_name,
                        entity_data[2]["apidetail"].last_name,
                        entity_data[2]["apidetail"].lang_code,
                    )
                )
            TelegramHelper.print_web(entity_data)
        else:
            print("  |  No Telegram account found..")

    @staticmethod
    def print_web(entity_data):
        if (
            entity_data[2]
            and "apidetail" in entity_data[2].keys()
            and "webdetail" in entity_data[2].keys()
        ):
            if type(entity_data[2]["apidetail"]) == Channel:
                print(
                    "  |  Name: {}, Description: {}, Subscribers: {}".format(
                        entity_data[2]["webdetail"]["name"],
                        entity_data[2]["webdetail"]["description"],
                        entity_data[2]["webdetail"]["participants"],
                    )
                )
                print(
                    "  |  Profilepic: {}".format(entity_data[2]["webdetail"]["image"])
                )
            if type(entity_data[2]["apidetail"]) == Chat:
                print(
                    "  |  Name: {}, Description: {}, Members: {}".format(
                        entity_data[2]["webdetail"]["name"],
                        entity_data[2]["webdetail"]["description"],
                        entity_data[2]["webdetail"]["participants"],
                    )
                )
                print(
                    "  |  Profilepic: {}".format(entity_data[2]["webdetail"]["image"])
                )
            if type(entity_data[2]["apidetail"]) == User:
                print(
                    "  |  Name: {}, Description: {}".format(
                        entity_data[2]["webdetail"]["name"],
                        entity_data[2]["webdetail"]["description"],
                    )
                )
                print(
                    "  |  Profilepic: {}".format(entity_data[2]["webdetail"]["image"])
                )

    def check_telegram_nickname(self, _telegra_to_check):
        ent = None
        web = None
        try:
            ent = self.retrieve_entity(_telegra_to_check)
        except:
            pass
        if ent:
            try:
                web = TelegramHelper.parse_html_page(
                    TelegramHelper.create_tg_url(_telegra_to_check)
                )
            except:
                pass
        return {"apidetail": ent, "webdetail": web}

    def check_telegram_number(self, _number_to_check):
        try:
            contact = InputPhoneContact(
                client_id=0, phone=_number_to_check, first_name="", last_name=""
            )
            try:
                contacts = self._client(
                    functions.contacts.ImportContactsRequest([contact])
                )
            except FloodWaitError as e:
                time.sleep(e.seconds + 0.2)
                print("[!] Too many requests Waiting {}".format(e.seconds + 1))
                contacts = self._client(
                    functions.contacts.ImportContactsRequest([contact])
                )
            if len(contacts.to_dict()["users"]) > 0:
                username = contacts.to_dict()["users"][0]["username"]
                id = contacts.to_dict()["users"][0]["id"]
                telegram_details = None
                if id:
                    if self._outdir and self._outdir != "":
                        filename = self._client.download_profile_photo(
                            id, download_big=True
                        )
                        if filename:
                            os.rename(
                                os.path.join(self._outdir, str(filename)),
                                str(id) + ".jpg",
                            )

                    ###tru retrieving user details in contcat list
                    if not username:
                        username = "N/A"
                    if username != "N/A":
                        telegram_details = self.check_telegram_nickname("@" + username)
                    try:
                        try:
                            self._client(
                                functions.contacts.DeleteContactsRequest(id=[id])
                            )
                        except FloodWaitError as e:
                            time.sleep(e.seconds + 0.2)
                            self._client(
                                functions.contacts.DeleteContactsRequest(id=[id])
                            )
                    except Exception as exx:
                        return None, -2, None
                    return username, id, telegram_details
                else:
                    return None, -1, None
            else:
                return None, -1, None

        except IndexError as e:
            print(
                "  |  Error happened during retrieving information about this %s Ton Number "
                % (_number_to_check)
            )

        except TypeError as e:
            print(
                f"  |  TypeError: {e}. --> The error might have occurred due to the inability to delete the {_number_to_check} from the contact list."
            )
        except:
            raise
