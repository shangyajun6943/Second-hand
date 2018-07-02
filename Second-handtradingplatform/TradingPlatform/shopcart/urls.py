from django.urls import path
from . import views

app_name='shopcart'

urlpatterns = [
    path('', views.show,name='show'),
    path('remove', views.remove),
    path('countPrice', views.countPrice,name='countPrice'),
    path('removeShopcart', views.removeShopcart,name='removeShopcart'),
]
