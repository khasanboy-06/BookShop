from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE =(
        ('client','client'),
        ('seller','seller'),
        ('admin','admin'),
    )
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    jobs = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=100,choices=USER_ROLE,default="client")

    def str(self):
        return self.first_name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        return self.price * self.quantity
    

class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.product.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    image = models.ImageField(upload_to='client_image', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.first_name
    

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')

    def __str__(self):
        return self.user.first_name