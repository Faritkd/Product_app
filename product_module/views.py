from django.shortcuts import render
from django.views.generic import ListView
from product_module.models import Product


# Create your views here.


def product_list(request):
    products: Product = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "product_module/product_list.html", context)


def product_detail(request, slug):
    product = Product.objects.filter(slug=slug).first()
    context = {
        "product": product
    }
    return render(request, "product_module/product_detail.html", context)