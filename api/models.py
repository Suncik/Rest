from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    company_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.product_name
