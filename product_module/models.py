from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()