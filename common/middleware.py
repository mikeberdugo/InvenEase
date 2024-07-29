from django.utils.deprecation import MiddlewareMixin

class CompanyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            if hasattr(user, 'company'):
                request.session['company_id'] = user.company.id
                request.session['company_name'] = user.company.name
                
                
                