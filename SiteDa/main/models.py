from django.db import models
from django.urls import reverse

# Create your models here.
#модель отвечает за таблицу в БД
#файл миграции описывает таблицу из БД
class MyAuto(models.Model):
    title = models.CharField('Марка и модель авто', max_length=70)
    short_description = models.CharField('Краткое описание', max_length=250)
    long_description = models.TextField('Полное описание')
    date = models.DateTimeField(auto_now_add=True)
    coast = models.CharField('Цена Авто', max_length=20)

    img1 = models.ImageField(upload_to='images/',null=False, blank=False,verbose_name = 'Изображение 1')
    img2 = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Изображение 2')
    img3 = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Изображение 3')
    img4 = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Изображение 4')
    img5 = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Изображение 5')

    CHASES_TYPE_SELECT = [ ('Купе','Купе'),
                           ('Седан','Седан'),
                           ('Минивен','Минивен'),
                           ('Кабриолет','Кабриолет'),
                           ('Кроссовер','Кроссовер'),
                           ('Пикап','Пикап'),
                           ('Хэтчбек','Хэтчбек'),
                           ('Универсал','Универсал') ]
    type = models.CharField(max_length=25, choices=CHASES_TYPE_SELECT)

    ENGINE_TYPE_SELECT = [('Бензин', 'Бензин'),
                          ('Дизель', 'Дизель'),
                          ('Гибрид', 'Гибрид'),
                          ('Электро', 'Электро') ]
    engine = models.CharField(max_length=30,choices=ENGINE_TYPE_SELECT)

    PRIVOD_TYPE_SELECT = [('Передний', 'Передний'),
                          ('Задний', 'Задний'),
                          ('Полный', 'Полный') ]
    privod = models.CharField(max_length=30,choices=PRIVOD_TYPE_SELECT)

    born_year = models.CharField('Год выпуска', max_length=30)
    engine_ob = models.CharField('Объем двигателя', max_length=30)

    KPP_TYPE_SELECT = [('Автоматическая', 'Автоматическая'),
                       ('Механика', 'Механика'),
                       ('Типтроник', 'Типтроник'),
                       ('Адаптивная', 'Адаптивная')]
    kpp = models.CharField(max_length=30,choices=KPP_TYPE_SELECT)
    probeg = models.CharField('Пробег', max_length=30)



    def __str__(self):#при помощи какого ключа будет выводиться инфа
        return self.title
    class Meta:
        verbose_name = 'Автомобили в наличии'
        verbose_name_plural = 'Автомобили в наличии'

class Applications(models.Model):
    fio = models.CharField('ФИО',max_length=20)
    tel_number = models.CharField('Номер телефона', max_length=12)
    comment = models.TextField('Комментарий')

    def __str__(self):#при помощи какого ключа будет выводиться инфа
        return self.fio
    class Meta:
        verbose_name = 'Заявки на страхование'
        verbose_name_plural = 'Заявки на страхование'