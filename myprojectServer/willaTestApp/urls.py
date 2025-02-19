from willaTestApp import views
from willaTestApp.views import PersonViewSet
from django.conf.urls import include
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

from willaTestApp.views import UserViewSet

router=DefaultRouter()

router.register(r'',PersonViewSet,basename="person")
router.register(r'user',UserViewSet,basename="user")
urlpatterns=[
    url('',include(router.urls))
]
# 问题是因为在注册视图集时使用了相同的空字符串 '' 作为基础 URL 模式。
# Django REST Framework 的 DefaultRouter 不支持为多个视图集注册相同的 URL 前缀。
# 这会导致后面的注册覆盖前面的，从而使得部分路由失效。