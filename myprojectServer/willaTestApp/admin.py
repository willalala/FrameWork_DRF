#在此处声明后，能在后台管理系统中管理创建的表
from django.contrib import admin
from willaTestApp.models import Person
from willaTestApp.models import Users
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_DISPLAY=['id','name','age','time']

class UserAdmin(admin.ModelAdmin):
    list_DISPLAY=['id','username','password','time']

admin.site.register(Person,PersonAdmin)
admin.site.register(Users,UserAdmin)