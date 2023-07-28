from django.contrib import admin

from .models import (
    Message,
    Command
)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Класс для настройки административного Django интерфейса модели Message.

    Поля класса:
        list_display (tuple): Кортеж с названиями полей модели, которые будут отображаться в списке объектов
                              модели в административном интерфейсе.

    Пример использования:
        После регистрации данного класса с моделью Message в файле административного интерфейса Django,
        администратор сможет просматривать объекты Message, отображая только поля 'id', 'to_whom' и 'date'
        в списке объектов модели.
    """
    list_display = ('id', 'to_whom', 'date')


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'command', )
