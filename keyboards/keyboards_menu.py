from telethon.tl.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRow


async def keyboard_show_main_menu(event):
    """
    Клавиатура главного меню.
    """
    buttons = [
        KeyboardButtonRow([KeyboardButton(text="🤝 Вступить в каналы")]),
        KeyboardButtonRow([KeyboardButton(text="👀 Просмотреть посты")]),
        KeyboardButtonRow([KeyboardButton(text="❤️ Поставить реакции")]),
        KeyboardButtonRow([KeyboardButton(text="📌 Скрыть меню")])
    ]
    markup = ReplyKeyboardMarkup(
        rows=buttons,
        resize=True,  # Автоматически подгоняет размер кнопок под содержимое
        selective=True,  # Показывать только тому, кто вызвал меню
        persistent=True  # Не сохранять клавиатуру после перезапуска
    )
    await event.respond("Выберите, что нужно сделать:", buttons=markup)


# async def keyboard_show_action_menu(event, action_name):
#     """
#     Клавиатура меню действий с кнопками Готово/Назад.
#     """
#     buttons = [
#         KeyboardButtonRow([KeyboardButton(text="✅ Готово")]),
#         KeyboardButtonRow([KeyboardButton(text="🔙 Главное меню")]),
#         KeyboardButtonRow([KeyboardButton(text="📌 Скрыть меню")])
#     ]
#     markup = ReplyKeyboardMarkup(
#         rows=buttons,
#         resize=True,
#         selective=True,
#         persistent=False
#     )
#     await event.respond(f"{action_name}", buttons=markup)
