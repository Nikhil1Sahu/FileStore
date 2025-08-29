# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
APP_ID = os.environ.get("APP_ID")#Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH")#Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002731391701")) #Your db channel Id
OWNER = os.environ.get("OWNER", "𝑵𝑮_x") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5565120414")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
#force sub channel id, if you want enable force sub 
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/NG_bot_support")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://envs.sh/ttL.png")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/tsH.png")
# (extra pic you provided "https://envs.sh/uxs.jpeg" is unused since only 2 vars exist)
#--------------------------------------------

HELP_TXT = "<b><blockquote>𝑻𝒉𝒊𝒔 𝒊𝒔 𝒂𝒏 𝒇𝒊𝒍𝒆 𝒕𝒐 𝒍𝒊𝒏𝒌 𝒃𝒐𝒕 𝒘𝒐𝒓𝒌 𝒇𝒐𝒓 @network_of_kingdom\n\n❏ 𝑩𝒐𝒕 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔\n├/start : 𝑺𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒃𝒐𝒕\n├/about : 𝑶𝒖𝒓 𝑰𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏\n└/help : 𝑯𝒆𝒍𝒑 𝒓𝒆𝒍𝒂𝒕𝒆𝒅 𝒃𝒐𝒕\n\n 𝑺𝒊𝒎𝒑𝒍𝒚 𝒄𝒍𝒊𝒄𝒌 𝒐𝒏 𝒍𝒊𝒏𝒌 𝒂𝒏𝒅 𝒔𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝒃𝒐𝒕 𝑱𝒐𝒊𝒏 𝒃𝒐𝒕𝒉 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒂𝒏𝒅 𝒕𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒕𝒉𝒂𝒕𝒔 𝒊𝒕.....!\n\n 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒅 𝒃𝒚 <a href=https://t.me/OwnerOfNG>𝑵𝑮_x</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: <a href=https://t.me/OwnerOfNG>𝑵𝑮_x</a>\n◈ 𝑭𝒐𝒖𝒏𝒅𝒆𝒓 𝒐𝒇 : <a href=https://t.me/network_of_kingdom>𝑲𝒊𝒏𝒈𝒅𝒐𝒎 𝑵𝒆𝒕𝒘𝒐𝒓𝒌</a>\n◈ 𝑨𝒏𝒊𝒎𝒆 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href=https://t.me/Anime_Of_Kingdom>𝑨𝑵𝑰𝑴𝑬 𝑲𝑰𝑵𝑮𝑫𝑶𝑴</a>\n◈ 𝑺𝒆𝒓𝒊𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href=https://t.me/Pornhwa_KN>𝑾𝒆𝒃𝒔𝒆𝒓𝒊𝒆𝒔 𝑭𝒍𝒊𝒙</a>\n◈ 𝑨𝒅𝒖𝒍𝒕 𝑴𝒂𝒏𝒉𝒘𝒂 : <a href=https://t.me/Pornhwa_KN>𝑷𝒐𝒓𝒏𝒉𝒘𝒂𝒔</a>\n◈ 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 : <a href=https://t.me/OwnerOfNG>𝑵𝑮_x</a></blockquote></b>"
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>𝑯𝒆𝒍𝒍𝒐 {mention}\n\n<blockquote> 𝑰 𝒂𝒎 𝑭𝒊𝒍𝒆 𝑺𝒕𝒐𝒓𝒆 𝑩𝒐𝒕, 𝑰 𝒄𝒂𝒏 𝒔𝒕𝒐𝒓𝒆 𝒑𝒓𝒊𝒗𝒂𝒕𝒆 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝒔𝒑𝒆𝒄𝒊𝒇𝒊𝒆𝒅 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒂𝒏𝒅 𝒐𝒕𝒉𝒆𝒓 𝒖𝒔𝒆𝒓𝒔 𝒄𝒂𝒏 𝒂𝒄𝒄𝒆𝒔𝒔 𝒊𝒕 𝒇𝒓𝒐𝒎 𝒔𝒑𝒆𝒄𝒊𝒂𝒍 𝒍𝒊𝒏𝒌.</blockquote></b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝑯𝒆𝒍𝒍𝒐 {mention}\n\n<b><blockquote>𝑱𝒐𝒊𝒏 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒂𝒏𝒅 𝒕𝒉𝒆𝒏 𝒄𝒍𝒊𝒄𝒌 𝒐𝒏 𝑹𝒆𝒍𝒐𝒂𝒅 𝒃𝒖𝒕𝒕𝒐𝒏 𝒕𝒐 𝒈𝒆𝒕 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕𝒆𝒅 𝒇𝒊𝒍𝒆.</b></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /delreq :</b> Rᴇᴍᴏᴠᴇᴅ ʟᴇғᴛᴏᴠᴇʀ ɴᴏɴ-ʀᴇǫᴜᴇsᴛ ᴜsᴇʀs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @network_of_kingdom</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
#--------------------------------------------
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝑵𝒐 𝑾𝒂𝒚! 𝑴𝒚 𝑺𝒆𝒏𝒑𝒂𝒊 𝑾𝒐𝒖𝒍𝒅𝒏’𝒕 𝑩𝒆 𝑺𝒐 𝑷𝒂𝒕𝒉𝒆𝒕𝒊𝒄!!"
#--------------------------------------------

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
