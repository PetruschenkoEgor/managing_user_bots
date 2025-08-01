import asyncio
import os

from colorama import Fore
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import Message

from config.config import API_ID, API_HASH, PHONE_NUMBERS


async def get_messages(session_str: str, channel: str, limit: int = 5) -> list[Message]:
    """
    Получаем последние сообщения с чата.
    """
    try:
        async with TelegramClient(StringSession(session_str), API_ID, API_HASH) as client:
            return await client.get_messages(entity=channel, limit=limit)
    except Exception as e:
        print(Fore.RED + f"Ошибка при получении постов: {str(e)}")
        return []
