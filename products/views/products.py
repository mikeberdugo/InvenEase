from django.shortcuts import render
from .forms.productsform import Productsform
from .forms.categoryform import Categoryform
from common.models import Company,Product


def products(request):
    company_id = request.session.get('company', None) 
    if company_id:
        company = Company.objects.get(id=company_id)
    
    if request.method == 'POST':
        form = Productsform(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            stock_quantity = form.cleaned_data['stock_quantity']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            
            # Crear un nuevo producto y guardarlo en la base de datos
            Product.objects.create(
                name=name,
                
                description=description,
                stock_quantity=stock_quantity,
                company = company,
                price = price ,
                quantity=quantity,
            )
    else : 
        form = Productsform()
        form2 = Categoryform()
    product = Product.objects.filter(company_id=company_id)
    
    
    return render(request, './products/products.html',
                    {
                    'product':product,
                    'form':form,
                    'form2':form2,
                    
                    })    
    

    

    # name = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    # description = models.TextField(verbose_name="Descripción")
    # stock_quantity = models.PositiveIntegerField(verbose_name="Cantidad en Stock")
    # price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    # location = models.CharField(max_length=100, verbose_name="Ubicación")
    # sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")  # Stock Keeping Unit
    # barcode = models.CharField(max_length=100, blank=True, verbose_name="Código de Barras")
    # supplier = models.CharField(max_length=150, blank=True, verbose_name="Proveedor")
    # purchase_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Compra")
    # expiration_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Expiración")
    # weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Peso")
    # dimensions = models.CharField(max_length=100, blank=True, verbose_name="Dimensiones")  # e.g., 10x10x10 cm
    # condition = models.CharField(max_length=50, choices=[('new', 'Nuevo'), ('used', 'Usado'), ('refurbished', 'Reacondicionado')], default='new', verbose_name="Condición")
    # notes = models.TextField(blank=True, verbose_name="Notas")

    # # Campos adicionales
    # manufacturer = models.CharField(max_length=150, blank=True, verbose_name="Fabricante")
    # model_number = models.CharField(max_length=100, blank=True, verbose_name="Número de Modelo")
    # warranty_period = models.PositiveIntegerField(null=True, blank=True, verbose_name="Período de Garantía (meses)")
    # reorder_level = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nivel de Reorden")
    # safety_stock = models.PositiveIntegerField(null=True, blank=True, verbose_name="Stock de Seguridad")
    # last_restock_date = models.DateField(null=True, blank=True, verbose_name="Última Fecha de Reabastecimiento")
    # shipping_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Peso de Envío")
    # handling_instructions = models.TextField(blank=True, verbose_name="Instrucciones de Manejo")
    # product_url = models.URLField(blank=True, verbose_name="URL del Producto")
    # batch_number = models.CharField(max_length=100, blank=True, verbose_name="Número de Lote")
    # production_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Producción")
    # import_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Importación")
    # expiration_warning_days = models.PositiveIntegerField(null=True, blank=True, verbose_name="Días de Advertencia de Expiración")
    # barcode_type = models.CharField(max_length=50, choices=[('UPC', 'UPC'), ('EAN', 'EAN'), ('QR', 'QR')], blank=True, verbose_name="Tipo de Código de Barras")
    # product_image = models.ImageField(upload_to='product_images/', blank=True, verbose_name="Imagen del Producto")
    # safety_data_sheet = models.FileField(upload_to='safety_data_sheets/', blank=True, verbose_name="Hoja de Datos de Seguridad")
    # country_of_origin = models.CharField(max_length=100, blank=True, verbose_name="País de Origen")
    # import_duty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Derecho de Importación")
    # product_tag = models.CharField(max_length=100, blank=True, verbose_name="Etiqueta del Producto")
    # minimum_order_quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name="Cantidad Mínima de Pedido")
    # maximum_order_quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name="Cantidad Máxima de Pedido")
    # bulk_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio al por Mayor")
    # tax_code = models.CharField(max_length=100, blank=True, verbose_name="Código de Impuestos")
    # compliance_certifications = models.TextField(blank=True, verbose_name="Certificaciones de Cumplimiento")
    # product_source = models.CharField(max_length=100, blank=True, verbose_name="Fuente del Producto")