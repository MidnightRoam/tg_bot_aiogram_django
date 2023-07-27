import os

import aiosqlite


async def db_start():
    """
    Устанавливает соединение с базой данных и инициализирует глобальные переменные db и cur.

    """
    global db, cur

    db_filename = "service/db.sqlite3"
    if os.path.exists(db_filename):
        db = await aiosqlite.connect(db_filename)
        cur = await db.cursor()
        if db:
            print('Data base is connected successfully')
    else:
        print(f'Database file "{db_filename}" not found.')


async def get_bot_messages_db():
    """
    Извлекает все сообщения из таблицы bot_messages_message в базе данных.

    :return: Курсор (cursor), содержащий результат запроса.
    """
    global db, cur

    messages = await cur.execute('SELECT * FROM bot_messages_message;')
    return messages


async def save_bot_message_db(message):
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
    await cur.execute('INSERT INTO bot_messages_message (text, date, message_id, to_whom) VALUES(?, ?, ?, ?)',
                      (message['text'], message['date'], message['message_id'], message['chat']['username'])
                      )
    await db.commit()
