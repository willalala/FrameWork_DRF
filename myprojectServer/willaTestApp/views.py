from django.shortcuts import render
from willaTestApp.models import Person
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import MultipleObjectsReturned

from django.http import HttpResponse
from willaTestApp import models
import uuid

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from willaTestApp.serializers import PersonSerializer
from willaTestApp.models import Person

from willaTestApp.serializers import UserSerializer
from willaTestApp.models import Users
from django.contrib.auth.hashers import make_password,check_password#密码存储加密和校验
# Create your views here.

####第一版
# def index(request):
#     # article_list=serializers.serialize('python',Article.objects.all())#选择所有数据
#     # return render(request,'index.html',{'article_list':json.dumps(article_list,cls=DjangoJSONEncoder)})
#     person_list=Person.objects.all()#选择所有数据
#     return render(request,'index.html',{'person_list':person_list})


####第二版
# def write_server(request):
#     data=json.loads(request.body)
#     data['id']=uuid.uuid4()#生成基于事件的uuid作为主键
#     models.Person.objects.create(**data)
#     res={
#         'success':True
#     }
#     return HttpResponse(json.dumps(res),content_type='application/json')

# def read_server(request):
#     name=request.GET['name']
#     # data=serializers.serialize('python',models.Person.objects.all())
#     data=serializers.serialize('python',models.Person.objects.filter(name=name))
#     res={
#         'success':True,
#         'data':data
#     }
#     return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')


####第三版
class PersonViewSet(viewsets.ModelViewSet):
    #方法1：由rest framework进行get、post与数据的关联

    # queryset=Person.objects.all()
    # serializer_class=PersonSerializer
    
    #方法2：由手动定义get、post等各种方法

    #@action 是DRF(django rest framework)提供的装饰器，用于在视图集（ViewSet获ModelViewSet）中定义额外的动作
    #这些动作可以是自定义的http方法或路径

    #def 是python内置关键字，用于定义函数或者方法

    @action(detail=False,methods=['post'])
    def new_person(self,request):
        data=json.loads(request.body)
        data['id']=uuid.uuid1()
        Person.objects.create(**data)
        res={
            'success':True,
            'data':data
        }
        return Response(res)
    
    @action(detail=False,methods=['get'])
    def all_person(self,request):
        name=request.GET['name']
        if name=='':
            data=PersonSerializer(Person.objects.all(),many=True).data
        else:
            data=serializers.serialize('python',models.Person.objects.filter(name=name))
        # data=PersonSerializer(Person.objects.all(),many=True).data
        res={
            'success':True,
            'data':data
        }
        return Response(res)
    @action(detail=False,methods=['delete'])
    def delete_person(self,request):
        name=request.GET['name']
        if Person.objects.filter(name=name).exists():
            try:
                data=Person.objects.get(name=name)
            except Person.DoesNotExist:
                print("No matching name")
            except MultipleObjectsReturned:
                data=Person.objects.filter(name=name).first()
            data.delete()
        res={
            'success':True,
            'data':PersonSerializer(Person.objects.all(),many=True).data
        }
        return Response(res)
    @action(detail=False,methods=['patch'])
    def edit_person(self,request):
        nametemp=json.loads(request.body)
        name=nametemp['name']
        if Person.objects.filter(name=name).exists():
            try:
                data=Person.objects.get(name=name)
            except Person.DoesNotExist:
                print("No matching name")
            except MultipleObjectsReturned:
                data=Person.objects.filter(name=name).first()
            serializer=PersonSerializer(data,data=request.data,partial=True)#针对这一条数据修改数据库中的data
            if serializer.is_valid():
                serializer.save()
        res={
            'success':True,
            'data':PersonSerializer(Person.objects.all(),many=True).data
        }
        return Response(res)    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UserSerializer

    @action(detail=False,methods=['post'])
    def register(self,request):
        data=json.loads(request.body)
        #注册用户名校验
        user=Users.objects.filter(username=data['username'])
        if len(user):
            res={
                'success':False,
                'mess':'用户名已注册'
            }
            return Response(res)
        
        data['id']=uuid.uuid1()
        data['password']=make_password(data['password'])#Django 默认使用 PBKDF2 算法
        #可以通过修改 settings.py 文件中的 PASSWORD_HASHERS 设置来更改默认算法
        Users.objects.create(**data)
        res={
            'success':True
        }
        return Response(res)
    
    @action(detail=False,methods=['post'])
    def login(self,request):
        data=json.loads(request.body)
        filter_user=Users.objects.filter(username=data['username'])
        if not len(filter_user):
            res={
                'success':False,
                'mess':'用户名未注册'
            }
            return Response(res)
        user=UserSerializer(filter_user,many=True).data[0]
        check_pass_result=check_password(data['password'],user['password'])
        if not check_pass_result:
            res={
                'success':False,
                'mess':'密码错误'
            }
            return Response(res)
        res={
            'success':True,
            'data':user
        }
        return Response(user)
    
    @action(detail=False,methods=['get'])
    def all_users(self,request):
        users=UserSerializer(Users.objects.all(),many=True).data
        res={
            'success':True,
            'data':users
        }
        return Response(res)

    @action(detail=False,methods=['patch'])
    def edit_users(self,request):
        data=json.loads(request.body)#data和request.data的效果基本一样
        filter_user_QuerySet=Users.objects.filter(username=data['username'])#QuerySet类型
        if not len(filter_user_QuerySet):
            res={
                'success':False,
                'mess':'用户名不存在'
            }
            return Response(res)
        filter_user_Object=Users.objects.get(username=data['username'])
        data['password']=make_password(data['password'])
        serializer=UserSerializer(filter_user_Object,data=data,partial=True)#针对这一条数据修改数据库中的data
        if serializer.is_valid():#You must call `.is_valid()` before calling `.save()`
            serializer.save()
            res={
                'success':True,
                'data':UserSerializer(Users.objects.all(),many=True).data
            }
            return Response(res)
        else:
            res={
                'success':True,
                'mess':'serial is not valid',
                'data':request.data,
                'detail':serializer.errors
            }
            print(serializer.errors)
            return Response(res)
    
    @action(detail=False,methods=['delete'])
    def delete_users(self,request):
        name=request.GET['username']
        filter_user=Users.objects.filter(username=name)
        if not len(filter_user):
            res={
                'success':False,
                'mess':'用户名不存在'
            }
            return Response(res)
        filter_user.delete()
        res={
            'success':True,
            'data':UserSerializer(Users.objects.all(),many=True).data
        }
        return Response(res)

# GET：获取数据，使用 params 传递查询参数。
# POST：提交数据，使用请求体传递数据。
# PATCH：部分更新资源，使用请求体传递要更新的数据。
# DELETE：删除资源，通常在 URL 中指定资源 ID。