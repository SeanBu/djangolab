# Generated by Django 4.1.2 on 2022-10-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pepper',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
