from django import forms
from common.models import AstradUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from components.frases import  frases_error_usuario , frases_error_email
from components.choices import CATEGORY_CHOICES
import random 




class CompanyForm(forms.Form):
    name = forms.CharField(
        label='Nombre de la empresa',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de la empresa'}),
    )


    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico de la empresa'}),
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
