from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    slug = models.SlugField()
    
 
    def __str__(self):
        return self.name


class Item(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Description of the item") 
    discount_price = models.FloatField(blank = 'True', null = 'True')
    Gender = (
        ('M', 'Male'),  
        ('F', 'Female'),  
        ('MF', 'Male and Female')   
        
)
    gender = models.CharField(default='M',max_length=2, choices = Gender)
    Stuff = (
        ('S','Shoes'),
        ('H','Shirts'),
        ('I','Shorts'),
        ('T','Trousers'),
        ('P','Pyjamas')
    )

    #cat = models.ManyToManyField(Category, null="True", blank = "True")
    category = models.CharField(default='Pick a category',max_length=20, choices = Stuff)
    image1 = models.ImageField(default='default.jpeg', upload_to='product_pics')
    image2 = models.ImageField(default='default.jpeg', upload_to='product_pics')
    image3 = models.ImageField(default='default.jpeg', upload_to='product_pics')
    image4 = models.ImageField(default='default.jpeg', upload_to='product_pics')
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("item-detail", kwargs={
           'slug':self.slug
        })
    
    def get_add_to_cart(self):
        return reverse("add-to-cart", kwargs={
           'slug':self.slug
        })
    
    def get_remove_from_cart(self):
        return reverse("remove-from-cart", kwargs={
           'slug':self.slug 
        })
    

     
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
    def get_item_total(self):
        return self.quantity * self.item.price
    
    def get_item_discount(self):
        return self.quantity * self.item.discount_price
    
    def get_amount_saved(self):
        return self.get_item_total() - self.get_item_discount()
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_item_discount()
        return self.get_item_total()
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class BillingAddress(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     street_address = models.CharField(max_length=100)
     home_address = models.CharField(default = '121 Lubowa',max_length=100)
     country = models.CharField(max_length=100)
     zip = models.CharField(max_length=100)

     def __str__(self):
         return self.user.username

class ItemReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    review = models.TextField(default="Review of the item")
    phone_number = models.FloatField()

    def __str__(self):
        return f'{self.user.username} review for {self.item.Item.slug}'

class Variation(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    colors = {
        ('R','Red'),
        ('B','Black'),
        ('P','Pink'),
        ('Y','Yellow')
    }
    color = models.CharField(max_length=2,choices= colors, default='R')
    sizes = {
        ('L','Large'),
        ('M','Medium'),
        ('S','Small')
    }
    size = models.CharField(default="M", choices = sizes, max_length=2)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(default='product.image1', upload_to='product_pics')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


    
