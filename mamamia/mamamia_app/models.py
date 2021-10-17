from django.db import models
from django.db.models.base import Model

# Create your models here.


class User(models.Model):
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    userFirstname = models.CharField(max_length=30)
    userLastname = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=50)
    userGender = models.BooleanField(max_length=1, choices=gender_choices)
    userPhone = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=100)
    userIsRegisteredOn = models.DateTimeField(auto_now_add=True)
    userIsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Admin(models.Model):
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    adminUsername = models.CharField(max_length=30)
    adminPassword = models.CharField(max_length=128)
    adminFirstname = models.CharField(max_length=30)
    adminLastname = models.CharField(max_length=30)
    adminEmail = models.CharField(max_length=50)
    adminGender = models.BooleanField(max_length=1, choices=gender_choices)
    adminPhone = models.CharField(max_length=20)
    adminAddress = models.CharField(max_length=100)
    adminIsRegisteredOn = models.DateTimeField(auto_now_add=True)
    adminIsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.adminUsername


class Products(models.Model):
    productName = models.CharField(max_length=30)
    productDetail = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductDetails(models.Model):
    productDesc = models.TextField()
    productIngredients = models.TextField()
    productAvatar = models.ImageField(upload_to='product_avatars/')
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productIsRegisteredOn = models.DateTimeField(auto_now_add=True)
    productIsAvailable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.productDesc)+': Rp.'+str(self.productPrice)


class OrderMethods(models.Model):
    AVAILABLE_METHODS = ((1, 'Dine in'), (2, 'Takeaway'))
    methodName = models.BooleanField(
        max_length=1, choices=AVAILABLE_METHODS, default=1)


class Orders(models.Model):
    userID = models.ForeignKey(to=User)
    productID = models.ForeignKey(to=Products)
    orderNote = models.CharField(max_length=30)
    orderMethod = models.ForeignKey(to=OrderMethods)
