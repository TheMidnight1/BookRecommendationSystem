# Generated by Django 4.0.1 on 2022-04-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_remove_book_author_remove_book_bookformat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
    ]
