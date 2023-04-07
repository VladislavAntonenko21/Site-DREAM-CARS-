from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import *
from .models import MyAuto, Applications
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea,ImageField, FileField, ChoiceField

class StraxovkaForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['fio','tel_number','comment']#поля из таблицы Applications

        widgets = {
            "fio": TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО'}),
            "tel_number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            "comment": Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
        }

class MyAutoForm(ModelForm):
    class Meta:
        model = MyAuto
        fields = ['title','short_description','long_description','coast','img1','img2','img3','img4','img5','type','engine','born_year','privod','engine_ob','kpp','probeg']#поля из таблицы MyAuto

        widgets = {
            "title": TextInput(attrs={'class':'form-control', 'placeholder':'Название авто' }),
            "short_description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            "long_description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Полное описание'}),
            # "date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            "coast": TextInput(attrs={'class': 'form-control', 'placeholder': 'Цена авто'}),

            "type": Select(attrs={'id':'DropDownList','class':'cs-select cs-skin-rotate'}),#можно ставить свой id чтобы написать для поля стиль
            "engine": Select(attrs={'id':'DropDownList','class':'cs-select cs-skin-rotate'}),
            "privod": Select(attrs={'id':'DropDownList','class':'cs-select cs-skin-rotate'}),
            "kpp": Select(attrs={'id':'DropDownList','class':'cs-select cs-skin-rotate'}),

            "probeg": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег, км'}),
            "born_year": TextInput(attrs={'class': 'form-control', 'placeholder': 'Год выпуска'}),
            "engine_ob": TextInput(attrs={'class': 'form-control', 'placeholder': 'Объем двигателя'}),
        }


class UserloginForm(AuthenticationForm):
    username = forms.CharField(label="Имя Пользователя", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин','autofocus': ''}),)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Имя Пользователя", widget = forms.TextInput(attrs = {'class': 'form-control','placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'E-mail'}))
    password1 = forms.CharField(required=True,label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True,label="Подверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = {'username','email','password1','password2'}

    # def clean(self):
    #
    #     if password1 and password2 and password1 != password2:
    #         errors = {'password2': ValidationError('Введённые пароли не совпадают', code='password_mismatch')}
    #         raise ValidationError(errors)
    #     else:
    #         return self.cleaned_data
    # def clean_password1(self):
    #     super().clean()
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #
    #
    #     # cd = self.cleaned_data['password1']
    #     # print(cd['password1'])
    #     if password1 != password2:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     else:
    #         return self.cleaned_data

        #Поля по умолчанию
        # widgets = {
        #     'username': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Имя пользователя'}),
        #     'email': forms.EmailInput(attrs = {'class':'form-control'}),
        #     'password1': forms.PasswordInput(attrs = {'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        # }


# class UserRegisterForm(UserCreationForm):
#     class Meta:
#
#         model = User
#         fields = ('username','password','password2')
#         widgets = {
#             'username': forms.TextInput(attrs = {'class': 'form-input'}),
#             'password': forms.PasswordInput(attrs = {'class':'form-input'}),
#             'password2': forms.PasswordInput(attrs = {'class':'form-input'})
#         }
