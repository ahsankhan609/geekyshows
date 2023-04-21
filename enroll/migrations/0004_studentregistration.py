# Generated by Django 4.1.5 on 2023-01-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enroll", "0003_alter_student_city_alter_student_country_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentRegistration",
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
                ("stu_name", models.CharField(max_length=70)),
                ("stu_email", models.EmailField(max_length=70)),
                ("stu_password", models.CharField(max_length=64)),
            ],
        ),
    ]
