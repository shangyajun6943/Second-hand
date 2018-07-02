from django.db import models
from account.models import *
from showgoods.models import *

# Create your models here.


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0) 

class Comment(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    pro_id=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    shopid=models.ForeignKey(Shop_user,on_delete=models.SET_NULL,blank=True,null=True)
    comment=models.CharField(max_length=255)
    sat_level=models.IntegerField()
    support=models.BooleanField(default=False)
    isdelete=models.IntegerField(default=0)
    comments=CommentManager()
    def __str__(self):
        return self.id
    class Meta:
        db_table='comment'

class FocusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0)

class Focus(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    shopid=models.ForeignKey(Shop_user,on_delete=models.SET_NULL,blank=True,null=True)
    pro_id = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    isdelete=models.IntegerField(default=0)
    focus=FocusManager()
    def __str__(self):
        return self.id
    class Meta:
        db_table='focus'