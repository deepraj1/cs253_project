from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django import forms


# Create your models here.


#class Department(models.Model):
    #Department_Name = models.CharField(max_length=100,unique=True)

#department changes are to be done

class Student(models.Model):
    CheckChoices=[
        ('Yes','Yes'),
        ('No','No'),
    ]
    number = models.IntegerField(primary_key=True,default=0)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    check_box = models.CharField(
        max_length=100,
        choices=CheckChoices,
        default='No',
        )
    discrepency = models.CharField(
        max_length=10,
        choices=CheckChoices,
        default='No'
    )
    comment = models.CharField(max_length=1000,default="")


class Profile(models.Model):
    Role_Choices = [
        ('Ta','Ta'),
        ('Manager','Manager'),
        ('Admin','Admin'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=Role_Choices,
        default='Ta'
        )
    start_No=models.IntegerField(default=0)
    end_No=models.IntegerField(default=0)

class Pending_Requests(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,blank=True)
    password=models.CharField(max_length=100)



