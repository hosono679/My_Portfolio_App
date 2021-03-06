from django.urls import path,include
from . import views 
from .views import listfunc,BoardCreate,detailfunc,deletefunc,UserDeleteView
from django.conf.urls.static import static
from django.conf import settings  

app_name = 'stsnsapp'
urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('signup_done/', views.SignupDone.as_view(), name='signup_done'),
    path('guest_login/', views.guest_login, name = 'guest_login'), 
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'), 
    path('user_delete<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('create/',BoardCreate.as_view(),name='create'),
    path('first/',views.first_page,name=''),
    path('my_page/<int:pk>/', views.mypage_liquor_cigalettes, name='mypage'), 
    path('ranking/',views.ranking_view, name = 'ranking'),
    path('top_page_list/',listfunc, name = 'top_page'),
    path('delete/<int:pk>',deletefunc.as_view(),name='delete'),
    path('detail/<int:pk>',detailfunc,name='detail'),
    path('good/<int:pk>/', views.how_many_good, name='good'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 