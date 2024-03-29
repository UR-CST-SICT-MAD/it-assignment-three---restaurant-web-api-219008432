# Generated by Django 3.2.9 on 2021-11-26 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish_name', models.CharField(max_length=40)),
                ('Cooking_Time', models.TimeField()),
                ('Ingredient', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_name', models.CharField(max_length=20)),
                ('Owner_name', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=40)),
                ('Rating', models.CharField(choices=[('StarI', '*'), ('StarII', '**'), ('StarIII', '***'), ('StarIV', '****'), ('StarV', '*****')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('District', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sectors', to='Resto_App.district')),
            ],
        ),
    ]
