from django.shortcuts import render
# Create your views here.

### index login 

def index(request):
    company_id = request.session.get('company_id')
    company_name = request.session.get('company_name')
    
    print(company_id)
    print(company_name)
    return render(request, './authentication/index.html')
