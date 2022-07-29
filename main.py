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



async def account_login(bot: Client, m: Message):
    
    link = input("link : ")
    os.system(f"yt-dlp -o "tesst.mp4" '{link}'")
bot.run()
