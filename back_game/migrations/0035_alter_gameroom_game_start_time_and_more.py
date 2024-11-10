# Generated by Django 5.1.2 on 2024-11-04 12:03

import back_game.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_game', '0034_alter_waitingroom_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='game_start_time',
            field=models.IntegerField(blank=True, default=1730721834, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='place_status',
            field=models.JSONField(blank=True, default=back_game.models.get_default_board_state, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='time_player_1',
            field=models.IntegerField(blank=True, default=1730721834, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='time_player_2',
            field=models.IntegerField(blank=True, default=1730721834, null=True),
        ),
        migrations.AlterField(
            model_name='waitingroom',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 12, 5, 54, 823071, tzinfo=datetime.timezone.utc)),
        ),
    ]
