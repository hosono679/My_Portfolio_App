from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from stsnsapp.models import CustomUser,liquor,cigalettes,BoardModel

admin.site.register(CustomUser)
admin.site.register(liquor)
admin.site.register(cigalettes)
admin.site.register(BoardModel)