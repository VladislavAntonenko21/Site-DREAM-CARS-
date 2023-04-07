from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first_page, name = 'FirstPage'), #отслеживает на какую страницу мы перешли и вызывает метод из другога файла
    path('registration', views.reg_page, name='RegPage'),
    path('login',views.user_login, name = 'LoginPage'),
    path('logout',views.user_logout, name = 'LogoutPage'),
    path('for_buyer', views.buyer_page, name = 'BuyerPage'),
    path('for_owner', views.owner_page, name = 'OwnerPage'),
    path('our_services',views.uslugi_page, name = 'UslugiPage'),
    path('admin_page',views.admin_page_add_car, name = 'AdminPage'),
    path('insurance/', views.straxovanie, name='InsurancePage'),
    path('buy_and_ship',views.buy_ship_page, name = 'Buy_Ship_Page'),
    path('car_card', views.card_of_auto, name='Card'),

    path('sedan',views.sedan, name = 'Sedan'),
    path('cross',views.crossover, name = 'Cross'),
    path('coupe', views.coupe, name='Coupe'),
    path('pickup', views.pickup, name='Pickup'),
    path('universal', views.universal, name='Universal'),
    path('hatchback', views.hatchback, name='Hatchback'),
    path('minivan', views.minivan, name='Minivan'),
    path('cabrio', views.cabrio, name='Cabrio'),

    path('cars/<str:title>',views.card_of_auto,name = 'Card'),

    path('<str:name_car>',views.search_car, name='filtered_car'),

    # второй вариант сортировки по типу кузова
    # path('filter/<str:typecar_car>', views.filter_car, name='filter_car'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)