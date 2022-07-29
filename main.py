import requests
from requests.structures import CaseInsensitiveDict
import json
import urllib.parse
import os
import pyrogram
from pyrogram import Client, filters
from pyromod import listen
#from details import api_id, api_hash, bot_token
from pyrogram.types import User, Message
import subprocess
import yt_dlp
import requests
import re
import os.path
import time

bot = Client(
    "ytdl",
    api_id="9077578",
    api_hash='2b1b24357234f68d6e383fffab87b3b7',
    bot_token="5234006821:AAGi2NJC4ZCjm82Q1kco84r-v2blDCXdYRE")


async def account_login(bot: Client, m: Message):
    
    link = input("link : ")
    os.system(f"yt-dlp -o "tesst.mp4" '{link}'")
bot.run()
