# admin.py (inside your product app directory)

from django.contrib import admin
from .models import Product, ProductImage,Category

# Define inline admin class for ProductImage
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display for uploading additional images

# Define admin class for Product
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # Include ProductImageInline in Product admin page
    list_display = ['name', 'category', 'price', 'quantity', 'availability']
    list_filter = ['category', 'availability']
    search_fields = ['name', 'category__name']  # Search by product name or category name
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
# Register Product and ProductImage with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
