# Generated by Django 3.2.9 on 2021-12-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resto_App', '0007_rename_owner_name_restaurant_ouner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Rating',
            field=models.CharField(choices=[('*', 'StarI'), ('**', 'StarII'), ('***', 'StarIII'), ('****', 'StarIV'), ('*****', 'StarV')], max_length=50, null=True),
        ),
    ]
