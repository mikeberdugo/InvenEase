from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.db import models



class AstradUser(AbstractUser):
    # Opciones para el campo de rol del usuario
    ROLES_CHOICES = [
        ('Admin', 'Admin'),  # Administrador del sistema con acceso total
        ('Manager', 'Manager'),  # Manager de inventario con permisos para gestionar inventarios
        ('Employee', 'Employee'),  # Empleado con acceso limitado a ciertas funciones
    ]

    # Opciones para el campo de género del usuario
    GENDER_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]

    # Relación con la empresa a la que pertenece el usuario
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company_employees',null=True,blank=True)  
    
    # Campo para indicar si la membresía está pagada
    membership_paid = models.BooleanField(default=False, help_text="Indica si la membresía está pagada.")
    
    # Campo para la fecha de expiración de la membresía
    membership_expiry_date = models.DateField(null=True, blank=True, help_text="Fecha de expiración de la membresía.")
    
    # Campo para almacenar el rol del usuario (Admin, Manager, Employee)
    role = models.CharField(max_length=50, choices=ROLES_CHOICES, default='Employee', help_text="Rol del usuario en el sistema.")
    
    # Campo para la fecha de nacimiento del usuario
    birth_date = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario.")
    
    # Campo para el género del usuario
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, help_text="Género del usuario.")
    
    
    # Campo para la nacionalidad del usuario
    nationality = models.CharField(max_length=100, null=True, blank=True, help_text="Nacionalidad del usuario.")
    
    # Campo para la imagen de perfil del usuario
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, help_text="Imagen de perfil del usuario.")
    
    # Campo para un código único del usuario
    cdunico = models.CharField(max_length=7, unique=True, editable=False, blank=True, help_text="Código único del usuario.")

    def save(self, *args, **kwargs):
        # Generar un código único si no existe
        if not self.cdunico:
            self.cdunico = self.generate_unique_cdunico()
        super().save(*args, **kwargs)

    def generate_unique_cdunico(self):
        while True:
            cdunico = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            if not AstradUser.objects.filter(cdunico=cdunico).exists():
                return cdunico
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = 'astrad_user'


#* empresa 

class Company(models.Model):
    # Nombre único de la empresa
    name = models.CharField(max_length=255, unique=True, help_text="Nombre de la empresa.")  
    # Dirección física de la empresa
    address = models.CharField(max_length=255, help_text="Dirección de la empresa.")  
    # Ciudad donde se encuentra la empresa
    city = models.CharField(max_length=100, help_text="Ciudad donde se encuentra la empresa.") 
    # País donde se encuentra la empresa
    country = models.CharField(max_length=100, help_text="País donde se encuentra la empresa.")  
    # Número de teléfono opcional de la empresa
    phone_number = models.CharField(max_length=20, null=True, blank=True, help_text="Número de teléfono de la empresa.")  
    # Correo electrónico opcional de la empresa
    email = models.EmailField(null=True, blank=True, help_text="Correo electrónico de la empresa.")  
    # URL del sitio web opcional de la empresa
    website = models.URLField(null=True, blank=True, help_text="Sitio web de la empresa.")  
    # Fecha en que se creó el registro de la empresa
    creation_date = models.DateField(auto_now_add=True, help_text="Fecha de creación de la empresa.")  
    # Categoría de la empresa
    category = models.CharField(max_length=50, help_text="Categoría de la empresa.")
    
    def __str__(self):
        return self.name  # Representación de cadena del objeto de la empresa

    class Meta:
        verbose_name = "Company"  # Nombre en singular en la administración
        verbose_name_plural = "Companies"  # Nombre en plural en la administración
        db_table = 'company'




#* Productos 

class Category(models.Model):
    # Nombre de la categoría de productos
    name = models.CharField(max_length=255, unique=True)
    # Descripción opcional de la categoría
    description = models.TextField(blank=True, null=True)
    # Relación con la empresa a la que pertenece la categoría.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_categories')  

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'category'
    

class Product(models.Model):
    # Nombre del producto
    name = models.CharField(max_length=255)
    # Categoría a la que pertenece el producto (relación con Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')  
    # SKU (Stock Keeping Unit) único para identificar el producto
    sku = models.CharField(max_length=100, unique=True)
    # Descripción opcional del producto
    description = models.TextField(blank=True, null=True)
    # Precio del producto
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Cantidad en stock del producto
    stock_quantity = models.PositiveIntegerField()
    # unidad de stock del producto
    quantity = models.CharField(max_length=100 )
    # Fecha de creación del registro (automáticamente se establece al crear el producto)
    created_at = models.DateTimeField(auto_now_add=True)
    # Fecha de la última actualización del registro (se actualiza automáticamente)
    updated_at = models.DateTimeField(auto_now=True)
    # Relación con la empresa a la que pertenece el producto.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_products')  
    
    barcode = models.CharField(max_length=50, unique=True, blank=True, null=True) 
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = 'product'

#* Inventory 

class InventoryMovement(models.Model):
    # Tipo de movimiento: 'IN' para entrada y 'OUT' para salida
    MOVEMENT_TYPE_CHOICES = [
        ('IN', 'In'),
        ('OUT', 'Out'),
    ]
    
    # Producto afectado por el movimiento
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_inventory_movements')  
    # Tipo de movimiento (entrada o salida)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE_CHOICES)
    # Cantidad del movimiento
    quantity = models.PositiveIntegerField()
    # Fecha y hora del movimiento
    date = models.DateTimeField(auto_now_add=True)
    # Nota adicional sobre el movimiento
    note = models.TextField(blank=True, null=True)
    # Relación con la empresa a la que pertenece el movimiento de inventario.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_inventory_movements')  
    
    def __str__(self):
        return f'{self.product.name} - {self.movement_type} - {self.quantity}'
    
    class Meta:
        verbose_name = "Inventory Movement"
        verbose_name_plural = "Inventory Movements"
        db_table = 'inventory_movement'
    
#* Suppliers

class Supplier(models.Model):
    # Nombre del proveedor
    name = models.CharField(max_length=255)
    # Información de contacto del proveedor (opcional)
    contact_info = models.TextField(blank=True, null=True)
    # Dirección del proveedor (opcional)
    address = models.TextField(blank=True, null=True)
    # Teléfono del proveedor (opcional)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # Correo electrónico del proveedor (opcional)
    email = models.EmailField(blank=True, null=True)
    # Relación con la empresa a la que pertenece el proveedor.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_suppliers')  

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        db_table = 'supplier'
    
    
#* Purchase Orders

class PurchaseOrder(models.Model):
    # Proveedor asociado con la orden de compra
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_purchase_orders')  
    # Fecha de creación de la orden de compra
    order_date = models.DateTimeField(auto_now_add=True)
    # Estado de la orden de compra (Pendiente, Completada, Cancelada)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')])
    # Monto total de la orden de compra
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Relación con la empresa a la que pertenece la orden de compra.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_purchase_orders')  
    
    def __str__(self):
        return f'Order {self.id} - {self.status}'
    
    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
        db_table = 'purchase_order'

class PurchaseOrderItem(models.Model):
    # Orden de compra a la que pertenece este ítem
    order = models.ForeignKey(PurchaseOrder, related_name='items', on_delete=models.CASCADE)
    # Producto que se está comprando
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Cantidad del producto en la orden
    quantity = models.PositiveIntegerField()
    # Precio del producto en la orden
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
    
    class Meta:
        verbose_name = "Purchase Order Item"
        verbose_name_plural = "Purchase Order Items"
        db_table = 'purchase_order_item'

#* Bar Codes     
class Barcode(models.Model):
    # Producto asociado con este código de barras
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_barcode')  
    # Código de barras único del producto
    barcode = models.CharField(max_length=100, unique=True)
    # Relación con la empresa a la que pertenece el código de barras.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_barcodes')  

    def __str__(self):
        return self.barcode
    
    class Meta:
        verbose_name = "Barcode"
        verbose_name_plural = "Barcodes"
        db_table = 'barcode'
    

#*  Audit

class AuditLog(models.Model):
    # Acción realizada (Crear, Actualizar, Eliminar)
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    # Usuario que realizó la acción
    user = models.ForeignKey(AstradUser, on_delete=models.SET_NULL, null=True, related_name='user_audit_logs')  
    # Tipo de acción realizada
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    # Nombre del modelo afectado por la acción
    model_name = models.CharField(max_length=255)
    # ID del objeto afectado
    object_id = models.PositiveIntegerField()
    # Fecha y hora en la que se realizó la acción
    change_date = models.DateTimeField(auto_now_add=True)
    # Descripción del cambio realizado
    change_description = models.TextField()
    # Relación con la empresa a la que pertenece el registro de auditoría.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_audit_logs')  
    
    
    def __str__(self):
        return f'{self.action} - {self.model_name} - {self.change_date}'
    
    class Meta:
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"
        db_table = 'audit_log'

