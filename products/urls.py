from django.urls import path
from .views import products

urlpatterns = [
    path('products', products.products, name='products'),
    
    
    
    
    # path('prueba/', views.prueba, name='prueba'),
]