from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import UserRegisterForm, UserloginForm, StraxovkaForm  # формы регистрации и аутентификации
from django.contrib.auth import login, logout

from .models import MyAuto
from .forms import MyAutoForm


#методы которые отвечают за открытие html страниц:



def search_car(request,name_car):
    # print(name_car)
    new_auto = MyAuto.objects.filter(title__icontains=name_car)  # критерии поиска
    return render(request, 'main/firstPage.html', {'new_auto': new_auto,'name_car':name_car})

def card_of_auto(request,title):
    new_auto = MyAuto.objects.filter(title=title)
    return render(request, 'main/card_of_auto.html',{'new_auto':new_auto})

# сортировки -------------------------------------------------------------------------------------------------------

# второй способ сортировки по типу кузова
def filter_car(request,typecar_car):
    new_auto = MyAuto.objects.filter(type__icontains=typecar_car)  # критерии поиска
    return render(request, 'main/firstPage.html', {'new_auto': new_auto, 'typecar_car': typecar_car})



# первый способ сортировки по типу кузова
def cabrio(request):
    type = 'Кабриолет'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def pickup(request):
    type = 'Пикап'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def hatchback(request):

    type = 'Хэтчбек'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def minivan(request):

    type = 'Минивэн'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def universal(request):

    type = 'Универсал'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def crossover(request):

    type = 'Кроссовер'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})

def coupe(request):

    type = 'Купе'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto,'type': type })

def sedan(request):

    type = 'Седан'
    search_query = request.GET.get('search_value', '')
    if search_query:
        old_auto = MyAuto.objects.filter(title__icontains=search_query)  # критерии поиска
    else:
        old_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'old_auto': old_auto, 'type': type})
#-------------------------------------------------------------------------------------------------------

def buy_ship_page(request):
    return render(request,'main/buy_shipPage.html')

def straxovanie(request):
    error = ''
    if request.method == 'POST':
        form = StraxovkaForm(request.POST)  # получение данных от пользователя с формы
        if form.is_valid():
            form.save()  # если данные коректны сохраняем их
            error = "Заявка успешно отправлена! Наш специалист свяжется с вами"
        else:
            error = 'Форма былы неверной'
    form = StraxovkaForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/straxovanie.html', data)

def admin_page_add_car(request):
    error = ''
    if request.method == 'POST':
        form = MyAutoForm(request.POST, request.FILES)#получение данных от пользователя с формы
        if form.is_valid():
            form.save()#если данные коректны сохраняем их
            error = "Авто успешно добавлено"
        else:
            error = 'Форма былы неверной'
    form = MyAutoForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'main/adminPage.html',data)

def uslugi_page(request):
    return render(request, 'main/uslugiPage.html')

def owner_page(request):
    return render(request, 'main/ownerPage.html')

def buyer_page(request):
    return render(request, 'main/buyerPage.html')

def first_page(request):
    # return render(request,'main/firstPage.html')
    # new_auto = MyAuto.objects.all()

    search_query = request.GET.get('search_value','')
    # sort_query = request.GET.get('sort_value', '')

    if search_query:
        new_auto = MyAuto.objects.filter(title__icontains=search_query)#критерии поиска
    # if sort_query:
    #     new_auto = MyAuto.objects.filter(title__icontains='Acura')  # критерии поиска
    else:
        new_auto = MyAuto.objects.all()
    return render(request, 'main/firstPage.html', {'new_auto': new_auto})



def reg_page(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            # # Create a new user object but avoid saving it yet
            # new_user = form.save(commit=False)
            # # Set the chosen password
            # new_user.set_password(form.cleaned_data['password1'])
            # # Save the User object
            # new_user.save()

            form.save()#вывод сообщения

            #автоматически авторизует пользователя
            #user = form.save()
            #login(request, user)

            messages.success(request,'Вы успешно зарегистрировались')#выводит короткое сообщение типа: error,warning,succe и тд
            return redirect('LoginPage')
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request,'main/Registr_page.html',{"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserloginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('FirstPage')
        else:
            messages.error(request,'Ошибка входа')
    else:
        form = UserloginForm()
    return render(request,'main/Log_in.html',{"form": form})

def user_logout(request):
    logout(request)
    return redirect('LoginPage')