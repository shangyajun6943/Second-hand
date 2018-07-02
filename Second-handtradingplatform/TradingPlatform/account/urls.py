from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('login', views.login,name='login'),
    path('login/*/', views.login,name='login2'),
    path('register', views.register,name='register'),
    path('conact', views.conact,name='conact'),
    path('do_register',views.do_register,name='do_register'),
    path('out_register',views.out_register,name='out_register'),
    path('loginVerify',views.loginVerify,name='loginVerify'),
    path('Verifyum',views.Verifyum),
    path('user_detail',views.user_detail,name='user_detail'),
    path('user_detail2',views.user_detail2,name='user_detail2'),
    path('user_order_info',views.user_order_info,name='user_order_info'),
    path('user_address_info',views.user_address_info,name='user_address_info'),
]
