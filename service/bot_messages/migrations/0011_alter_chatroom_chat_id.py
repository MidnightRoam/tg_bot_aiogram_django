# Generated by Django 4.2 on 2023-07-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0010_chatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chat_id',
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
    ]
