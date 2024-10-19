from django.contrib import admin
from django.contrib.auth.views  import LoginView
from django.urls import path,include
from INMUEBLESAPP.views import index,agregar_usuario,mis_datos,contacto,bienvenido,loginxxx,detalles,agregar_inmueble#,  ,about,,exito,grilla
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('agregar_usuario/',agregar_usuario, name="agregar_usuario"),
    path('mis_datos/',mis_datos, name="mis_datos"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('bienvenido/',bienvenido),
    # path('acerca/',about),
    path('contacto/',contacto , name="contacto"),
    # path('exito/',exito ),
    # path('grilla/',grilla ),
    path('detalles/<int:inmueble_id>',detalles, name='detalles'),
    path('agregar_inmueble/<int:usuario_id>',agregar_inmueble, name='agregar_inmueble'),
    path('INMUEBLESAPP/',include('INMUEBLESAPP.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
