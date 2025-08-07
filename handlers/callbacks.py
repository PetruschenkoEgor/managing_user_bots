from telethon import events

from config.config import bot
from keyboards.keyboards_menu import keyboard_show_main_menu
from utils.choice_action import choice_view, choice_join, choice_reaction
from utils.state import UserState

# Храним состояние пользователя и данные
user_state = UserState()


@bot.on(events.NewMessage)
async def handler_action_menu(event):
    """
    Обработчик меню действий с сохранением состояния.
    """
    user_id = event.sender_id
    text = event.text.strip()
    # Преобразовываем полученные каналы в список
    channel_list = text.split(',')

    # Если пользователь в главном меню
    if text in ["🤝 Вступить в каналы", "👀 Просмотреть посты", "❤️ Поставить реакции", "📌 Скрыть меню"]:
        if text == "🤝 Вступить в каналы":
            user_state.set_state(user_id, "WAITING_CHANNELS_JOIN")
            await event.respond("Введите ссылки или id каналов через запятую в любом виде(t.me/food_healthy_food, https://t.me/food_healthy_food, @food_healthy_food, food_healthy_food, 123456789)")
        elif text == "👀 Просмотреть посты":
            user_state.set_state(user_id, "WAITING_CHANNELS_VIEW")
            await event.respond("Введите ссылки или id каналов через запятую в любом виде(t.me/food_healthy_food, https://t.me/food_healthy_food, @food_healthy_food, food_healthy_food, 123456789)")
        elif text == "❤️ Поставить реакции":
            user_state.set_state(user_id, "WAITING_CHANNELS_REACTION")
            await event.respond("Введите ссылки или id каналов через запятую в любом виде(t.me/food_healthy_food, https://t.me/food_healthy_food, @food_healthy_food, food_healthy_food, 123456789)")
        elif text == "📌 Скрыть меню":
            await event.respond("Меню скрыто. Используйте '/start' для возврата.")

    # Если пользователь в состоянии ввода данных
    elif user_id in user_state.states:
        current_state = user_state.get_state(user_id)

        # Обработка для "Вступить в каналы"
        if current_state == "WAITING_CHANNELS_JOIN":
            user_state.set_data(user_id, "channels_join", channel_list)
            user_state.set_state(user_id, "WAITING_BOTS_LIMIT_JOIN")
            await event.respond("Сколько ботов должно вступить?")
        elif current_state == "WAITING_BOTS_LIMIT_JOIN":
            user_state.set_data(user_id, "bots_limit_join", int(text))
            # Каналы для вступления
            channels = user_state.get_data_value(user_id, "channels_join")
            # Количество ботов для вступления
            bots_limit = user_state.get_data_value(user_id, "bots_limit_join")

            # НУЖНО ПРОРАБОТАТЬ МОМЕНТ, ЕСЛИ БУДУТ ОШИБКИ ПРИ ВСТУПЛЕНИИ
            await event.respond(f"Готово! Ботов вступит: {bots_limit} Каналы: {", ".join(channels)}.")
            # Вступаем в каналы
            await choice_join(channels, bots_limit)
            # Сбрасываем состояние и удаляем данные
            user_state.clear(user_id)

        # Обработка для "Просмотреть посты"
        elif current_state == "WAITING_CHANNELS_VIEW":
            user_state.set_data(user_id, "channels_view", channel_list)
            user_state.set_state(user_id, "WAITING_POSTS_LIMIT_VIEW")
            await event.respond("Сколько постов просмотреть?")
        elif current_state == "WAITING_POSTS_LIMIT_VIEW":
            user_state.set_data(user_id, "posts_limit_view", int(text))
            user_state.set_state(user_id, "WAITING_BOTS_LIMIT_VIEW")
            await event.respond("Сколько ботов должно просмотреть?")
        elif current_state == "WAITING_BOTS_LIMIT_VIEW":
            user_state.set_data(user_id, "bots_limit_view", int(text))
            # Каналы для просмотра
            channels = user_state.get_data_value(user_id, "channels_view")
            # Количество постов для просмотра
            posts = user_state.get_data_value(user_id, "posts_limit_view")
            # Количество ботов для просмотра
            bots_limit = user_state.get_data_value(user_id, "bots_limit_view")
            await event.respond(f"Готово! Постов: {posts}. Ботов просмотрит: {bots_limit}. Каналы: {", ".join(channels)}")
            # Просматриваем посты
            await choice_view(channels, posts, bots_limit)
            user_state.clear(user_id)

        # Обработка для "Поставить реакции"
        elif current_state == "WAITING_CHANNELS_REACTION":
            user_state.set_data(user_id, "channels_reaction", channel_list)
            user_state.set_state(user_id, "WAITING_POSTS_LIMIT_REACTION")
            await event.respond("На сколько постов поставить реакции?")
        elif current_state == "WAITING_POSTS_LIMIT_REACTION":
            user_state.set_data(user_id, "posts_limit_reaction", int(text))
            user_state.set_state(user_id, "WAITING_BOTS_LIMIT_REACTION")
            await event.respond("Сколько ботов должно поставить реакции?")
        elif current_state == "WAITING_BOTS_LIMIT_REACTION":
            user_state.set_data(user_id, "bots_limit_reaction", int(text))
            # Каналы для отправки реакций
            channels = user_state.get_data_value(user_id, "channels_reaction")
            # Количество постов для отправки реакций
            posts = user_state.get_data_value(user_id, "posts_limit_reaction")
            # Количество ботов для отправки реакций
            bots_limit = user_state.get_data_value(user_id, "bots_limit_reaction")
            await event.respond((f"Готово! Постов: {posts}. Ботов поставит: {bots_limit}. Каналы: {", ".join(channels)}"))
            # Отправляем реакции
            await choice_reaction(channels, posts, bots_limit)
            user_state.clear(user_id)
    # Если состояние не распознано
    else:
        await keyboard_show_main_menu(event)
