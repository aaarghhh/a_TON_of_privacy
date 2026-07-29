

# A TON of privacy v0.2.24
## ATOP - Una herramienta para investigar la red TON y sus NFT.

"A TON of Privacy", formalmente llamado ATOP ... es una herramienta para llevar a cabo investigaciones OSINT sobre NFTs de TON (Telegram 🙃).  
  
La red TON se integra cada vez más con el ecosistema de Telegram a través de NFTs. Telegram permite a las personas comprar números, dominios y apodos mediante criptomonedas.  
  
ATOP tiene como objetivo proporcionar visibilidad sobre las direcciones y detalles de los titulares de estos activos. Al utilizar esta herramienta podrás recuperar:
- Dirección del propietario
- Estado de estafa (scam)
- Saldo
- Otros NFT relacionados
  
ATOP es compatible con:
- TON DNS
- TON NICKNAME
- NÚMEROS DE TELÉFONO TON (+888)

## INSTALACIÓN
### 1. Clonar el repositorio con Git.
```
$ git clone https://github.com/aaarghhh/a_TON_of_privacy.git
$ cd a_TON_of_privacy
```
Instala las dependencias utilizando pip y el archivo requirements.
```
$ pip install -r requirements.txt
```
### 2. A través de pipx
```
$ pipx install atop
```
## USO 


Si atop se instaló como un **paquete global** (pipx): 
```
$ a-ton-of-privacy --target "+888 12345678"
```
Si atop se instaló clonando el repositorio, desde el directorio raíz del mismo:
```
cd src/
# python -m atop.atop --target @whatiamlookingfor
```
Recupera información sobre:
- Números de teléfono
```
$ python3 /src/atop/atop.py --target "+888 12345678"
```
- Apodos (Nicknames)
```
$ python3 /src/atop/atop.py --target @telegram_nickname
```
- Dominios
```
$ python3 /src/atop/atop.py --target atop.ton
```
La SALIDA contendrá información sobre el propietario del activo.
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
v 0.2.25

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
## BANDERAS (FLAGS) 
- La bandera `-c` soporta pivotes y análisis en profundidad; de momento, ayuda a correlacionar dominios TON con dominios ENS, simplemente haciendo un pivot en el dominio de segundo nivel.
```
[+]  Details for domain ENS domain: xxxxxx.eth
  ├  Owner address:  0xd8xxxxxxxxxxxxxxxxxxxxxxx
  ├  Registration:  2020-xxxxxxxxxxxxxxxx
  ├  Expiry:  2034-xxxxxxxxxxxxxxxxxxxxxx
  └  ------------------------------------
```
- La bandera `-t` habilita un proxy SOCK5 de TOR para cada conexión.

- La bandera `-s` es silenciosa, por lo que no imprime ningún resultado en stdout. 

- La bandera `-p` habilitará el pivot desde NFT de TON a la cuenta de TELEGRAM; esta es una nueva función que requiere un ajuste fino para evitar errores graves de OPSEC. **POR FAVOR, LEA EL SIGUIENTE CAPÍTULO CON ATENCIÓN**

- La bandera `-l` permite crear una cadena de sesión (session string). Esta cadena puede usarse para autenticarse en Telegram sin necesidad de SQLLITE, y puede colocarse en el archivo .env para investigar números TON +888.

```
 [!] Please enter your API ID: 123232132131
 [!] Please enter your API Hash: 12321312321321321321321
 [!] Please enter your phone number: +112312312312 ( sock puppet account BEWARE!! )
Please enter your phone (or bot token): >? +112312312312 ( sock puppet account BEWARE!! )
Please enter the code you received: >? 12345
Warning: Password input may be echoed.
Please enter your password: xxxxxxxx 
```

- El parámetro `--picpath`, si se habilita `-p`, puede contener una ruta donde se almacenarán las fotos de perfil de Telegram. Cada archivo se renombrará como Telegram_id[.]extension.

## PIVOT A TELEGRAM 

Para usar esta nueva función debes asegurarte de **‼️ configurar adecuadamente una cuenta ficticia (sock puppet) dedicada y limpia ‼️**.  
Puedes seguir diferentes guías sobre cómo crearlas con un número desechable.
La cuenta ficticia debe endurecerse (harden) lo más posible.

### EN LA CONFIGURACIÓN DE PRIVACIDAD DE TU CLIENTE DE TELEGRAM

Usa esta configuración para endurecer tu cuenta de Telegram.
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

Tras la creación de la cuenta ficticia, necesitarás el API HASH y la API KEY. 
`API_ID` y `API_HASH` de Telegram, los cuales puedes obtener creando una cuenta de desarrollador en este enlace: https://my.telegram.org/.  
Coloca estos valores en un archivo .env en el directorio desde donde ejecutes la herramienta o configura las variables de entorno para la sesión, junto con el número de teléfono de tu cuenta de Telegram:

```
API_ID=123456
API_HASH=aaaaaaaavvvvvvbbbbbbbbb1223
PHONE_NUMBER=+11234XXXXXX
SESSION_STRING=aabababababbababab123123...
```
Si tu cuenta de Telegram se creó correctamente y tu archivo .env se colocó en el directorio donde ejecutas la herramienta, se creará una nueva base de datos SQLlite que contendrá la información de tu sesión de Telegram. Si usas SESSION_STRING, el archivo SQLlite se ignorará y se omitirá la fase de autenticación.

## CRÉDITOS
Agradecimiento especial al grupo Bellingcat por crear este proyecto [Telegram Phone Number Checker](https://github.com/bellingcat/telegram-phone-number-checker), lo cual me ayudó a darme cuenta de que este método también podría utilizarse en la red TON.
