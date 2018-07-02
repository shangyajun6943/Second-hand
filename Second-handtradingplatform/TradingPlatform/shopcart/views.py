from django.shortcuts import render
from django.http import HttpResponse
from shopcart.models import *
from showgoods.models import *
from shopcart.shopcart import *
from datetime import datetime
from django.contrib.sessions.models import Session
import time
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from until.getinfo import *
# Create your views here.


def show(request):
    # 判断是否登录
    try:
        #从colkie中获取sessionID
        sessionid=request.COOKIES.get('sessionid')
        #从数据库中获取seesion数据
        sess = Session.objects.get(pk=sessionid)
    #未登录
    except Exception as e:
        print(e)
        return render(request, 'login/login.html')
        # sess.get_decoded()['userinfo'] 是个json字符串
        # 把json字符串转换成字典
    sess2 = json.loads(sess.get_decoded()['userinfo'])

        # 把字典转换成对象
    user = User()
    user.__dict__ = sess2
    userid=user.id
    #已登录
    shopcart=ShopCart()
    #当前时间-获取当天订单
    now = datetime.now()
    #获取查看时当天的订单
    year=now.year
    month=now.month
    day=now.day
    order=list(Order.orders.all().filter(order_time__gte=datetime(year,month,day),userid=userid))
    if order:
        order = order[0]
        # print(order)
        if not bool(order):
            return render(request, 'shopcart/shopcartshow.html', {"shopcart": shopcart,'userinfo':user})
        else:
            shopcart.order=order
            list1=[]
            #获取订单的订单ID-查找订单项
            order_id = order.id
            #由当天的订单的id查询获取isdelete=0的订单项
            shop_user = list(Shop_user.shops.all().filter(id=shopcart.order.shopid_id))
            # print(shop_user)
            shop_user=shop_user[0]
            shopcart.shop_user=shop_user
            items=list(Order_item.orderitem.all().filter(order_id=order_id,isdelete=0))
            if not bool(items):
                shopcart.order_item_list=list1
                return render(request, 'shopcart/shopcartshow.html', {"shopcart": shopcart,'userinfo':user})
            else:
                for item in items:
                    list_item = OrderItems()
                    list_item.order_item=item
                    #订单项id
                    product=item.pro_id
                    #遍历订单获取产品
                    #从product表获得所有的订单项指向的产品   ?
                    # products = Product.products.get(id=int(item.pro_id))
                    #产品信息

                    list_item.product=product
                    #获取单个订单项总价
                    item_subtotal=list_item.product.price*list_item.order_item.quantity
                    #将总价加给order_item
                    list_item.order_item.subtotal=item_subtotal
                    #获取总价


                    list1.append(list_item)
                shopcart.order_item_list=list1

        quantity = json.dumps(list_item.order_item.quantity, default=lambda obj: obj.__dict__)
        request.session['order_item_list'] = quantity
        # print(quantity)

        return render(request,'shopcart/shopcartshow.html',{"shopcart":shopcart,'userinfo':user})
    else:
        return render(request, 'shopcart/shopcartshow.html', {"shopcart": shopcart,'userinfo':user})



# 未完成功能：物品数量增加减少，点击删除，全选或者单选后价格动态变化。
@csrf_exempt
def remove(request):
    ordid=request.POST['orderid']
    print(ordid)
    orderitem=Order_item.orderitem.get(pk=int(ordid))
    orderitem.isdelete=1
    orderitem.save()
    return HttpResponse(1)

def get_reduce(request):
    pass
    return HttpResponse(1)

def countPrice(request):
    #得到用户
    user=getUser(request)
    if user is None:
        return HttpResponse(0)
    #获取订单
    now = datetime.now()
    #获取查看时当天的订单
    year=now.year
    month=now.month
    day=now.day
    order=list(Order.orders.filter(order_time__gte=datetime(year,month,day),userid=int(user.id)))[0]
    #获取所有订单项
    order_item=list(Order_item.orderitem.filter(order_id=order.id,isdelete=0))
    sum1=0
    for item in order_item:
        price=item.pro_id.price
        sum1+=int(price)
    return HttpResponse(sum1)

def removeShopcart(request):
    #得到用户
    user=getUser(request)
    if user is None:
        return HttpResponse(0)
    #获取订单
    now = datetime.now()
    #获取查看时当天的订单
    year=now.year
    month=now.month
    day=now.day
    order=list(Order.orders.filter(order_time__gte=datetime(year,month,day),userid=int(user.id)))[0]
    #获取所有订单项
    order_item=list(Order_item.orderitem.filter(order_id=order.id,isdelete=0))
    for item in order_item:
        item.isdelete=1
        item.save()
    return HttpResponse(1)


