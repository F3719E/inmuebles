from django.db import models

import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
'''
*********************************************************************
******************************* HITO ******************************** 
*********************************************************************
'''
# Create your models here.
class Persona(models.Model): 
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    correo      = models.EmailField(max_length=50)
    eliminada   = models.BooleanField(default=False)
    
'''
*********************************************************************
******************************* HITO 1 USUARIOS********************** 
*********************************************************************
'''


# MODELO USUARIO
class Usuario(models.Model):
    id              = models.AutoField(     primary_key=True)
    nombres         = models.CharField(     max_length=50   )
    apellidos       = models.CharField(     max_length=50   )
    rut             = models.CharField(     max_length=15   )
    direccion       = models.CharField(     max_length=150  )
    telefono        = models.CharField(     max_length=150  )
    correo          = models.EmailField(    max_length=50   )
    tipo_usuario    = models.CharField(   )
    eliminado       = models.BooleanField(default=False)
    password        = models.CharField(default="123",max_length=50)
   
    def __str__(self):
        return self.tipo_usuario
    
    
    
class ContactForm(models.Model):
    contact_form_uuid   = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name       = models.TextField(max_length=64)
    customer_email      = models.TextField()
    message             = models.TextField()
    
    def __str__(self):
        return self.customer_name
    
    
class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'

class Comuna(models.Model): 
    
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.RESTRICT)
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'
    
class Inmueble(models.Model):
    TIPOS                   = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
    nombre                  = models.CharField(max_length=50)
    descripcion             = models.TextField(max_length=1500)
    m2_construidos          = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales              = models.IntegerField(validators=[MinValueValidator(1)])
    num_estacionamientos    = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_habitaciones        = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    num_baños               = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion               = models.CharField(max_length=255)
    tipo_inmueble           = models.CharField(max_length=255, choices=TIPOS)
    precio                  = models.IntegerField(validators=[MinValueValidator(1000)], null=True) # precio mensual
    precio_ufs              = models.FloatField(validators=[MinValueValidator(1.0)], null=True)
    disponible              = models.BooleanField(default=True)
    img_url                 = models.URLField(default='')
    id                      = models.AutoField(     primary_key=True)
    tipo_usuario            = models.CharField(default='')
    eliminado               = models.BooleanField(default=False)
    #* UF se utiliza para ajustar los valores de contratos, precios y pagos para reflejar cambios en la inflación.
    #TODO_ FKs - llaves foráneas - 1:N
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    arrendador = models.ForeignKey(User, related_name='inmuebles', on_delete=models.RESTRICT)
    #* arrendador - propietario es un USER de de tipo rol 'arrendador' en el UserProfile
    # estado = models.CharField(max_length=255, choices=ESTADO) # <- 'nuevo', 'estrenar', 'viejo'
        
    
    
class LoginForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.TextField(max_length=64)
    customer_email = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name   
    


    
    
    '''
        IMPORTAR DATA DESDE JSON
        python manage.py loaddata INMUEBLES/data/users.json
        python manage.py loaddata INMUEBLES/data/regiones_comunas.json
        python manage.py loaddata INMUEBLES/data/inmuebles.json
        python manage.py loaddata INMUEBLES/data/usuarios_auth.json
    '''