from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    """
    Форма для входа пользователя.

    Класс UserLoginForm представляет форму для ввода учетных данных пользователя
    при попытке входа на сайт. Он является наследником стандартной формы AuthenticationForm
    из библиотеки Django.

    Поля:
        username (forms.CharField): Поле для ввода имени пользователя (логина).
        password (forms.CharField): Поле для ввода пароля пользователя.

    Атрибуты:
        Нет дополнительных атрибутов для данного класса.

    Методы:
        __init__(*args, **kwargs):
            Конструктор класса, который вызывает конструктор родительского класса
            и добавляет атрибут 'class' для виджетов полей формы. Это делается
            для того, чтобы применить стилевое оформление из CSS-класса 'auth__input'.

    Примечания:
        Этот класс использует стандартные поля из Django для ввода имени пользователя и пароля,
        а также применяет CSS-класс 'login__input' к виджетам полей 'username' и 'password'
        для стилизации элементов на странице.
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login__input'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'login__input'
            }
        )
    )

    def __init__(self, *args, **kwargs) -> None:
        """
        Конструктор класса UserLoginForm.

        Вызывает конструктор родительского класса и применяет стилевой CSS-класс 'auth__input'
        к виджетам полей формы, чтобы стилизовать их на странице.

        Аргументы:
            *args: Позиционные аргументы для передачи в конструктор родительского класса.
            **kwargs: Именованные аргументы для передачи в конструктор родительского класса.
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'auth__input'


class UserCreateForm(UserCreationForm):
    """
    Форма для создания нового пользователя.

    Атрибуты:
        - username (forms.CharField): Поле для ввода имени пользователя (логина).
        - password1 (forms.CharField): Поле для ввода пароля.
        - password2 (forms.CharField): Поле для повторного ввода пароля (для подтверждения).
        - Meta (class): Вложенный класс для указания модели и полей, используемых в форме.

    Методы:
        __init__(self, *args, **kwargs):
            Конструктор класса, выполняющий инициализацию формы.
            Применяет стилизацию к видимым полям формы.
    """
    username = forms.CharField(
        max_length=250,
        widget=forms.TextInput(),
        label='Username'
    )

    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Password'
    )

    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Repeat password'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Конструктор класса, выполняющий инициализацию формы.
        Применяет стилизацию к видимым полям формы.

        :param *args: Аргументы.
        :param **kwargs: Ключевые аргументы.
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'auth__input'
