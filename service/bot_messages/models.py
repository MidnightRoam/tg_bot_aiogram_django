from asgiref.sync import sync_to_async
from django.db import models


class Message(models.Model):
    """
    Модель для хранения информации о сообщении.

    Поля модели:
        text (models.TextField): Текст сообщения.
        date (models.CharField): Дата сообщения (строка с максимальной длиной 250 символов).
                                 Может быть пустым (null=True) или содержать пустую строку (blank=True).
        message_id (models.PositiveIntegerField): Идентификатор сообщения (положительное целое число).
                                                  Может быть пустым (null=True) или равным нулю (blank=True).
        to_whom (models.CharField): Telegram юзернейм адресата сообщения (строка с максимальной длиной 250 символов).
                                    Может быть пустым (null=True) или содержать пустую строку (blank=True).
    """
    text = models.TextField()
    date = models.CharField(max_length=250, null=True, blank=True)
    message_id = models.PositiveIntegerField(null=True, blank=True)
    to_whom = models.CharField(max_length=250, null=True, blank=True)
    command = models.ForeignKey('Command', on_delete=models.CASCADE, null=True, blank=True)


class Command(models.Model):
    """
    Модель для хранения информации о команде.

    Поля модели:
        command (models.CharField): Текстовый идентификатор команды (строка с максимальной длиной 124 символов).
        text (models.TextField): Текстовое описание команды.
    """
    command = models.CharField(max_length=124)
    text = models.TextField()

    @classmethod
    @sync_to_async
    def get_command_text(cls, command: str) -> str:
        """
        Асинхронный метод для получения текста команды.

        Параметры:
            command (str): Текстовый идентификатор команды.

        Возвращает:
            str: Текстовое описание команды.

        Пример использования:
            command_text = await Command.get_command_text('/start')
        """
        return cls.objects.get(command=command).text
