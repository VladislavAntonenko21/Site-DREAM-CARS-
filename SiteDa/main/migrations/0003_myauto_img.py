# Generated by Django 4.1.2 on 2022-10-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_myauto_options_myauto_coast'),
    ]

    operations = [
        migrations.AddField(
            model_name='myauto',
            name='img',
            field=models.ImageField(default=12, height_field=100, upload_to='images/', width_field=100),
            preserve_default=False,
        ),
    ]
