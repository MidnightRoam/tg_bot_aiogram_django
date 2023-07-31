from typing import Dict

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import UserLoginForm, UserCreateForm


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


class UserCreateView(CreateView):
    """
    Представление для создания нового пользователя.

    Атрибуты:
        template_name (str): Строка, содержащая имя шаблона HTML для отображения представления.
        form_class (Form): Класс формы, используемой для создания нового пользователя.
        success_url (str): Строка с URL-адресом, на который будет перенаправлен пользователь
                           после успешного создания нового аккаунта.

    Методы:
        get_context_data(self, **kwargs):
            Возвращает контекстные данные для шаблона HTML, которые позволяют добавить
            дополнительные переменные в шаблон перед его рендерингом. В данном случае, добавляется
            переменная 'title' со значением 'Sign Up'.

        form_valid(self, form):
            Вызывается при успешной проверке и сохранении формы. Создает нового пользователя
            на основе данных из формы, выполняет вход в систему от имени этого пользователя и
            перенаправляет на страницу 'messages-list'.
    """
    template_name = 'users/registration.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('messages-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'title': 'Sign Up'
        })
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('messages-list')


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
