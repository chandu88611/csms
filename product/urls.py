# product/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/images/<int:pk>/', views.ProductImageDeleteView.as_view(), name='product-image-delete'),
]
