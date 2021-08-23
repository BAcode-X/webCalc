from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.MyLoginView.as_view(), name='user_login'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('register/', views.MyRegister.as_view(), name='register'),
    path('calc/', views.Calculate.as_view(), name='calculate'),
    path('history/', views.ListHistory.as_view(), name='list_calc'),
    path('profile/', views.ChangeProfile.as_view(), name='profile'),
]
