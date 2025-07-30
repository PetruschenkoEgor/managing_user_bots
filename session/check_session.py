import json
from colorama import Fore
from telethon import TelegramClient
from telethon.sessions import StringSession

from config.config import API_ID, API_HASH


async def check_create_session(number: str) -> str | None:
    """
    Проверка существования сессии.
    """
    client = None
    try:
        with open('sessions.json', 'r') as f:
            sessions = json.load(f)
            session_str = sessions.get(number)
            if not session_str:
                return None

            client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
            await client.connect()
            if await client.is_user_authorized():
                print(Fore.GREEN + f"Найдена валидная сессия для {number}")
                return session_str
            return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    finally:
        if client:
            await client.disconnect()
