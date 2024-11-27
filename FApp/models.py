from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Categoryname = models.CharField(max_length=100,null=True,blank=True)
    Categoryimage = models.ImageField(upload_to="categoryImage",null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)



class ProductDb(models.Model):
    Selectproduct = models.CharField(max_length=100,null=True,blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Mrp = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Manufactured = models.CharField(max_length=100, null=True, blank=True)
    Productimage1 = models.ImageField(upload_to="Productimage", null=True, blank=True)
    Productimage2 = models.ImageField(upload_to="Productimage",null=True, blank=True)
    Productimage3 = models.ImageField(upload_to="Productimage", null=True, blank=True)

class BlogDb(models.Model):
    Blogimage = models.ImageField(upload_to="blogimage",null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)