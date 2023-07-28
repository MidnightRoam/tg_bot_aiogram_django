from datetime import datetime
from random import randrange

import requests
import asyncio
from aiogram import types, Dispatcher
from asgiref.sync import sync_to_async

from bot_messages.models import Command, CommandLog
from tgbot.config import OPEN_WEATHERMAP_TOKEN, NY_TIMES_API_TOKEN
from tgbot.keyboards.reply_keyboards import get_default_keyboard
from tgbot.database.sqlite import save_bot_message_db


async def cmd_start(message: types.Message):
    """
    Обработчик команды /start.

    Когда команда /start отправляется боту, данный обработчик будет вызван.
    Он отправляет приветственное сообщение пользователю с информацией о функции бота и доступных командах.
    Сообщение от бота сохраняется в базу данных.

    Параметры:
        message (types.Message): Объект сообщения от Telegram.

    Пример использования:
        /start

    Пример ответа:
        Привет! Бот выполняет функцию тестового задания,
        все зарегистрированные команды можно посмотреть через /help
    """
    # Берем текст команды из базы данных
    command_text = await Command.get_command_text('/start')
    answer = await message.answer(
        command_text,
        reply_markup=get_default_keyboard()
    )
    # Сохраняем сообщение бота в базе данных
    await save_bot_message_db(answer)
    # Прибавляем к счетчику вызова функции в логах
    await CommandLog.log_command_call('/start')
    return answer


async def cmd_help(message: types.Message):
    """
    Обработчик команды /help.

    Когда команда /help отправляется боту, данный обработчик будет вызван.
    Он отправляет сообщение с описанием всех поддерживаемых команд бота.
    Сообщение от бота сохраняется в базу данных.

    Параметры:
        message (types.Message): Объект сообщения от Telegram.

    Пример использования:
        /help

    Пример ответа:
        <strong>Поддерживаемые команды</strong>:
        /start - Запуск бота
        /help - Список команд
        /weather [город] - показать текущую погоду в выбранном городе
        /news - получить случайную новость

    Примечание:
        В ответе используется HTML-разметка для выделения заголовка жирным шрифтом.
    """
    # Берем текст команды из базы данных
    command_text = await Command.get_command_text('/help')
    answer = await message.answer(
        command_text,
        parse_mode='HTML',
        reply_markup=get_default_keyboard()
    )
    # Сохраняем сообщение бота в базе данных
    await save_bot_message_db(answer)
    # Прибавляем к счетчику вызова функции в логах
    await CommandLog.log_command_call('/help')
    return answer


async def cmd_weather(message: types.Message):
    """
    Обработчик команды /weather.

    Когда команда /weather отправляется боту с указанием названия города, данный обработчик будет вызван.
    Он отправляет запрос на сервис OpenWeatherMap API для получения информации о текущей погоде в указанном городе.
    Затем обработчик форматирует данные о погоде и отправляет ответ пользователю.
    Сообщение от бота сохраняется в базу данных.

    Параметры:
        message (types.Message): Объект сообщения от Telegram с указанием команды и названия города.

    Пример использования:
        /weather Moscow

    Пример ответа:
        *2023-07-26 12:30*
        Погода в городе: Москва
        Температура: 25C°
        Влажность: 65%
        Давление: 1016 мм.рт.ст
        Ветер: 3.5 м/с
        Восход солнца: 2023-07-26 05:15:30
        Закат солнца: 2023-07-26 19:45:45
        Продолжительность дня: 14:30:15


    Примечание:
        При возникновении ошибки в запросе или неверном названии города, бот отправит сообщение с просьбой
        проверить название города (допускается только английский язык для названия города).
    """
    requested_city = message.text.replace('/weather', '')
    # Прибавляем к счетчику вызова функции в логах
    await CommandLog.log_command_call('/weather')
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={requested_city}&appid={OPEN_WEATHERMAP_TOKEN}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(
            data["sys"]["sunrise"])

        answer = await message.reply(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                     f"Погода в городе: {city}\nТемпература: {cur_weather}C°\n"
                                     f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                     f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
                                     f"Продолжительность дня: {length_of_the_day}\n",
                                     reply_markup=get_default_keyboard()
                                     )
        await save_bot_message_db(answer)
        return answer
    except:
        await message.reply(
            "Проверьте название города. Название города допускается только на английском языке",
            reply_markup=get_default_keyboard()
        )


async def cmd_news(message: types.Message):
    """
    Обработчик команды /news.

    Когда команда /news отправляется боту, данный обработчик будет вызван.
    Он отправляет запрос на API сервиса New York Times для получения списка популярных новостей.
    Затем случайно выбирает одну из новостей и отправляет её пользователю.
    Сообщение от бота сохраняется в базу данных.

    Параметры:
        message (types.Message): Объект сообщения от Telegram с указанием команды.

    Пример использования:
        /news

    Пример ответа:
        <strong>Ваша случайная популярная новость:</strong>
        https://www.nytimes.com/2023/07/23/theater/regional-theater-crisis.html
        A Crisis in America’s Theaters Leaves Prestigious Stages Dark
        As they struggle to recover after the pandemic, regional theaters are staging fewer shows, giving fewer
        performances, laying off staff and, in some cases, closing.

    Примечание:
        Если произойдет ошибка при получении новостей, бот отправит сообщение "Упс, что-то пошло не так."
        В ответе используется HTML-разметка для выделения заголовка жирным шрифтом.
    """
    # Прибавляем к счетчику вызова функции в логах
    await CommandLog.log_command_call('/news')
    try:
        r = requests.get(
            f'https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key={NY_TIMES_API_TOKEN}'
        )
        data = r.json()
        # При помощи randrange извлекаем из конечной выборки случайную новостную статью
        random_news = data['results'][randrange(0, len(data['results']))]

        url = random_news['url']
        title = random_news['title']
        abstract = random_news['abstract']

        answer = await message.reply(f"<strong>Ваша случайная популярная новость:</strong>"
                                     f"{url} \n"
                                     f"<strong>{title}</strong>\n"
                                     f"{abstract}",
                                     parse_mode='HTML')
        await save_bot_message_db(answer)
        return answer
    except:
        await message.reply(
            f"Упс, что-то пошло не так.",
            reply_markup=get_default_keyboard()
        )


def register_handlers_client(dp: Dispatcher):
    """
    Функция для регистрации обработчиков команд клиента (бота) в объекте Dispatcher.

    Параметры:
        dp (Dispatcher): Объект Dispatcher из aiogram, который отвечает за обработку сообщений и команд.

    Пример использования:
        register_handlers_client(dp)
    """
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(cmd_weather, commands=["weather"])
    dp.register_message_handler(cmd_news, commands=["news"])
