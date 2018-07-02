from account.models import *
import json
from showgoods.models import Product

def getUser(request):
    '''
        从session中获取登录后的用户信息
    '''
    try:
        sess2=json.loads(request.session['userinfo'])
    except Exception as e:
        print(e)
        return None
    #把字典转换成对象
    user=User()
    user.__dict__=sess2
    return user

def getIndexProduct():
    '''
        首页的产品信息的展示代码
    '''
    products=[]
    list1=[1,2,3]
    for i in list1:
        products1=list(Product.products.filter(isdelete=0,pro_status=1,pro_type=i).order_by('-pro_volume')[0:12])
        products.append((i,products1))
    return products
