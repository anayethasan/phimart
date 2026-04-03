from django.urls import path, include

urlpatterns = [
    path("products/", include('products.product_urls')),
    path("categories/", include('products.categories_urls')),
]