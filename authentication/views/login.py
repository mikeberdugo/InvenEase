from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
import random

from common.models import AstradUser,Company
from authentication.forms.loginform import LoginForm
from authentication.forms.signupform import SignupForm
from authentication.forms.companyform import CompanyForm
from components.frases import (
    frases_falla_login, frases_restablecimiento, frases_creacion_cuenta,
    frases_bienvenida, frases_error_contrasena, frases_inicio_sesion,
    frases_cancelacion
)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('login:home')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    request.session['company'] = user.company.id
                    
                    return redirect('login:home')  
                else:
                    frase_aleatoria = random.choice(frases_falla_login)
                    messages.error(request, frase_aleatoria)
        else:
            form = LoginForm()

        reinstatement = random.choice(frases_restablecimiento)
        Create = random.choice(frases_creacion_cuenta)
    return render(request, './authentication/login.html',{
        'form':form,
        'Create': Create ,
        'reinstatement' : reinstatement,
        })
    
    

def logout_view(request):
    logout(request)
    return redirect('login:login')  # Redirigir a la página de inicio de sesión después de cerrar sesión




def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                if AstradUser.objects.filter(username=username).exists():
                    messages.error(request, '¡Ups! Parece que este nombre de usuario ya ha sido tomado. ¿Podrías intentar con otro?')
                else:
                    new_company = Company(
                        name= form.cleaned_data['name'] ,
                        email= form.cleaned_data['emailc'],
                        category= form.cleaned_data['category'],
                    )
                    
                    new_company.save()
                    
                    user = AstradUser.objects.create_user(
                        username=username, 
                        email=email, 
                        password=password1,
                        company = new_company ,
                        role = 'Manager',
                        )
            
                    login(request, user)
                    frase_aleatoria = random.choice(frases_bienvenida)
                    messages.success(request, frase_aleatoria)
                    request.session['company'] = user.company.id
                    return redirect('login:home')  # Redirigir a la página de inicio después de registrarse
            else:
                frase_aleatoria = random.choice(frases_error_contrasena)
                messages.error(request, frase_aleatoria)
    else:
        form = SignupForm()
    login_f = random.choice(frases_inicio_sesion)
    return render(request, './authentication/signup.html', 
                    {'form': form,
                    'login_f':login_f,
                    })
    
    
def company_view_login(request):
    
    form = CompanyForm()
    cancel = random.choice(frases_cancelacion)
    
    return render(request, './authentication/company.html', 
                    {'form': form,
                    'cancel':cancel,
                    
                    })
    
    
