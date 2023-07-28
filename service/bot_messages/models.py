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

    def __str__(self):
        return self.command


class CommandLog(models.Model):
    """
    Модель для хранения информации о вызовах команд бота.

    Поля модели:
        command (models.ForeignKey): Внешний ключ для связи с моделью Command.
                                     Определяет команду, которая была вызвана.
        calls_count (models.PositiveIntegerField): Количество вызовов команды.
                                                   Целое положительное число.
                                                   Поле не редактируется пользователем (editable=False).

    Методы:
        log_command_call(command: str): Статический метод класса для логирования вызовов команды бота.
                                        Принимает строку с именем команды (например, '/start').
                                        Если команда существует в модели CommandLog, увеличивает счетчик вызовов на 1.
                                        Если команда отсутствует, создает новую запись и устанавливает счетчик в 1.

    Пример использования:
        CommandLog.log_command_call('/start')
    """
    command = models.ForeignKey('Command', on_delete=models.SET_NULL, null=True)
    calls_count = models.PositiveIntegerField(null=True, blank=True, default=0, editable=False)

    @classmethod
    @sync_to_async
    def log_command_call(cls, command: str):
        try:
            command_obj = Command.objects.get(command=command)
            command_log, created = cls.objects.get_or_create(command=command_obj)
            if created:
                command_log.calls_count = 1
            else:
                command_log.calls_count += 1
            command_log.save()
        except Command.DoesNotExist:
            pass
