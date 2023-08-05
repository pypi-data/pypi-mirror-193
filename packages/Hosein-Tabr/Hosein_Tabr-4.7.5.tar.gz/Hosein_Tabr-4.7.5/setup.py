import os
import re
from setuptools import setup,find_packages

with open("README.md","r")as fh:
	long_description = fh.read()

requires = ["pycryptodome==3.16.0","aiohttp==3.8.3","asyncio==3.4.3","tinytag==1.8.1","Pillow==9.4.0"]
_long_description = """

<p align="center">
    <br>
    <b>library Hosein-Tabr</b> 
    <br>
</p>

### Our channel in messengers

``` bash

Our channel in Ita

https://eitaa.com/Hosein_Tabr
 

Our channel in Rubika


https://rubika.ir/accant_app


### How to import the Rubik's library

``` bash
from Hosein-Tabr import Robot

``` bash

### How to import the Robino class

``` bash
from Hosein-Tabr import Robino
```


### How to install the library

``` bash
pip install ArseinRubika==3.0.0
```

### My ID in Telegram

``` bash
@hazrat_dark_web
```

## An example:
``` python
from Hosein_Tabr import Robot

bot = Messenger("Enter Auth Account")

bot.sendMessage("1234")
```

## And Or:
``` python
from Hosein_Tabr import Robino

bot = Robot_Rubika("Enter Auth Account")

bot.sendMessage("1234")
```

"""

setup(
    name = "Hosein_Tabr",
    version = "4.7.5",
    authors = "hosein",
    author_email = "09014719950qwer@gmail.com",
    description = (" Robot smart"),
    readme = "README.md",
    url = "https://github.com/pypa/sampleproject",
    requires_python = "1.48.0",
    keywords = ["Hosein","Hosein_tabr","Hosein-tabr","hosein_tabr","bot","Bot","BOT","Robot","ROBOT","robot","rubika","Rubika","Python"],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
    ],
)
