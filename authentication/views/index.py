from django.shortcuts import render
from common.models import AstradUser,Company
# Create your views here.

### index login 

def index(request):
    # Accede al id de la compañía desde la sesión
    #company = request.session.get('company', None)
    return render(request, './authentication/index.html')
