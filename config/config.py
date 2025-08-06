import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PHONE_NUMBERS = os.getenv("NUMBERS").split(",")
CHANNELS = os.getenv("CHANNELS").split(",")

bot = TelegramClient('bot', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN)
