from django.shortcuts import render
from until.getinfo import *

# Create your views here.
def index(request):
    # 获取登录对象信息
    user=getUser(request)
    #显示商品
    products=getIndexProduct()
    if user is None:
        return render(request,'index.html',{'products':products})
    #把对象返回首页
    return render(request,'index.html',{'userinfo':user,'products':products})
