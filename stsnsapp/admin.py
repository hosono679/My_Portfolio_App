from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from stsnsapp.models import CustomUser,liquor,cigalettes,BoardModel

#ユーザー設定
admin.site.register(CustomUser)
#ユーザーごとのお酒節約量
admin.site.register(liquor)
#ユーザーごとの煙草節約量
admin.site.register(cigalettes)
#掲示板
admin.site.register(BoardModel)