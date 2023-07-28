from aiogram import executor

from service.tgbot.config import dp
from service.tgbot.handlers import client
from service.tgbot.database.sqlite import db_start

client.register_handlers_client(dp)


async def on_startup(_):
    await db_start()
    print('Bot is started successfully')

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
