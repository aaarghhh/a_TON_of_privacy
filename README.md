# A TON of privacy v0.2.02
## ATOP - A tool for investigating TON network and its NFT.

"A TON of Privacy" formally called ATOP ... is a tool for conducting OSINT investigations on TON (Telegram 🙃) NFTs.  
  
The TON network is increasingly integrated with the Telegram ecosystem, via NFT. Telegram allows people to purchase numbers, domains and nicknames through cryptocurrency.  
  
ATOP aims to give visibility into the addresses and details of the holders of these assets. Using this tool you will be able to retrieve:
- Address of the owner
- Scam status
- Balance
- Other related NFT
  
ATOP supports:
- TON DNS
- TON NICKNAME
- TON PHONE NUMBERS (+888)

## INSTALLATION
### 1. Git clone the repository.
```
$ git clone https://github.com/aaarghhh/a_TON_of_privacy.git
$ cd a_TON_of_privacy
```
Install dependencies using pip and the file requirements.
```
$ pip install -r requirements.txt
```
### 2. Via pipx
```
$ pipx install atop
```
## USAGE 


If atop was installed as a **global package** (pipx): 
```
$ a-ton-of-privacy --target "+888 12345678"
```
If atop was installed cloning the repository, from the root directory of the repository:
```
cd src/
# python -m atop.atop --target @whatiamlookingfor
```
It retrieves information about a:
- Telephone numbers
```
$ python3 /src/atop/atop.py --target "+888 12345678"
```
- Nickname 
```
$ python3 /src/atop/atop.py --target @telegram_nickname
```
- Domain 
```
$ python3 /src/atop/atop.py --target atop.ton
```
The OUTPUT will contain information about the owner of the asset.
```
Welcome in the realm of.....

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
v 0.1.8

 [!] START CRAWLING.... NUMBER: +888XXXXXXXXXXXX

 [+]  Details for number: +8880XXXXXXXXXXXXXXXXX
  ├  Owner address:  0:c8351922XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  ├  Is scam:  False
  ├  Last activity:  2023-XXXXXXXXXXXXx
  ├  Balance:  0.9XXXXXXXXXX
  └  ------------------------------------

 [+]  NFTs found: 2
  ├  Address: EQCJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  |  Name: +888 XXXXXX, Kind: CollectionItem
  |  Collection: Anonymous Telegram Numbers
  |  Url: https://nft.fragment.com/number/XXXXX.webp
  |
  ├  Address: EQCnIG-ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  |  Name: +888 XXXXXXX, Kind: CollectionItem
  |  Collection: Anonymous Telegram Numbers
  |  Url: https://nft.fragment.com/number/XXXXXX.webp
  └  ------------------------------------

Process finished with exit code 0
```
## FLAGS 
- The flag `-c` supports pivots and in depth analysis, ATM it helps to correlate TON domains to ENS domains, simply pivoting on the second-level domain.
```
[+]  Details for domain ENS domain: xxxxxx.eth
  ├  Owner address:  0xd8xxxxxxxxxxxxxxxxxxxxxxx
  ├  Registration:  2020-xxxxxxxxxxxxxxxx
  ├  Expiry:  2034-xxxxxxxxxxxxxxxxxxxxxx
  └  ------------------------------------
```
- The flag `-t` enable a TOR SOCK5 proxy for each connection.

- The flag `-s` is silent so it doesn't print any result on stdout. 

- The flag `-p` will enable the pivot from TON NFT to TELEGRAM account, this is a new feature that requires a fine tune in order to avoid bad OPSEC mistake. **PLEASE READ THE NEXT CHAPTER CAREFULLY**

- The flag `-l` it's a flag that let to create a session string. The session string is a string that could be used to authenticate to Telegram avoiding the use of SQLLITE, this string could be used in .env file in order to investigate on +888 TON numbers.

```
 [!] Please enter your API ID: 123232132131
 [!] Please enter your API Hash: 12321312321321321321321
 [!] Please enter your phone number: +112312312312 ( sock puppet account BEWARE!! )
Please enter your phone (or bot token): >? +112312312312 ( sock puppet account BEWARE!! )
Please enter the code you received: >? 12345
Warning: Password input may be echoed.
Please enter your password: xxxxxxxx 
```

- The parameter `--picpath`, if `-p` enabled, can contain a path where Telegram profile pics will be stored. Each file will be renamed as Telegram_id[.]extension.

## TELEGRAM PIVOTING 

For using this new feature you need to be sure that you properly **‼️ setup a clean dedicated sock puppet ‼️**.  
You can follow different guide on how to create them with a disposable number.
The sockpuppet need to be hardened as much is possible.

### UNDER PRIVACY SETTINGS ON YOUR TELEGRAM CLIENT

Use this setting in order to hardening your Telegram account.
```
Phone number -> Nobody
Last Seen / Online -> Nobody 
Profile Pics -> Nobody
Bio -> Nobody
Forwarded Message -> Nobody
Calls -> Nobody
Group & Channel -> Nobody
```

<p align="center">
  <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/968839/271731626-75fdfdde-a997-40c9-8cca-d32f444ad276.png" />
</p>

After the sock puppet creation, You'll need API HASH and API KEY. 
Telegram 'API_ID' and 'API_HASH', which you can get by creating a developers account using this link: https://my.telegram.org/.  
Place these values in a .env file in the directory where you launch or set environment variable for the session, along with the phone number of your Telegram account:

```
API_ID=123456
API_HASH=aaaaaaaavvvvvvbbbbbbbbb1223
PHONE_NUMBER=+11234XXXXXX
SESSION_STRING=aabababababbababab123123...
```
If your Telegram account was properly created and your file .env was installed in the directory where you launch the tool, a new SQLlite containing your Telegram session information will be created. If you'll use SESSION_STRING, the SQLlite file will be ignored and the authentication phase will skipped.

## CREDITS
Special thanks to Bellingcat Group for creating this project [Telegram Phone Number Checker](https://github.com/bellingcat/telegram-phone-number-checker), it helped me to realize that this method could be used on TON network too. 


