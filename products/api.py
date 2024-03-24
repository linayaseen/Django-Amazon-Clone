from rest_framework import generics
from.models import Product, Brand,Review,ProductImages
from .import serializers


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=serializers.ProductListSerializer
    
    
class ProductDetailAPI(generics.RetriveAPIView):
    queryset = Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer
    
    
class BrandListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=serializers.BrandListSerializer
    
    
class BrandDetailAPI(generics.RetriveAPIView):
    queryset = Product.objects.all()
    serializer_class=serializers.BrandDetailSerializer