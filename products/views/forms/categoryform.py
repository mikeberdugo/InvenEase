from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit ,HTML
from django.core.validators import MinValueValidator



class Categoryform(forms.Form):
    
    name = forms.CharField(
        label='Category Name', 
        widget=forms.TextInput(attrs={'placeholder': 'Product Name','class': 'form-control form-control-solid'}), 
        max_length=150
    )
    
    description = forms.CharField(
        label='Description', 
        widget=forms.Textarea(attrs={'class': 'form-control form-control-solid'})
    )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'category-form'
        self.helper.label_class = 'col-form-label custom-label'
        self.helper.field_class = 'col-sm-12'
        self.helper.layout = Layout(
            Row(
                
                Column('name' , css_class='form-group mb-0'),
                css_class='row'
            ),
            
            Row(
                Column('description', css_class='form-group mb-0'),
                css_class='row'
            ),         
        )
