from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "brand", "slug"]
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(models.Product, ProductAdmin)