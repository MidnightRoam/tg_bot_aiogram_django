# Generated by Django 4.2 on 2023-07-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0006_commandlog_delete_commandslog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandlog',
            name='calls_count',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
