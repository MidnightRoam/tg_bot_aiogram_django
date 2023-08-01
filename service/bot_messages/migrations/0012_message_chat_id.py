# Generated by Django 4.2 on 2023-07-31 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0011_alter_chatroom_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_messages.chatroom'),
        ),
    ]