from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0) 

class Product(models.Model):
    pro_name=models.CharField(max_length=40,unique=True)
    price=models.DecimalField(max_digits=7,decimal_places=3)
    pro_status=models.IntegerField(default=1)
    pro_type=models.IntegerField()
    pro_num=models.IntegerField()
    pro_volume=models.IntegerField()
    pro_introduction=models.CharField(max_length=255)
    shop_id=models.IntegerField()
    img_1=models.URLField()
    img_2=models.URLField()
    img_3=models.URLField()
    isdelete=models.IntegerField(default=0)
    products=ProductManager()

    def __str__(self):
            return self.pro_name
    class Meta:
        db_table='product'