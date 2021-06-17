from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth import get_user_model
from django.db import models
from .models import CustomUser,BoardModel
User = get_user_model()

#ログイン用フォーム
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        labels = {'username': 'ユーザー名', 'password': 'メールアドレス'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


#サインアップ用フォーム
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')
        labels = {'username': 'ユーザー名', 'email': 'メールアドレス'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            #フォームの整形
            field.widget.attrs['class'] = 'form-control'
            #入力必須
            field.widget.attrs['required'] = '' 
            if field.label == 'ユーザー名':
                #初期カーソル位置
                field.widget.attrs['autofocus'] = '' 
                field.widget.attrs['placeholder'] = '田中'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@gmail.com'

#お酒節約量計算
class H_liquor(forms.ModelForm,):
    class Meta:
        model = CustomUser
        fields = ('how_many_liquor',)

#煙草節約量計算
class H_cigalettes(forms.ModelForm,):
    class Meta:
        model = CustomUser
        fields = ('how_many_cigalettes',)

#掲示板への書き込み機能
class createform(forms.ModelForm,):
    class Meta:
        model = BoardModel
        fields = ('title','content',)

#ユーザー情報アップデート
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ( 'username','email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''

