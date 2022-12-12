import requests
import json
from config import bot
from aiogram import types


async def movie_parser(message: types.Message):
    response = requests.get('https://cinematica.kg/api/v1/movies/today')
    data = json.JSONDecoder().decode(response.text)

    api_url = 'https://cinematica.kg'
    for movie in data['list']:
        if movie["file_poster_vertical"][-3:] != "jpg":
            await bot.send_message(
                message.chat.id,
                api_url + movie["file_poster_vertical"]
            )

        else:
            await bot.send_photo(
                message.chat.id,
                api_url + movie["file_poster_vertical"]
            )

        await bot.send_message(
            message.chat.id,
            f'{movie["name"]}; {movie["age_restriction"]}'
        )
