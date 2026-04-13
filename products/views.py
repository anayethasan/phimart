# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Category, Review
from products.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# from rest_framework.views import APIView
# from rest_framework.mixins import CreateModelMixin, ListModelMixin
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from products.filters import ProductFilter 
from products.pagination import DefaultPagination
# from rest_framework.permissions import IsAdminUser, AllowAny
from api.permissions import IsAdminOrReadOnly
from products.permissions import IsReviewAuthorOrReadOnly


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'updated_at']
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [FullDjangoModelPermission]
    
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()] nijer moto kore permission classes baniye nea
    

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10:
            return Response({'message': "Product with stock more then 10 could not be deleted"})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CategoriesViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.annotate(
        product_count=Count('products')).all()
    serializer_class = CategorySerializer
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}