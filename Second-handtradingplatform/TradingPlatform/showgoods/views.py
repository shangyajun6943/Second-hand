from django.shortcuts import render
from .models import Product
from until.getinfo import *
from django.http import HttpResponse
from shopcart.models import *
from datetime import datetime
import time
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def single(request,proid=None):
    if proid is None:
        return render(request,'404.html')
    else:
        product=list(Product.products.filter(id=proid))[0]
        #获取登录对象信息
        user=getUser(request)
        return render(request,'showgoods/single.html',
                {'product':product,'userinfo':user,'pro_id':product.id})
    

def product(request,page=None):
    if page is None:
        return render(request,'404.html')
    else:
        #获取商品类型
        page=int(page)
        # 获取该类型的所有商品
        products=list(Product.products.filter(pro_type=page).order_by('-pro_volume'))
        # 返回该系列的商品
        return render(request,'showgoods/products.html',{'products':products})

def add_shopcart(request):
    proid=request.POST['pro_id']
    print(proid)
    num=request.POST['num']
    print(num)
    if proid is None:
        return HttpResponse(0)
    else:
        #检测用户是否登录
        try:
            #获取用户信息
            user=getUser(request)
            #获取用户对象
            user2=User.users.get(pk=user.id)
        except AttributeError as e:
            print(e)
            return HttpResponse(2)
        #获取商铺对象
        shop=Shop_user.shops.get(pk=1)
        #获取商品
        product=Product.products.get(pk=int(proid))
        #获取当前时间的年月日
        year=datetime.now().year
        month=datetime.now().month
        day=datetime.now().day
        order=Order.orders.filter(isdelete=0,
            userid=user.id,order_time__gte=datetime(year,month,day))
        if not bool(list(order)):
            # 创建新订单
            order=Order()
            time1=str(time.time())
            order_number=time1[0:10]+time1[11:]+str(product.pro_volume)+str(product.pro_num)
            order.order_number=order_number
            order.userid=user2
            order.shopid=shop
            order.order_time=datetime(year,month,day)
            order.delivery_time=datetime.now()
            order.shopping_state=0
            order.save()
        # 创建新订单项
        order_item=Order_item()
        order_item.pro_id=product
        try:
            order_item.order_id=list(order)[0]
        except TypeError as e:
            print(e)
            order_item.order_id=order
        order_item.quantity=int(num)
        order_item.save()
        return HttpResponse(1)