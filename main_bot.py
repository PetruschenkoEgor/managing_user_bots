from config.config import bot


async def main():
    # Импортируем все обработчики
    import handlers.start
    import keyboards.keyboards_menu
    import handlers.callbacks

    print("Бот успешно запущен!")
    await bot.start()
    await bot.run_until_disconnected()

if __name__ == '__main__':
    bot.loop.run_until_complete(main())
