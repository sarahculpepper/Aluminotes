# Generated by Django 5.0.6 on 2024-08-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_customuser_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                default="Aluminotes User", max_length=32, verbose_name="Username"
            ),
        ),
    ]