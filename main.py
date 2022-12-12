from aiogram import executor
from config import dp
from handlers import extra, client
from handlers import fsmadmin

fsmadmin.register_handler_fsmadmin(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)