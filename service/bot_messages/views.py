from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Message


class MessageListView(ListView):
    """
    Класс MessageListView представляет представление списка сообщений в боте.

    Атрибуты:
        template_name (str): Имя шаблона для отображения списка сообщений.
        model (Model): Модель, используемая для получения данных сообщений.

    Методы:
        get_queryset(): Возвращает QuerySet с сообщениями, отсортированными по дате.
        get_context_data(**kwargs): Возвращает контекст данных для отображения списка сообщений.

    """
    template_name = 'bot_messages/messages_list.html'
    model = Message

    def get_queryset(self):
        """
        Возвращает QuerySet с сообщениями, отсортированными по дате.
        """
        username_sort = self.request.GET.get('username')
        group_sort = self.request.GET.get('group')
        if username_sort:
            return Message.objects.filter('to_whom').order_by('-date')
        if group_sort:
            return Message.objects.filter('to_whom').order_by('-date')

        return Message.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        """
        Возвращает контекст данных для отображения списка сообщений.

        Аргументы:
            **kwargs: Дополнительные аргументы для метода get_context_data.

        Возвращает:
            dict: Контекст данных для использования в шаблоне.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Bot analytics"
        context["messages"] = self.get_queryset()
        return context

