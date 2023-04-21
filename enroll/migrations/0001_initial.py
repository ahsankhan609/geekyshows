# Generated by Django 4.1.5 on 2023-01-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=70)),
                ("address", models.TextField(default="Not Available", max_length=254)),
                ("city", models.CharField(default="Not Available", max_length=70)),
                ("state", models.CharField(default="Not Available", max_length=70)),
                ("country", models.CharField(default="Not Available", max_length=70)),
            ],
        ),
    ]