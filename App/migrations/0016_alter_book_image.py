# Generated by Django 4.0.1 on 2022-04-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]