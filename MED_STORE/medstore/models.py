from django.db import models
from django.contrib.auth.hashers import check_password
import datetime

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='pics')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=200 , default='')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
        
class Productview(models.Model):
    medname = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='pics')
    mrp = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    brand = models.CharField(max_length=50)
    shopname = models.CharField(max_length=50)
    about = models.TextField(max_length=200 , default='')

    @staticmethod
    def get_all_productviews():
        return Productview.objects.all()

class Catergory(models.Model):
    name = models.CharField(max_length=50)

class Customer(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    mobno = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)        

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
