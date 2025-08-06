from telethon import events
from telethon.tl.types import ReplyKeyboardHide

from config.config import bot
from keyboards.keyboards_menu import keyboard_show_action_menu, keyboard_show_main_menu


@bot.on(events.NewMessage)
async def handler_action_menu(event):
    """
    Обработчик меню действий.
    """
    text = event.raw_text

    if text == "🤝 Вступить в каналы":
        await keyboard_show_action_menu(event, "Введите названия каналов через запятую(автоматически просматриваются 5 последних постов):")

    elif text == "👀 Просмотреть посты":
        await keyboard_show_action_menu(event, "Введите название канала:")

    elif text == "❤️ Поставить реакции":
        await keyboard_show_action_menu(event, "Введите название канала:")

    elif text == "✅ Готово":
        await event.respond("Действие выполнено!", buttons=ReplyKeyboardHide())

    elif text == "🔙 Главное меню":
        await keyboard_show_main_menu(event)

    elif text == "📌 Скрыть меню":
        await event.respond("Меню скрыто", buttons=ReplyKeyboardHide())
