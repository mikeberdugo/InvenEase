from django import forms
from common.models import AstradUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from components.frases import  frases_error_usuario , frases_error_email
from components.choices import CATEGORY_CHOICES
import random 




class SignupForm(forms.Form):
    
    username = forms.CharField(
        label='Nombre de usuario', 
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}), 
        max_length=150
    )
    email = forms.EmailField(
        label='Correo electrónico', 
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'})
    )
    
    name = forms.CharField(
        label='Nombre de la empresa',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de la empresa'}),
    )


    emailc = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico de la empresa'}),
        required=False
    )
    
    category = forms.ChoiceField(
        label='Categoría',
        widget=forms.Select(attrs={'data-control': 'select2'}),
        choices=CATEGORY_CHOICES
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                Column('password1', css_class='form-group mb-0'),
                Column('password2', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                
                css_class='row'
            ),
            
            Row(
                Column('name', css_class='form-group mb-0'),
                css_class='row'
            ),
            
            Row(
                Column('emailc', css_class='form-group mb-0'),
                Column('category', css_class='form-group mb-0'),
                css_class='row'
            ),
            
            Submit('submit', 'Registrarse', css_class='btn btn-light-success w-100')
        )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Verificar si el nombre de usuario ya está tomado
        if AstradUser.objects.filter(username=username).exists():
            frase_aleatoria = random.choice(frases_error_usuario)
            self.add_error('username', frase_aleatoria)

        # Verificar si el correo electrónico ya está tomado
        if AstradUser.objects.filter(email=email).exists():
            frase_aleatoria = random.choice(frases_error_email)
            self.add_error('email', frase_aleatoria)
