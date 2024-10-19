from django import forms
from .models import ContactForm,Usuario,Inmueble

# class ContactFormForm(forms.Form): #TODO DEFINE LOS CAMPOS DEL MODELO , CON SU TIPO DE CAMPO PREFORMATEADO DESDE DJANGO
#     customer_email = forms.EmailField(label='Email')
#     customer_name = forms.CharField(max_length=64, label='Nombre')
#     message = forms.CharField(label='Mensaje')
    
    
#     class ContactModelForm(forms.ModelForm):
#         class Meta:
#             model = ContactForm
#             fields = ['customer_email', 'customer_name', 'message']
            
class PostForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label='Email'                 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje'                       , widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class PostFormModelForm(forms.ModelForm):
        class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']
            

class LoginPostForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label='Email'                 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje'                       , widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class LoginPostFormModelForm(forms.ModelForm):
        class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']
            
class UsuarioPost(forms.Form):
    
    CHOICES = (('arrendatario', 'arrendatario'),('arrendador', 'arrendador'),)
    nombres     = forms.CharField(max_length=50     , label='nombres'     , widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos   = forms.CharField(max_length=50     , label='apellidos'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    rut         = forms.CharField(max_length=15     , label='rut'         , widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion   = forms.CharField(max_length=150    , label='direccion'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono    = forms.CharField(max_length=150    , label='telefono'    , widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo      = forms.CharField(max_length=50     , label='correo'      , widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_usuario= forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    eliminado   = forms.BooleanField(required=False)
    id          = forms.IntegerField(required=False,widget=forms.HiddenInput())
     
    
    class UsuarioPostFormModelForm(forms.ModelForm):
        class Meta:
            model = Usuario
            fields = ['nombres','apellidos','rut','direccion','telefono','correo','tipo_usuario','eliminado' ]
            
            
    class LoginPostForm(forms.Form):
        customer_name = forms.CharField(max_length=64, label='Nombre'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
        customer_email = forms.EmailField(label='Email'                 , widget=forms.TextInput(attrs={'class': 'form-control'}))
        message = forms.CharField(label='Mensaje'                       , widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class LoginPostFormModelForm(forms.ModelForm):
        class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']
            
            
            
class InmueblePostForm(forms.Form):
    CHOICES =  (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
    nombre                  = forms.CharField(max_length=50     , label='Nombre'        , widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion             = forms.CharField(max_length=50     , label='descripcion'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion               = forms.CharField(max_length=50     , label='direccion'     , widget=forms.TextInput(attrs={'class': 'form-control'}))
    m2_construidos          = forms.IntegerField( label='m2_construidos'             , widget=forms.TextInput(attrs={'class': 'form-control'}))
    m2_totales              = forms.IntegerField( label='m2_totales'                    , widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_estacionamientos    = forms.IntegerField( label='num_estacionamientos'          , widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_habitaciones        = forms.IntegerField( label='num_habitaciones'              , widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_baños               = forms.IntegerField( label='num_baños'                     , widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio                  = forms.IntegerField( label='precio'                        , widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio_ufs              = forms.IntegerField( label='precio_ufs'                    , widget=forms.TextInput(attrs={'class': 'form-control'}))
    disponible              = forms.BooleanField(required=False , label='disponible'    , widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_inmueble           = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    img_url                 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_usuario            = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    usuario_id              = forms.CharField(required=False)
    
    
    
class InmueblePostFormModelForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'direccion','m2_construidos','m2_totales','num_estacionamientos','num_habitaciones',
                  'num_baños','precio','precio_ufs','disponible','tipo_inmueble'] 
        
class PostFormBusqueda(forms.Form):
    txt_busqueda = forms.CharField(max_length=64,    widget=forms.TextInput(attrs={'class': 'form-control'}))