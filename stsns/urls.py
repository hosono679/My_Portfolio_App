from django.contrib import admin
from django.urls import path,include
app_name = "stsnsapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("stsnsapp.urls")),
    
]
