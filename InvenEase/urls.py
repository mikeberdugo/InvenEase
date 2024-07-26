from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(('authentication.urls', 'login'))),
    # path('boards/', include(('shared_boards.urls', 'boards'))),
    # path('boards/accounts/', include(('accounts.urls', 'accounts'))), ## eliminar despues 
    # path('boards/patrimony/', include(('patrimony.urls', 'patrimony'))),
    # path('boards/shopping/', include(('shopping.urls', 'shopping'))),
    # path('boards/income/', include(('income.urls', 'income'))),
]