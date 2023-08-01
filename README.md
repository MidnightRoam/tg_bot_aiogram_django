## Telegram bot with Django 
### Описание приложения:
<p>Приложение состоит из двух частей: телеграм бота и веб-сервиса на Django.</p>

#### Телеграм бот:
<p>
Телеграм бот работает с двумя API, а именно: <b>OpenWeatherMap</b> и <b>New-York Times API</b></br>
<b>OpenWeatherMap</b> отдает нам актуальные данные по погоде выбранного региона. </br>
<b>New-York Times API</b> отдает нам актуальные новости, в нашем случае - актуальные популярные новости за последнее время.
</p>

##### Примечание к работе команд бота:
Команда <b>/weather</b> [город] корректно возвращает погоду в выбранном городе, только если вводить название города на английском языке. Работает через OpenWeatherMap API.</br>
Команда <b>/news</b> возвращает случайную популярную новость за последнее время. Работает через New-York Times API.

#### Веб-сервис на Django:
<p>
Веб-сервис на Django отвечает за администрирование и сбор аналитических данных бота для администрации.</br>
Присутствует аутентификация и разделение прав и ролей пользователей, 
т.е. для обычных пользователей предоставлена возможность просматривать список команд и последние сообщения бота. 
Однако редактирование команд и просмотр аналитики доступен только пользователям с выданным доступом.
</p>

#### Инструменты разработки:
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Aiogram</li>
    <li>JavaScript</li>
    <li>HTML</li>
    <li>CSS</li>
</ul>


### Начало работы:

#### 1. Клонируйте репозиторий следующей командой:
    git clone https://github.com/MidnightRoam/tg_bot_aiogram_django.git

#### 2. Перейдите в корневую папку проекта и установите все зависимости следующей командой:
    pip install -r requirements.txt

#### 3. После установления всех зависимостей перейдите в папку service и запустите миграции базы данных:
    cd service (для Windows)
    python manage.py migrate

#### 4. Запустите локальный сервер Django:
    python manage.py runserver

#### 5. Запустите файл bot.py, который отвечает за работу бота
    Находясь в директории aiogram_django/service введите в терминал bot.py

#### 6. Вы должны видеть следующие строки в терминале, которые подтверждают, что ошибок нет
    Updates were skipped successfully
    Data base is connected successfully
    Bot is started successfully

#### 7. После всех предыдущих шагов наш бот и веб-сервис успешно запущены, чтобы начать пользоваться ботом перейдите по телеграмм-ссылке: 
    https://t.me/test_assignment_bot


### Тестовый пользователь:
#### Если вы не хотите регистрировать нового пользователя, то можно воспользоваться тестовым:
<ul>
    <li>Username: admin</li>
    <li>Password: admin</li>
</ul>
