from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product', null=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    price = models.FloatField()
    quantity = models.IntegerField(default=0, null=True, blank=True)
    detail = models.TextField(max_length=1000, blank=False)
    digital =  models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name
    
class Favorites(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_favorite = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()   
        return sum([item.quantity for item in orderitems])
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()   
        return sum([item.get_total for item in orderitems])

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order =models.ForeignKey(Order,  on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price *  self.quantity
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order =models.ForeignKey(Order,  on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    cyti = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=15, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class carousel(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title