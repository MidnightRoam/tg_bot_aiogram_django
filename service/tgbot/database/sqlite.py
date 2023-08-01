import os
from typing import Dict

import aiosqlite
from aiosqlite import Cursor


async def db_start() -> None:
    """
    Устанавливает соединение с базой данных и инициализирует глобальные переменные db и cur.

    """
    global db, cur

    service_folder = os.path.dirname(os.path.dirname(os.path.abspath('service/service')))
    db_filename = os.path.join(service_folder, "db.sqlite3")
    if os.path.exists(db_filename):
        db = await aiosqlite.connect(db_filename)
        cur = await db.cursor()
        if db:
            print('Data base is connected successfully')
    else:
        print(f'Database file "{db_filename}" not found.')


async def get_bot_messages_db() -> Cursor:
    """
    Извлекает все сообщения из таблицы bot_messages_message в базе данных.

    :return: Курсор (cursor), содержащий результат запроса.
    """
    global db, cur

    messages = await cur.execute('SELECT * FROM bot_messages_message;')
    return messages


async def save_bot_message_db(message: Dict[str, any]) -> None:
    """
    Сохраняет сообщение бота в базу данных.

    :param message: Словарь с информацией о сообщении, которое нужно сохранить. Словарь должен содержать ключи:
                    'text' (текст сообщения),
                    'date' (дата сообщения),
                    'message_id' (идентификатор сообщения),
                    'chat' (словарь с информацией о чате, в котором было отправлено сообщение).
    :type message: dict

    :return: None
    """
    global db, cur

    message_text = message['text']
    message_date = message['date']
    message_id = message['message_id']
    message_username = message['chat']['username']

    await cur.execute('INSERT INTO bot_messages_message (text, date, message_id, to_whom) VALUES(?, ?, ?, ?)',
                      (message_text, message_date, message_id, message_username)
                      )

    await db.commit()


async def save_chatroom_message_db(message: Dict[str, any]) -> None:
    """
    Сохраняет айди чат комнаты, куда было отправлено сообщение бота.

    :param message: Словарь с информацией о сообщении, которое нужно сохранить. Словарь должен содержать ключи:
                    'chat_id' (айди чат комнаты, куда было отправлено сообщение бота).
    :type message: dict

    :return: None
    """
    global db, cur

    chat_id = message['chat']['id']

    await cur.execute('INSERT OR IGNORE INTO bot_messages_chatroom (chat_id) VALUES(?)', (chat_id,))
    await db.commit()
