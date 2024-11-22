from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ("Юридична", "Юридична"),
        ("Фізична", "Фізична"),
    ]

    company_name = models.CharField(max_length=100)
    client_type = models.CharField(max_length=50, choices=CLIENT_TYPE_CHOICES)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("Готівковий", "Готівковий"),
        ("Безготівковий", "Безготівковий"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    delivery_needed = models.BooleanField()
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Продаж {self.product.product_name} до {self.client.company_name}"
