from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = '5450083383:AAE0uHMDPdB__eGVwnBhGUOoqdeyzARYJRk'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
