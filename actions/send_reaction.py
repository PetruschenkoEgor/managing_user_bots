import asyncio
import random

from colorama import Fore
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl import types
from telethon.tl.functions.messages import SendReactionRequest

from actions.get_messages import get_messages
from config.config import API_HASH, API_ID


async def send_reaction(session_str: str, channel: str, messages_limit: int = 5) -> None:
    """
    Отправка рандомной реакции на пост(в том числе пустая реакция - некоторые боты пропускают реакцию).
    """
    async with TelegramClient(StringSession(session_str), API_ID, API_HASH) as client:
        messages = await get_messages(session_str, channel, limit=messages_limit)

        reactions = [
            None,  # Нет реакции
            types.ReactionEmoji(emoticon="👍"),
            types.ReactionEmoji(emoticon="❤️"),
            types.ReactionEmoji(emoticon="🔥"),
            types.ReactionEmoji(emoticon="🥰"),
            types.ReactionEmoji(emoticon="😍"),
            types.ReactionEmoji(emoticon="👀"),
            types.ReactionEmoji(emoticon="✍️"),
            types.ReactionEmoji(emoticon="🦄"),
        ]

        for msg in messages:
            try:
                reaction = random.choice(reactions)
                await client(
                    SendReactionRequest(peer=channel, msg_id=msg.id, reaction=[reaction] if reaction else None)
                )
                print(f"Реакция {'пустая' if not reaction else reaction.emoticon} отправлена на пост {msg.id}")
                await asyncio.sleep(1)
            except Exception as e:
                print(Fore.RED + f"Ошибка при отправке реакции на пост {msg.id}: {str(e)}")
