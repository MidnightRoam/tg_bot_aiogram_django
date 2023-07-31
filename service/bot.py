import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'service.settings')
django.setup()

from aiogram import executor

from tgbot.config import dp
from tgbot.handlers import client
from tgbot.database.sqlite import db_start

client.register_handlers_client(dp)


async def on_startup(_) -> None:
    """
    Асинхронная функция, которая выполняется при запуске бота.

    Параметры:
        _: Игнорируемый параметр. Может быть использован для передачи контекста,
           но в данной функции не используется.

    Возвращаемое значение:
        None

    Действия:
        Выполняет инициализацию базы данных (db_start).
        Выводит сообщение "Bot is started successfully" в консоль.

    Примечание:
        Эта функция предполагает использование в качестве обработчика события on_startup
        при запуске Telegram-бота.
    """
    await db_start()
    print('Bot is started successfully')

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
