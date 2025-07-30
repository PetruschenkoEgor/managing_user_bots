import os

from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
NUMBERS = os.getenv("NUMBERS").split(",")
CHANNELS = os.getenv("CHANNELS").split(",")
