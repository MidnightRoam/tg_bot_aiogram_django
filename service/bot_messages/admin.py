from django.contrib import admin

from .models import (
    Message,
    Command,
    CommandLog,
    Chatroom
)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Класс для настройки административного Django интерфейса модели Message.

    Атрибуты:
        - list_display (tuple): Кортеж с полями, которые будут отображаться в списке записей.

    Пример использования:
        После регистрации данного класса с моделью Message в файле административного интерфейса Django,
        администратор сможет просматривать объекты Message, отображая только поля 'id', 'to_whom' и 'date'
        в списке объектов модели.
    """
    list_display = ('id', 'to_whom', 'date', )


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    """
    Класс для настройки административного Django интерфейса модели Command.

    Атрибуты:
        - list_display (tuple): Кортеж с полями, которые будут отображаться в списке записей.

    """
    list_display = ('id', 'command', )


@admin.register(CommandLog)
class CommandLogAdmin(admin.ModelAdmin):
    """
    Класс для настройки административного Django интерфейса модели CommandLog.

    Атрибуты:
        - list_display (tuple): Кортеж с полями, которые будут отображаться в списке записей.

    """
    list_display = ('id', 'command', 'calls_count', )


@admin.register(Chatroom)
class ChatroomAdmin(admin.ModelAdmin):
    """
    Класс для настройки административного Django интерфейса модели Chatroom.

    Атрибуты:
        - list_display (tuple): Кортеж с полями, которые будут отображаться в списке записей.

    """
    list_display = ('id', 'chat_id', )
