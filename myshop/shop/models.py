from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cart(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    expired_in = models.IntegerField(default=60)

class CartItem(models.Model):
    cart = models.ForeignKey("shop.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField("shop.ProductCategory")

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)

class Order(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    products = models.ManyToManyField("shop.Product", through="shop.OrderItem")

class OrderItem(models.Model):
    order = models.ForeignKey("shop.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Payment(models.Model):
    order = models.OneToOneField("shop.Order", on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Paymentitem(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    order_item = models.OneToOneField("shop.OrderItem", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class PaymentMethod(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    class Method(models.TextChoices):
        QR = 'QR'
        CREDIT = 'CREDIT'
    method = models.CharField(max_length=10, choices=Method.choices, default=Method.CREDIT)

    price = models.DecimalField(max_digits=10, decimal_places=2)





    
    
