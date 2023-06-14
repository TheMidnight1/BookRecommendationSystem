# Generated by Django 4.0.1 on 2022-07-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0058_alter_main_genre_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='main_category',
        ),
        migrations.AddField(
            model_name='genre',
            name='main_category',
            field=models.ManyToManyField(related_name='main_genre', to='App.Main_Genre'),
        ),
    ]
