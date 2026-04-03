from django.urls import path
from products import views

urlpatterns = [
    # path('', views.view_categories, name='categories-list'),
    path('', views.CategoriesList.as_view(), name='categories-list'),
    # path('<int:pk>/', views.view_specific_categories, name='view-specific-category'),
    path('<int:pk>/', views.CategoriesDetails.as_view(), name='view-specific-category'),
]