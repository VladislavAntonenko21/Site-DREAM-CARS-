# Generated by Django 4.1.2 on 2022-10-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_myauto_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=20, verbose_name='ФИО')),
                ('tel_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Заявки на страхование',
                'verbose_name_plural': 'Заявки на страхование',
            },
        ),
        migrations.AlterField(
            model_name='myauto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
