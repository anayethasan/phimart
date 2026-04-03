from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data) #Deserializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data) #Deserializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_product(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        copy_of_product = product
        product.delete()
        serializer = ProductSerializer(copy_of_product)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        copy_of_product = product
        product.delete()
        serializer = ProductSerializer(copy_of_product)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

@api_view()
def view_categories(request):
    category = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(category, many=True)
    
    return Response(serializer.data)

class ViewCategories(APIView):
    def get(self, request):
        category = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view()
def view_specific_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    
    return Response(serializer.data)

class ViewSpecificCategories(APIView):
    def get(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def put(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        serializer = CategorySerializer(category, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    