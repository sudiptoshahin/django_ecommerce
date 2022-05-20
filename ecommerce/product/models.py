from unicodedata import category
import uuid
from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=100)
    discount_price = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField()
    # review
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    # pictures
    category = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)

