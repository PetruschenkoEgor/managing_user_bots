from colorama import Fore
from telethon import TelegramClient
from telethon.sessions import StringSession

from actions.get_messages import get_messages
from config.config import API_HASH, API_ID


async def get_views(session_str: str, channel: str, message_limit: int = 5) -> None:
    """
    Отмечает посты как просмотренные.
    """
    async with TelegramClient(StringSession(session_str), API_ID, API_HASH) as client:
        try:
            messages = await get_messages(session_str, channel, limit=message_limit)

            for msg in messages:
                entity = await client.get_entity(channel)
                await client.send_read_acknowledge(entity, msg)
                print(Fore.GREEN + f"Просмотрено: {msg.id}")

        except Exception as e:
            print(Fore.RED + f"Ошибка: {str(e)}")
