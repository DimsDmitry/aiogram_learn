# inline инлайн кнопка - ничего не отправляет в чат, выполняет действие при нажатии, отправляет запрос (callback)
# на сервер можно открывать приложение или ссылку

# reply реплай кнопка - при нажатии отправляет содержимое в чат. может запрашивать локацию, контакт и др. данные
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

"""создаём клавиатуру, добавляем в неё кнопки. 1 список - 1 ряд, когда в списке 2 KeyboardButton,
это значит что в одном ряду две кнопки. Настраиваем размер кнопки resize_keyboard, 
приглашение ко вводу input_field_placeholder"""

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube',
                          url='https://timeweb.cloud/tutorials/python/kak-sozdat-virtualnoe-okruzhenie')]
])

'''создавая инлайн клавиатуру, мы не можем оставить просто текст, нужно добавить ещё что-то, например url начиная
с http/https
resize или input_field_placeholder не принимает!'''

# БИЛДЕРЫ:
cars = 'Tesla Mercedes BMW Porsche'.split()


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(
            text=car, url='https://yandex.ru/images/search?from=tabbar&text=cars')
        )  # сделаем из списка клавиатуру
    return keyboard.adjust(2).as_markup()  # отредактировать количество кнопок в ряду
