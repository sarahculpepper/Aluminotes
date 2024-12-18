# Generated by Django 5.0.6 on 2024-06-19 16:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_userprofile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_prompt_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
