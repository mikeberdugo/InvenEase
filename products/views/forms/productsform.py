from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit ,HTML
from django.core.validators import MinValueValidator

UNIT_CHOICES = [
    ('', '----'),
    ('unit', 'Unit - u'),
    ('meter', 'Meter - m'),
    ('liter', 'Liter - l'),
    ('kg', 'Kilogram - kg'),
    ('box', 'Box - box'),
    ('piece', 'Piece - pc'),
    ('set', 'Set - set'),
    ('roll', 'Roll - roll'),
    ('bag', 'Bag - bag'),
    ('carton', 'Carton - carton'),
    ('pack', 'Pack - pack'),
    ('dozen', 'Dozen - doz'),
    ('case', 'Case - case'),
    ('barrel', 'Barrel - barrel'),
    ('gallon', 'Gallon - gal'),
    ('ounce', 'Ounce - oz'),
    ('pound', 'Pound - lb'),
    ('square_meter', 'Square meter - m²'),
    ('cubic_meter', 'Cubic meter - m³'),
    ('kilometer', 'Kilometer - km'),
    ('centimeter', 'Centimeter - cm'),
    ('millimeter', 'Millimeter - mm'),
    ('inch', 'Inch - in'),
    ('foot', 'Foot - ft'),
    ('yard', 'Yard - yd')
]




class Productsform(forms.Form):
    
    name = forms.CharField(
        label='Product Name', 
        widget=forms.TextInput(attrs={'placeholder': 'Product Name','class': 'form-control form-control-solid'}), 
        max_length=150
    )
    category = forms.CharField(
        label='Category', 
        widget=forms.TextInput(attrs={'placeholder': 'Product Category','class': 'form-control form-control-solid'}), 
    )
    
    price = forms.IntegerField(
        label='Price', 
        widget=forms.NumberInput(attrs={'placeholder': 'Available Quantity','class': 'form-control form-control-solid'}), 
        validators=[MinValueValidator(0)]

    )
    
    description = forms.CharField(
        label='Description', 
        widget=forms.Textarea(attrs={'rows': 3,'class': 'form-control form-control-solid'})
    )
    stock_quantity = forms.IntegerField(
        label='Stock Quantity', 
        widget=forms.NumberInput(attrs={'placeholder': 'Available Quantity','class': 'form-control form-control-solid'}), 
    )
    
    quantity =  forms.ChoiceField(
        choices=UNIT_CHOICES,
        label='unit quantity',
        widget=forms.Select(attrs={'placeholder': 'sd', 'class': 'form-select form-select-solid'})
    )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'products-form'
        self.helper.label_class = 'col-form-label custom-label'
        self.helper.field_class = 'col-sm-12'
        self.helper.layout = Layout(
            Row(
                
                Column('name' , css_class='form-group mb-0'),
                Column('category', css_class='form-group mb-0'),
                HTML('''
                        <button class="btn btn-icon btn-info" type="button" data-bs-stacked-modal="#kt_modal_stacked_2" >
                            <i class="fa-solid fa-plus"></i>
                        </button>

                '''),
                css_class='row'
            ),
            
            Row(
                Column('description', css_class='form-group mb-0'),
                css_class='row'
            ),
            Row(
                Column('price', css_class='form-group mb-0'),
                css_class='row'
            ), 
            Row(
                Column('stock_quantity', css_class='form-group mb-0'),
                Column('quantity', css_class='form-group mb-2'),
                css_class='row'
            ),            
        )
