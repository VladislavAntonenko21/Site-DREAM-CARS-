# Generated by Django 4.1.2 on 2022-10-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_myauto_born_year_myauto_engine_myauto_engine_ob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myauto',
            name='img',
        ),
        migrations.AddField(
            model_name='myauto',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 1'),
        ),
        migrations.AddField(
            model_name='myauto',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 2'),
        ),
        migrations.AddField(
            model_name='myauto',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 3'),
        ),
        migrations.AddField(
            model_name='myauto',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 4'),
        ),
        migrations.AddField(
            model_name='myauto',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 5'),
        ),
        migrations.AlterField(
            model_name='myauto',
            name='title',
            field=models.CharField(max_length=70, verbose_name='Марка и модель авто'),
        ),
    ]
