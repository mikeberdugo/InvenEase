from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}), max_length=150)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group mb-0'),
                css_class='row text-center'
            ),
            Row(
                Column('password', css_class='form-group mb-0'),
                css_class='row text-center'
            ),
            Submit('submit', 'Ingresar', css_class='btn btn-light-success w-100')
        )
