from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Firstname = models.CharField(max_length=100,null=True,blank=True)
    Lastname = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class SignupDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Re_password = models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Productname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_price = models.IntegerField(null=True,blank=True)

class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)
    Totalprice = models.IntegerField(null=True,blank=True)