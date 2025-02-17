from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()  # выполняет ту же функцию что и диспетчер но его объект можно сздавать много раз
# и его объект упрощает работу, если у вас много хендлеров и они раскиданы по паткам


# метод message который говорит что диспетчер ждёт именно сообщения (команду старт)
@router.message(CommandStart())  # также называется хендлер - обработчик вх. сообщений с фильтром CommandStart
async def cmd_start(message: Message):
    """асинхронная ф-я которая принимает объект сообщение, внутри неё мы обращаемся
    к методу answer который отвечает пользователю"""
    await message.answer(
        f'Привет! Твой ID:{message.from_user.id}\nИмя: {message.from_user.first_name}',
        reply_markup=await kb.inline_cars()
    )
    # добавляем набор клавиш при запуске команды старт
    # к одному сообщению можно прикрепить лишь одну клавиатуру


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
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
