from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import markups.markups
from config import dp, bot
from parser import parser


async def hello(message: types.Message):
    await bot.send_message(
        message.chat.id,
        f'Hello : {message.from_user.full_name}',
        reply_markup=markups.markups.keyboard_start
    )


async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()

    button_call_1 = InlineKeyboardButton(
        "Следующая задача",
        callback_data='next_task1'
    )

    markup.add(button_call_1)
    question = 'Из какого мультфильма эта девочка?'
    answers = ['Лоракс', 'Вверх', 'Гадкий Я', 'Минионы']
    photo = open('media/girl.jpg', 'rb')

    await bot.send_photo(message.chat.id, photo=photo)

    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        correct_option_id=2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup,
        open_period=30,
        explanation='Попробуй еще раз!',
    )
#
# async def parser_manas_film(message: types.Message):
#     # data = tv_show.parser()
#     # for i in data:
#     #     await bot.send_message(message.chat.id, i)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(games_1, commands=['games'])
    dp.register_message_handler(parser.movie_parser, commands=['parser'])
