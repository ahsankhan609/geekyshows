# Generated by Django 4.1.5 on 2023-01-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enroll", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="enrolled_courses",
            field=models.IntegerField(default=1),
        ),
    ]
