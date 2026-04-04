from django.urls import path
from products import views

urlpatterns = [
    # path('', views.view_products, name='product-list'), 
    path('', views.ProductList.as_view(), name='product-list'), 
    # path('<int:id>/', views.view_specific_product, name='specific-product' ),
    path('<int:pk>/', views.ProductDetails.as_view(), name='specific-product' ),
]