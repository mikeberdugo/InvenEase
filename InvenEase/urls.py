from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('boards/', include(('shared_boards.urls', 'boards'))),
    # path('boards/accounts/', include(('accounts.urls', 'accounts'))), ## eliminar despues 
    # path('boards/patrimony/', include(('patrimony.urls', 'patrimony'))),
    # path('boards/shopping/', include(('shopping.urls', 'shopping'))),
    # path('boards/income/', include(('income.urls', 'income'))),
]

urlpatterns += i18n_patterns(
    # incluimos el fichero de urls de la aplicación web
    path('', include(('authentication.urls', 'login'))),
    path('', include(('products.urls', 'products'))),
)