# Generated by Django 4.2 on 2023-07-31 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0007_alter_commandlog_calls_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='command',
            options={'permissions': [('can_view_command', 'Can view command'), ('can_change_command', 'Can change command'), ('can_delete_command', 'Can delete command'), ('can_add_command', 'Can add command')]},
        ),
    ]