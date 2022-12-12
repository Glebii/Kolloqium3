from aiogram import types, Dispatcher
from config import bot


async def secret_word(message: types.Message):
    await message.reply('Hi!')

async def secret_word2(message: types.Message):
    await message.reply('I am GLEB')

async def secret_word3(message: types.Message):
    await message.reply('fine')


async def echo_and_ban(message: types.Message):
    ban_words = ['fuck', 'nigga', 'bitch']
    for i in ban_words:
        if i in message.text.lower().replace(" ", " "):
            await message.delete()
            await bot.send_message(message.chat.id, "You've been banned!")
            # await message.reply('This is bad word')
            # await bot.delete_message(message.chat.id, message.message_id)
        if message.text.lower() == 'dice':
            await bot.send_dice(message.chat.id, emoji='')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: 'Hey, bot' in word.text)
    dp.register_message_handler(secret_word2, lambda word: 'What is your name?' in word.text)
    dp.register_message_handler(secret_word3, lambda word: 'How are you?' in word.text)
    dp.register_message_handler(echo_and_ban, content_types=['text'])
    