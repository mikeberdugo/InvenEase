from django.urls import path

from .views import login 
from .views import index

urlpatterns = [
    path('', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('signup/', login.signup_view, name='signup'),
    path('index/', index.index, name='home'),
    
    
    # path('prueba/', views.prueba, name='prueba'),
]