from rest_framework import serializers
from willaTestApp.models import Person
from willaTestApp.models import Users

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('id','name','age','time')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','username','password','time')