from django.shortcuts import render
from django.contrib.auth.models import User
from .serialiser import UserSerializer,EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class EmpView(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()


