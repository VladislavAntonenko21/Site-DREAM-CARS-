# Generated by Django 4.1.2 on 2022-11-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_myauto_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myauto',
            name='type',
            field=models.CharField(choices=[('Купе', 'Купе'), ('Седан', 'Седан'), ('Минивен', 'Минивен'), ('Кабриолет', 'Кабриолет'), ('Кроссовер', 'Кроссовер'), ('Пикап', 'Пикап'), ('Хэтчбек', 'Хэтчбек'), ('Универсал', 'Универсал')], default='Тип кузова', max_length=25),
        ),
    ]
