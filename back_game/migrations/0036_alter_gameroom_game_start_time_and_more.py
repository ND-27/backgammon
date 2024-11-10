# Generated by Django 5.1.2 on 2024-11-04 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_game', '0035_alter_gameroom_game_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='game_start_time',
            field=models.IntegerField(blank=True, default=1730741725, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='time_player_1',
            field=models.IntegerField(blank=True, default=1730741725, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='time_player_2',
            field=models.IntegerField(blank=True, default=1730741725, null=True),
        ),
        migrations.AlterField(
            model_name='waitingroom',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 17, 37, 25, 496092, tzinfo=datetime.timezone.utc)),
        ),
    ]
