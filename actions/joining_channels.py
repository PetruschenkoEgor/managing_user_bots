import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession
from colorama import init, Fore

from telethon.tl.functions.channels import JoinChannelRequest

from actions.get_view import get_views
from config.config import API_ID, API_HASH

init(autoreset=True)  # Инициализация colorama для цветного вывода


async def join_channels(session_str: str, channels: list[str]) -> None:
    """
    Вступление в каналы + просмотр последних 5 постов.
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
                await client(JoinChannelRequest(entity))
                print(Fore.GREEN + f"Успешно вступили в канал: {channel}")
                await get_views(session_str, channel)
            except ValueError:
                print(Fore.RED + f"Канал {channel} не найден или недоступен")
            except Exception as e:
                print(Fore.RED + f"Ошибка при вступлении в {channel}: {str(e)}")

    except Exception as e:
        print(Fore.RED + f"\nОшибка при подключении к аккаунту: {e}")
    finally:
        await client.disconnect()
        print(Fore.YELLOW + "\nСоединение закрыто")


async def main():
    session_str = "1ApWapzMBuwjAsHnR3IKVuSW1TAB7PwBRxYUre53mGBzIvU5snSxF_WH_57kh9ZCW0GhBVqsxly1zN7QFazgzvnuJcSvnXvuQdX0mi9HEzEToG0gJYaOZxDQw1UXeBumiefCMvvYE4-D5S_ro6CM6BhZVDSDsrOm1RB9JFUXE6xMJ0LNAp86U0CpyDqbhQFhFDtSeg2ZITuLM6uZVCHeaZruxe1DAGSJI6fBnoi42IQQ0Auz3IBJIL4Cu94eyIOdwu0TcGtUzmpQx2EFx33gPRP5t5EYNjL7RAj2FIXE1MHoY68y39qGYCoqHlGZUjxdKMJEsxEeCgSEOnSEzJrvjVUE_d_jKDok="
    await join_channels(session_str, ["t.me/food_healthy_food"])


if __name__ == "__main__":
    asyncio.run(main())