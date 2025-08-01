import asyncio
import os

from colorama import Fore

from actions.get_view import get_views
from actions.send_reaction import send_reaction
from config.config import PHONE_NUMBERS, CHANNELS
from session.check_session import check_create_session
from session.create_session import create_session
from actions.joining_channels import join_channels


async def main():
    print(Fore.BLUE + "Telegram UserBot Manager")
    print("1. Вступить в каналы")
    print("2. Просмотреть 5 последних постов")
    print("3. Поставить реакции на последние 5 постов")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        for number in PHONE_NUMBERS:
            try:
                print(f"\nОбработка номера: {number}")
                session_str = await check_create_session(number)
                print(f"Проверка {number} : {session_str}")
                if not session_str:
                    print(Fore.YELLOW + f"\nСоздаём сессию для {number}...")
                    session_str = await create_session(number)

                if session_str:
                    await join_channels(session_str, CHANNELS)
                else:
                    print(Fore.RED + f"Не удалось создать сессию для {number}")
            except Exception as e:
                print(Fore.RED + f"Ошибка для номера {number}: {str(e)}")
                continue

    elif choice == "2":
        for number in PHONE_NUMBERS:
            session_str = await check_create_session(number)
            if not session_str:
                session_str = await create_session(number)
            for channel in CHANNELS:
                await get_views(session_str, channel)

    elif choice == "3":
        for number in PHONE_NUMBERS:
            session_str = await check_create_session(number)
            if not session_str:
                session_str = await create_session(number)
            for channel in CHANNELS:
                await send_reaction(session_str, channel)

    elif choice == "4":
        return
    else:
        print(Fore.RED + "Неверный выбор!")


if __name__ == "__main__":
    asyncio.run(main())
