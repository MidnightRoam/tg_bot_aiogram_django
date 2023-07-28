# Generated by Django 4.2 on 2023-07-28 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0005_commandslog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calls_count', models.PositiveIntegerField(blank=True, null=True)),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot_messages.command')),
            ],
        ),
        migrations.DeleteModel(
            name='CommandsLog',
        ),
    ]
