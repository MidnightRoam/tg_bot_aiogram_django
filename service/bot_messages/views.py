from django.views.generic import ListView

from .models import Message


class MessageListView(ListView):
    template_name = 'bot_messages/messages_list.html'
    model = Message
