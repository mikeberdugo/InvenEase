from django import forms
from common.models import AstradUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from components.frases import  frases_error_usuario , frases_error_email

import random 




class CompanyForm(forms.Form):
    name = forms.CharField(
        #label='Nombre del items',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del items'}),
    )


    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico de la empresa'}),
    )
    
    category = forms.ChoiceField(
        label='Categoría',
        widget=forms.Select(attrs={'data-control': 'select2'}),
        
    )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                Column('category', css_class='form-group mb-0'),
                css_class='row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-light-success w-100')
        )
