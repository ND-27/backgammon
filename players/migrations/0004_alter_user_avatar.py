# Generated by Django 5.1.2 on 2024-10-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='avatar'),
        ),
    ]
