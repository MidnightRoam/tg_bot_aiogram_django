# Generated by Django 4.2 on 2023-07-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0004_command_message_command'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commands', models.ManyToManyField(to='bot_messages.command')),
            ],
        ),
    ]