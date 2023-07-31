from django import forms

from .models import Command


class CommandForm(forms.ModelForm):
    """
    Форма для создания и редактирования объекта модели Command.

    Атрибуты:
        - model (Command): Класс модели Command, для которой создается форма.
        - fields (list): Список полей модели Command, которые будут отображаться в форме.

    Методы:
        __init__(self, *args, **kwargs):
            Конструктор класса, выполняющий инициализацию формы.
            Назначает класс "input__default" для видимых полей формы для стилизации.
    """
    class Meta:
        model = Command
        fields = ('command', 'text')

    def __init__(self, *args, **kwargs) -> None:
        """
        Конструктор класса, выполняющий инициализацию формы.
        Назначает класс "input__default" для видимых полей формы для стилизации.

        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input__default'
