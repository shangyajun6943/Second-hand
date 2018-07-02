from django.urls import path
from . import views

app_name='showgoods'

urlpatterns = [
    path('single/(?P<proid>[0-9]{1-4})', views.single,name='single'),
    path('product/(?P<page>[0-9]{1,2})', views.product,name='product'),
    path('add_shopcart', views.add_shopcart,name='add_shopcart'),
]
