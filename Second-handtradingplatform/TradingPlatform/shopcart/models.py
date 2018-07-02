from django.db import models
from account.models import *
from showgoods.models import *

# Create your models here.


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0) 

class Order(models.Model):
    order_number=models.CharField(max_length=255)
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    shopid=models.ForeignKey(Shop_user,on_delete=models.SET_NULL,blank=True,null=True)
    order_time=models.DateTimeField()
    delivery_time=models.DateTimeField()
    shopping_state=models.IntegerField()
    isdelete=models.IntegerField(default=0)
    orders=OrderManager()

    def __str__(self):
            return self.order_number
    class Meta:
        db_table='order'

class OrderItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0) 
class Order_item(models.Model):
    pro_id=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order_id=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField()
    isdelete=models.IntegerField(default=0)
    orderitem=OrderItemManager()
    # def __str__(self):
    #         return self.id
    class Meta:
        db_table='order_item'