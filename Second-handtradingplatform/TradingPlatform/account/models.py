from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0)

class User(models.Model):
    username=models.CharField(max_length=40,unique=True)
    passwd=models.CharField(max_length=40)
    gender_choice=((0,'男'),(1,'女'))
    gender=models.IntegerField(default=0,choices=gender_choice)
    createdate=models.DateTimeField(auto_now_add=True)
    user_address=models.CharField(max_length=255)
    logindate=models.DateTimeField(default=timezone.now)
    tel=models.CharField(max_length=11)
    post_code=models.CharField(max_length=10)
    shop_id=models.IntegerField(default=0)
    email=models.EmailField()
    head_picture=models.URLField()
    isdelete=models.IntegerField(default=0)
    users=UserManager()

    def __str__(self):
        return self.username
    class Meta:
        db_table='user'

class ShopManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0)   
class Shop_user(models.Model):
    shop_name=models.CharField(max_length=40,unique=True)
    prestige=models.IntegerField()
    volume=models.IntegerField()
    shop_introduction=models.TextField(max_length=255)
    shop_address=models.TextField(max_length=255)
    create_data=models.DateTimeField()
    isdelete=models.IntegerField(default=0)
    shops=ShopManager()

    def __str__(self):
        return self.shop_name
    class Meta:
        db_table='shop_user'