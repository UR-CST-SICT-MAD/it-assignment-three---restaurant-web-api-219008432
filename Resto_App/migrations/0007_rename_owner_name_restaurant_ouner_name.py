# Generated by Django 3.2.9 on 2021-12-06 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resto_App', '0006_remove_restaurant_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Owner_name',
            new_name='Ouner_name',
        ),
    ]