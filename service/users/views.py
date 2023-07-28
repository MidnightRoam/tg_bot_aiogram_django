from typing import Dict

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .forms import UserLoginForm


class UserLoginView(LoginView):
    """
    Представление для входа пользователя.

    Класс UserLoginView представляет страницу входа пользователя,
    используя стандартное представление LoginView из библиотеки Django.
    На странице используется пользовательский шаблон 'users/login.html'
    и форма для входа пользователя UserLoginForm.

    Атрибуты:
        template_name (str): Имя шаблона для отображения страницы входа.
        form_class (UserLoginForm): Класс формы для входа пользователя.

    Методы:
        get_context_data(**kwargs):
            Возвращает словарь с дополнительными данными контекста для отображения на странице.
            В данном случае, добавляется ключ 'title' со значением 'Sign In'.

        get_success_url():
            Возвращает URL, на который перенаправить пользователя после успешного входа.
            В данном случае, возвращается URL 'messages-list' с использованием reverse_lazy.
    """
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs) -> Dict:
        """
        Возвращает словарь с дополнительными данными контекста для отображения на странице.

        Возвращает:
            dict: Словарь с данными контекста.
        """
        context = super().get_context_data()
        context.update({
            'title': 'Sign In'
        })
        return context

    def get_success_url(self) -> reverse_lazy:
        """
        Возвращает URL для перенаправления пользователя после успешного входа.

        Возвращает:
            str: URL для перенаправления.
        """
        return reverse_lazy('messages-list')


class RegistrationTemplateView(TemplateView):
    template_name = 'users/registration.html'


class UserLogoutView(View):
    """
    View для выхода пользователя из системы.

    Атрибуты:
        request (HttpRequest): HTTP-запрос от клиента.

    Возвращаемое значение:
        HttpResponse: Перенаправление пользователя на страницу 'messages-list'.

    Методы:
        get(self, request, *args, **kwargs):
            Обработчик GET-запроса. Выполняет выход текущего пользователя из системы
            и перенаправляет его на страницу 'messages-list'.
    """
    def get(self, request, *args, **kwargs) -> HttpResponse:
        logout(request)
        return redirect('messages-list')
