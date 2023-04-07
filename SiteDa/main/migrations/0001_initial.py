# Generated by Django 4.1.2 on 2022-10-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название Авто')),
                ('short_description', models.CharField(max_length=250, verbose_name='Краткое описание')),
                ('long_description', models.TextField(verbose_name='Полное описание')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
