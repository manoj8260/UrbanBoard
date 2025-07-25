# Generated by Django 5.2.4 on 2025-07-13 16:09

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[accounts.models.User.validate_phone], verbose_name='Phone Number'),
        ),
    ]
