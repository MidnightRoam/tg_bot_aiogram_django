from django.urls import path

from .views import MessageListView

urlpatterns = [
    path('', MessageListView.as_view(), name='messages-list'),
]
