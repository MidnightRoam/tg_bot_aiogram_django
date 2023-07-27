from aiogram import Bot, Dispatcher


TOKEN_API = '6674912433:AAHNIjBbXoEf-b8vZQqDesIRnPguN_lFV4s'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# OpenWeatherMap для получения погоды
OPEN_WEATHERMAP_TOKEN = 'dae49390d96f20b320623219b22cc7a9'

# New-York Times API для получения новостных статей
NY_TIMES_API_TOKEN = 'Jv20pr7DhGW1TvF0DSDH3WI6ubUAkG4k'
