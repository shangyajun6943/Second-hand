from django.shortcuts import render
from django.http import HttpResponse
from django.conf import *
import  json
from django.shortcuts import redirect
from .models import *
from datetime import datetime,time
from until.getinfo import *

# Create your views here.


def login(request):
    try:
        str1=request.session['errormsg']
    except Exception as e:
        print(e)
        return render(request,'login/login.html')
    #把json字符串转换成字典
    return render(request,'login/login.html',{'errormsg':str1})

def register(request):
    return render(request,'register/register.html')

def conact(request):
    return render(request,'conact/conact_index.html')

def do_register(request):
    '''
        注册功能
    '''
    # 获取前台请求的数据
    #用户名
    username = request.POST['username']
    #第一次密码
    password1=request.POST['password1']
    #第二次密码
    password2=request.POST['password2']
    #电话
    tel=request.POST['tel']
    #邮箱
    email=request.POST['email']
    #邮编
    post_code=request.POST['post_code']
    # 检测用户是否存在
    user = User.users.filter(username=username);
    if not user:
        user = User()
        # 用户名
        user.username = username
        # 密码
        user.passwd = password2
        #创建时间
        user.createdate=str(datetime.now())[:-7]
        #登录时间
        user.logindate=str(datetime.now())[:-7]
        #电话
        user.tel = tel
        #邮箱
        user.email = email
        #邮编
        user.post_code = post_code
        #创建seesion
        u= json.dumps(user, default=lambda obj: obj.__dict__)
        request.session['userinfo'] = u
        #创建cookie
        # rp=HttpResponse()
        # rp.set_cookie('session_key',request.session.session_key)
        #保存数据
        user.save()
        #重定向首页
        return redirect('index')
    return HttpResponse('用户名已存在')


def out_register(request):
    if request.session['userinfo']:
        request.session.flush()
        return redirect('index')
    else:
        return HttpResponse('error')

def loginVerify(request):
    '''
        登录
    '''
    #用户名
    username=request.POST['username']
    #密码
    password=request.POST['password']
    #检测用户是否存在
    try:
        user=User.users.get(username=username)
    except Exception as e:
        request.session['errormsg']='用户名错误!!!'
        return redirect('account:login')
    try:
        user=User.users.get(username=username,passwd=password)
    except Exception as e:
        request.session['errormsg']='密码错误!!!'
        return redirect('account:login')
    #判单用户
    user.createdate=str(user.createdate)[:-7]
    user.logindate=str(user.logindate)[:-7]
    #放入session
    user1 = json.dumps(user, default=lambda obj: obj.__dict__)
    request.session['userinfo'] = user1
    #重定向
    return redirect('index')

def Verifyum(request):
    '''
        异步Ajax验证用户是否存在
    '''
    username=request.GET['username']
    user=User.users.filter(username=username)
    if user:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

      
def user_detail(request):
    return redirect('account:user_detail3')

def user_detail2(request):
    return render(request,'userdetail/user_block.html')

def user_detail3(request):
    u=getUser(request)
    return render(request,'userdetail/user_info.html',{'userinfo':u})

def user_order_info(request):
    return redirect('account:user_order_info2')

def user_order_info2(request):
    return render(request,'userdetail/user_order.html')

def user_address_info(request):
    return redirect('account:user_address_info2')

def user_address_info2(request):
    return render(request,'userdetail/user_address.html')