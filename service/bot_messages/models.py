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
