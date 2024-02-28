# serializers.py
# serializers.py
from rest_framework import serializers
from .models import Category, Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'uploaded_at']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'quantity', 'brand', 'size', 'color', 'material', 'gender', 'discount_price', 'tags', 'availability', 'featured', 'product_code', 'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        images_data = self.context.get('request').FILES
        product = Product.objects.create(**validated_data)
        for image_data in images_data.getlist('images'):
            ProductImage.objects.create(product=product, image=image_data)
        return product

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']

