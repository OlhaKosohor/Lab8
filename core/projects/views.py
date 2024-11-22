from django.shortcuts import render
from .models import Client, Product, Sale


def clients_view(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})


def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def sales_view(request):
    sales = Sale.objects.all()
    return render(request, "sales.html", {"sales": sales})


def index(request):
    return render(request, "index.html")
