# Generated by Django 3.2.9 on 2021-12-02 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resto_App', '0005_auto_20211202_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='Location',
        ),
    ]
