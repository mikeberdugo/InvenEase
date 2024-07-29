from django.urls import path

from .views import products


urlpatterns = [
    path('products/', products.products_view, name='products'),
    # path('logout/', login.logout_view, name='logout'),
    # path('signup/', login.signup_view, name='signup'),
    # path('company/', login.company_view_login, name='company'),
    
    # path('index/', index.index, name='home'),
    
    
    # path('prueba/', views.prueba, name='prueba'),
]