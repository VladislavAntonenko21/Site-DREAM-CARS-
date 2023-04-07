from django.contrib import admin

# Register your models here.
from .models import MyAuto, Applications

admin.site.register(Applications)
admin.site.register(MyAuto)#регистрируем таблицу MyAuto в БД