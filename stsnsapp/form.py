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
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = '' # 全フィールドを入力必須
            # オートフォーカスとプレースホルダーの設定
            print(field.label)
            if field.label == 'ユーザー名':
                field.widget.attrs['autofocus'] = '' # 入力可能状態にする
                field.widget.attrs['placeholder'] = '田中'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@gmail.com'


class H_liquor(forms.ModelForm,):
    class Meta:
        model = CustomUser
        fields = ('how_many_liquor',)

class H_cigalettes(forms.ModelForm,):
    class Meta:
        model = CustomUser
        fields = ('how_many_cigalettes',)


class createform(forms.ModelForm,):
    class Meta:
        model = BoardModel
        fields = ('title','content',)

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ( 'username','email',)

    # bootstrap4
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''

