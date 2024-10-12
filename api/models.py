from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    image=models.ImageField(upload_to='images',null=True)
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    phn_no=models.BigIntegerField(max_length=10)
    email=models.EmailField()
    position=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    date_of_birth= models.DateField()
    salary=models.BigIntegerField()
