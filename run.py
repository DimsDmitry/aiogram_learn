import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN
from app.handlers import router

# экземляры классов бот и диспетчер
bot = Bot(token=TOKEN)
# боты работают через диспетчер, он - роутер, обрабатывающий входящие сообщения (сообщения и тд)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    # отправляет запрос на сервера телеграмм, если ответ есть то бот его обработает
    # если ответа нет - функция будет ожидать ответ


if __name__ == '__main__':
    # данная конструкция позволяет запустить код в том случае если запускаем именно
    # этот файл, а не импортируем его
    logging.basicConfig(level=logging.INFO)
    # логгирование. Таким образом используется только при разработке, на проде выключаем во избежание замедления
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
