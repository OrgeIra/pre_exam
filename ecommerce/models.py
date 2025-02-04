from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    class RatingChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/products/')
    rating = models.PositiveIntegerField(choices=RatingChoice.choices, default=RatingChoice.ONE.value)
    shipping_costs = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.name

class Specification(BaseModel):
    processor = models.CharField(max_length=250)
    memory  = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    display = models.CharField(max_length=250)
    storage = models.CharField(max_length=250)
    graphics = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    finish = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} Specification'
 

