from django.urls import path

from .views import (
    MessageListView,
    CommandListView,
    CommandDetailView,
    CommandUpdateView,
    JsonMessageView
)

urlpatterns = [
    path('', MessageListView.as_view(), name='messages-list'),
    path('commands/', CommandListView.as_view(), name='commands-list'),
    path('command/<int:pk>/', CommandDetailView.as_view(), name='command-detail'),
    path('command/<int:pk>/update', CommandUpdateView.as_view(), name='command-update'),
    path('get_messages_list/', JsonMessageView.as_view(), name='get-messages-list'),
]
