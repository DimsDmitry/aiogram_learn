import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

# экземляры классов бот и диспетчер
bot = Bot(token=TOKEN)
# боты работают через диспетчер, он - роутер, обрабатывающий входящие сообщения (сообщения и тд)
dp = Dispatcher()


# метод message который говорит что диспетчер ждёт именно сообщения (команду старт)
@dp.message(CommandStart())  # также называется хендлер - обработчик вх. сообщений с фильтром CommandStart
async def cmd_start(message: Message):
    """асинхронная ф-я которая принимает объект сообщение, внутри неё мы обращаемся
    к методу answer который отвечает пользователю"""
    await message.answer(f'Привет! Твой ID:{message.from_user.id}\nИмя: {message.from_user.first_name}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК!')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://sh6-zaterechnyj-r07.gosweb.gosuslugi.ru/netcat_files/70/1182/photo_output_3_8.jpg',
        caption='Это лого ТГ'
    )



async def main():
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
