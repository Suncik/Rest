from django.urls import path
from .views import (
    CategoryAPIView,
    SupplierAPIView,
    ProductAPIView,
    CategoryDetailAPIView
)

urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('suppliers/', SupplierAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
]


