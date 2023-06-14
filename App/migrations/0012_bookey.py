# Generated by Django 4.0.1 on 2022-04-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('bookformat', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=150)),
                ('pages', models.CharField(max_length=150)),
                ('totalratings', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
