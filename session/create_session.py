from colorama import Fore
from telethon import TelegramClient
from telethon.sessions import StringSession

from config.config import API_HASH, API_ID
from session.write_session_str import write_session_str


async def create_session(number: str) -> str | None:
    """
    Создание сессии и запись текущей строки сессии в файл.
    """
    client = None
    print(Fore.YELLOW + "\nСоздание новой сессии...")
    try:
        client = TelegramClient(StringSession(), API_ID, API_HASH)
        await client.connect()

        # Проверяем, не забанен ли номер
        try:
            await client.send_code_request(number)
        except Exception as e:
            if "banned" in str(e).lower():
                print(Fore.RED + f"Номер {number} забанен в Telegram!")
                return None
            raise

        code = input(Fore.CYAN + f"Введите код подтверждения для {number}: ")
        await client.sign_in(number, code)

        # Проверка успешной авторизации
        if not await client.is_user_authorized():
            print(Fore.RED + "Не удалось авторизоваться!")
            return None

        session_str = client.session.save()
        print(Fore.GREEN + "\nСессия успешно создана!")
        print(Fore.CYAN + f"Строка сессии для этого аккаунта: аккаунт: {number}, строка: {session_str}")
        session = {number: session_str}

        # сохраняем сессию в файл session.json
        await write_session_str(session)

        print(Fore.WHITE + session_str)
        return session_str
    except Exception as e:
        print(Fore.RED + f"\nОшибка при создании сессии: {e}")
        return None
    finally:
        if client:
            await client.disconnect()
