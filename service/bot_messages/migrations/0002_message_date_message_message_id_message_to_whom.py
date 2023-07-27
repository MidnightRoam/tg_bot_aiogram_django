# Generated by Django 4.2 on 2023-07-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='message_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='to_whom',
            field=models.TextField(blank=True, null=True),
        ),
    ]
