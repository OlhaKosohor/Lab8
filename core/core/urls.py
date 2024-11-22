from django.contrib import admin
from django.urls import path

from projects import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clients/", views.clients_view, name="clients_list"),
    path("products/", views.products_view, name="products_list"),
    path("sales/", views.sales_view, name="sales_list"),
    path("", views.index),
]
