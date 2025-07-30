from telethon import TelegramClient
from telethon.sessions import StringSession
from colorama import init, Fore

from telethon.tl.functions.channels import JoinChannelRequest

from config.config import API_ID, API_HASH

init(autoreset=True)  # Инициализация colorama для цветного вывода


async def join_channels(session_str, channels):
    """
    Подключение к юзерботу и вступление в каналы.
    """
    if not session_str:
        print(Fore.RED + "Строка сессии не может быть пустой!")
        return

    if not channels:
        print(Fore.RED + "Не указаны каналы для вступления!")
        return

    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
    await client.connect()

    try:
        me = await client.get_me()
        print(Fore.GREEN + f"\nУспешно подключились к аккаунту: {Fore.CYAN}{me.first_name} ({me.phone})")

        for channel in channels:
            try:
                print(Fore.YELLOW + f"\nПопытка вступить в канал: {channel}")
                entity = await client.get_entity(channel)
                await client(JoinChannelRequest(channel))
                print(Fore.GREEN + f"Успешно вступили в канал: {channel}")
            except ValueError:
                print(Fore.RED + f"Канал {channel} не найден или недоступен")
            except Exception as e:
                print(Fore.RED + f"Ошибка при вступлении в {channel}: {str(e)}")

    except Exception as e:
        print(Fore.RED + f"\nОшибка при подключении к аккаунту: {e}")
    finally:
        await client.disconnect()
        print(Fore.YELLOW + "\nСоединение закрыто")
