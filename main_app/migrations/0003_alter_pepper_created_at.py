# Generated by Django 4.1.2 on 2022-10-06 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pepper_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pepper',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 6, 15, 37, 39, 984001, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]