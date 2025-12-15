from django.urls import path
from .views import category_api, supplier_api, product_api

urlpatterns = [
    path('categories/', category_api),
    path('suppliers/', supplier_api),
    path('products/', product_api),
]
