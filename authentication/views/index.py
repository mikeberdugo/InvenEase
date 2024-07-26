from django.shortcuts import render
# Create your views here.

### index login 

def index(request):
    
    return render(request, './authentication/index.html')
