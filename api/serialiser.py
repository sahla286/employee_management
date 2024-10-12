from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)

class EmployeeSerializer(serializers.ModelSerializer):
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields='__all__'