from telethon import events

from config.config import bot
from keyboards.keyboards_menu import keyboard_show_main_menu


@bot.on(events.NewMessage(pattern="/start"))
async def handler_main_menu(event):
    """
    Обработчик главного меню.
    """
    await keyboard_show_main_menu(event)
