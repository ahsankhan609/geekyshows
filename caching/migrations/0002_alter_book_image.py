# Generated by Django 4.2 on 2023-06-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caching', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
