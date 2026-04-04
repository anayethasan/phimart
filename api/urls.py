from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoriesViewSet, ReviewViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoriesViewSet)

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product'
)
product_router.register('reviews', ReviewViewSet, basename='product-review')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
    # jodi amar onno  kono urls thake eirok example e dite parbo
    # path("example/")
]