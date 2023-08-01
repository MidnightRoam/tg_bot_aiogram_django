from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Message, CommandLog, Command
from .forms import CommandForm


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
    template_name = 'bot_messages/message_list.html'
    model = Message
    context_object_name = 'messages'

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
        context["popular_commands"] = CommandLog.objects.select_related('command').order_by("-calls_count")
        return context


class JsonMessageView(View):
    """
    Класс JsonMessageView представляет представление, возвращающее данные сообщений в формате JSON.

    Методы:
        get(self, request, *args, **kwargs):
            Обрабатывает GET-запрос и возвращает список всех сообщений в формате JSON.

    """
    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запрос и возвращает список всех сообщений в формате JSON.

        Аргументы:
            request (HttpRequest): HTTP-запрос, отправленный клиентом.
            *args: Дополнительные позиционные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Возвращает:
            JsonResponse: Ответ с данными сообщений в формате JSON.

        """
        messages = Message.objects.select_related('command').order_by('-date').values()
        return JsonResponse(list(messages), safe=False)


class CommandListView(ListView):
    """
    Класс представления (ListView) списка команд.

    Атрибуты:
        - template_name (str): Имя шаблона для отображения списка команд.
        - model (Command): Модель Command, используемая для получения данных.
        - context_object_name (str): Имя переменной контекста, передающей список команд в шаблон.

    Методы:
        get_context_data(self, **kwargs):
            Возвращает словарь с данными контекста для передачи в шаблон.
    """
    template_name = 'bot_messages/command_list.html'
    model = Command
    context_object_name = 'commands'

    def get_context_data(self, **kwargs):
        """
        Возвращает словарь с данными контекста для передачи в шаблон.

        :param **kwargs: Аргументы контекста.
        :return: dict: Словарь с данными контекста.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Command list"
        return context


class CommandDetailView(DetailView):
    """
    Класс представления (DetailView) деталей команды.

    Атрибуты:
        - template_name (str): Имя шаблона для отображения деталей команды.
        - model (Command): Модель Command, используемая для получения данных.

    Методы:
        get_context_data(self, **kwargs):
            Возвращает словарь с данными контекста для передачи в шаблон.
    """
    template_name = 'bot_messages/command_detail.html'
    model = Command

    def get_context_data(self, **kwargs):
        """
        Возвращает словарь с данными контекста для передачи в шаблон.

        :param **kwargs: Аргументы контекста.
        :return: dict: Словарь с данными контекста.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Command detail"
        return context


class CommandUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Класс представления (UpdateView) обновления команды.

   Атрибуты:
        - template_name (str): Имя шаблона для отображения формы обновления команды.
        - model (Command): Модель Command, используемая для получения данных.
        - form_class (CommandForm): Класс формы, используемой для обновления данных команды.
        - permission_required (str): Требуемое разрешение для доступа к представлению.
                                    Пользователи должны иметь разрешение 'bot_messages.can_change_command',
                                    чтобы получить доступ к представлению обновления команды.

    """
    template_name = 'bot_messages/command_update.html'
    model = Command
    form_class = CommandForm
    permission_required = 'bot_messages.can_change_command'
