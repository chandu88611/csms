# views.py
from rest_framework import generics
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer,ProductImageSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        # Delete associated images when a product is deleted
        ProductImage.objects.filter(product=instance).delete()
        instance.delete()

class ProductImageDeleteView(generics.DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
