import asyncio

from colorama import Fore

from actions.get_view import get_views
from actions.joining_channels import join_channels
from actions.send_reaction import send_reaction
from config.config import PHONE_NUMBERS
from session.check_session import check_create_session
from session.create_session import create_session


async def choice_join(channels: list[str], bots_limit: int = None) -> None:
    """
    При выборе вступления в каналы, запускается проверка на создание сессии телеграм для номера,
    и вступление в переданные каналы, и просмотр последних 5 постов в этих каналах.
    """
    if bots_limit is None or bots_limit > len(PHONE_NUMBERS):
        phones = PHONE_NUMBERS[:]
    else:
        phones = PHONE_NUMBERS[:bots_limit]
    for number in phones:
        try:
            print(f"\nОбработка номера: {number}")
            session_str = await check_create_session(number)
            print(f"Проверка {number} : {session_str}")
            if not session_str:
                print(Fore.YELLOW + f"\nСоздаём сессию для {number}...")
                session_str = await create_session(number)

            if session_str:
                await join_channels(session_str, channels)
            else:
                print(Fore.RED + f"Не удалось создать сессию для {number}")
        except Exception as e:
            print(Fore.RED + f"Ошибка для номера {number}: {str(e)}")
            continue


async def choice_view(channels: list[str], posts_limit: int = 1, bots_limit: int = None) -> None:
    """При выборе просмотра постов, запускается проверка на создание сессии телеграм для номера
    и просмотр последних N постов в этих каналах."""
    if bots_limit is None or bots_limit > len(PHONE_NUMBERS):
        phones = PHONE_NUMBERS[:]
    else:
        phones = PHONE_NUMBERS[:bots_limit]
    for number in phones:
        try:
            session_str = await check_create_session(number)
            if not session_str:
                session_str = await create_session(number)
            for channel in channels:
                try:
                    await get_views(session_str, channel, posts_limit)
                except ValueError:
                    print(Fore.RED + f"Канал {channel} не найден или недоступен")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при просмотре поста: {str(e)}")
        except Exception as e:
            print(Fore.RED + f"Ошибка для номера {number}: {str(e)}")
            continue


async def choice_reaction(channels: list[str], posts_limit: int = 1, bots_limit: int = None) -> None:
    """При выборе отправки реакции, запускается проверка на создание сессии телеграм для номера
    и отправка реакции на N постов в указанных каналах."""
    if bots_limit is None or bots_limit > len(PHONE_NUMBERS):
        phones = PHONE_NUMBERS[:]
    else:
        phones = PHONE_NUMBERS[:bots_limit]
    for number in phones:
        try:
            session_str = await check_create_session(number)
            if not session_str:
                session_str = await create_session(number)
            for channel in channels:
                try:
                    await send_reaction(session_str, channel, posts_limit)
                except ValueError:
                    print(Fore.RED + f"Канал {channel} не найден или недоступен")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при отправке реакции: {str(e)}")
        except Exception as e:
            print(Fore.RED + f"Ошибка для номера {number}: {str(e)}")
            continue
