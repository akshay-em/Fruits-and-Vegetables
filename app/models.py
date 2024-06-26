from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product(models.Model):
    
    image=models.ImageField(upload_to='static/img',null=True,blank=True)
    category=models.CharField(max_length=50,null=True)
    product_name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True)
    price=models.IntegerField()


class customer(models.Model):
    customerid=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)

class feedback(models.Model):
    customername=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    message=models.CharField(max_length=500)

class order_details(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    housename=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    postcode=models.IntegerField()
    mobile=models.IntegerField()
    email=models.EmailField(max_length=100)
    ordernotes=models.CharField(max_length=200,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    product_name = models.CharField(max_length=255,default=0)
    oid= models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    approve=models.IntegerField(default=0) 
