from django.core.management.base import BaseCommand, no_translations
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, LoginForm,Inmueble,Region,Comuna #, ContactForm
from .forms import PostForm,ContactForm,UsuarioPost,LoginPostForm,InmueblePostForm,PostFormBusqueda
from django.contrib.auth.decorators import login_required
from INMUEBLESAPP import services 
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.



def index(request):
    new_usuarios = Usuario.objects.all()
    return render(request, 'index.html', {"usuarios": new_usuarios})
    
    
def agregar_usuario(request): #! EL VIEW DEBERIA LLAMAR AL SERVICES
    if request.method == 'POST':
        form = UsuarioPost(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        # form.cleaned_data['id'] = request.user.id
        print('POST')
        print(str(form.is_valid()))
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            services.add_usuario(form.cleaned_data['nombres'],form.cleaned_data['apellidos'],form.cleaned_data['rut'],form.cleaned_data['direccion'],form.cleaned_data['telefono'],form.cleaned_data['correo'],form.cleaned_data['tipo_usuario'],form.cleaned_data['eliminado'])
            # print('POST form.is_valid')
            # print(f'''{form.data['nombres']}''')
            # print(f'''{form.cleaned_data}''')
            # print(f'''{form.cleaned_data['nombres'],form.cleaned_data['apellidos'],form.cleaned_data['rut'],form.cleaned_data['direccion'],form.cleaned_data['telefono'],form.cleaned_data['correo'],form.cleaned_data['tipo_usuario'],form.cleaned_data['eliminado']}''')
            # form = UsuarioPost.cleaned_data() # TODO: ** **form.cleaned_data PASA LOS DATOS COMO ARGUMENTOS PARA INSERT EN LA DDBB
            # return HttpResponseRedirect('exito.html')
        messages.success(request, "El usuario fue creado correctamente")
        form = UsuarioPost() 
        return render(request, 'agregar_usuario.html',{'form':form})
    else: 
        print('GET')
        form = UsuarioPost()   
        
    return render(request, 'agregar_usuario.html', {'form':form})

def mis_datos(request):
    if request.method == 'POST':
        print('POST')
        form = UsuarioPost(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCION
        # id_usuario, nombres,apellidos,rut,direccion,telefono,correo,tipo_usuario,eliminado
        print(f'''{form.data['csrfmiddlewaretoken']}''')
        print(f'''{request.POST.get('csrfmiddlewaretoken')}''')
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            #TODO: LA SIGUIENTE LINEA RESCATA DESDE EL FORM POR EL GET DEL DICCIONARIO  
            new_usuario =   services.actualizar_usuario(form.cleaned_data.get('id'),form.cleaned_data.get('nombres'),form.cleaned_data.get('apellidos'),
                                        form.cleaned_data.get('rut'),form.cleaned_data.get('direccion'),form.cleaned_data.get('telefono'),
                                        form.cleaned_data.get('correo'),form.cleaned_data.get('tipo_usuario'),form.cleaned_data.get('eliminado'))  #EN EL FORMULARIO
        # new_usuarios = usuario(request.POST,instance=new_usuarios)
        messages.success(request, "El usuario fue actualizado correctamente")
        return render(request, 'mis_datos.html', {"form": form} )
    else: 
        print('GET')
        usuario = Usuario.objects.get(id=request.user.id) #! FALTA RESCATAR EL ID --- ACTUALMENTE ESTA ENDURO 
        print(usuario.nombres,usuario.correo,usuario.apellidos)
        print(f'''usuaro: {usuario.id}''')
        form = UsuarioPost(initial=usuario.__dict__) #TODO: HACE EL GET DESDE LA INSTANCIA RESCATADA ASIGNA VALORES AL FORM
    return render(request, 'mis_datos.html', {"form": form} )


def contacto(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        print('POST')
        print(str(form.is_valid()))
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            print('POST form.is_valid')
            ContactForm.objects.create(**form.cleaned_data) # TODO: ** **form.cleaned_data PASA LOS DATOS COMO ARGUMENTOS PARA INSERT EN LA DDBB
            # return HttpResponseRedirect('exito.html')
            return render(request, 'exito.html', {})
    else: 
        print('GET')
        form = PostForm()   
    return render(request, 'contacto.html', {'form':form})

def loginxxx(request):
    print('entra login form view')
    if request.method == 'POST':
        form = LoginPostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        print('LOGIN POST')
        print(str(form.is_valid()))
        
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            print('POST form.is_valid')
            LoginForm.objects.create(**form.cleaned_data) # TODO: ** **form.cleaned_data PASA LOS DATOS COMO ARGUMENTOS PARA INSERT EN LA DDBB
            # return HttpResponseRedirect('exito.html')
            
            if services.valida_login(form.cleaned_data.get('nombres'),form.cleaned_data.get('password')):
                return render(request, 'exito.html', {})
    else: 
        print('GET')
        form = LoginPostForm()   
    return render(request, 'login.html', {'form':form})

@login_required
def bienvenido(request):
    if request.method == 'POST':
        form = PostFormBusqueda(request.POST)
        # print(request.request.user.id)
        print(request.POST.get("txt_busqueda"))
        inmuebles_asociados_al_usuario = services.get_inmuebles_usuarios_por_usuario(request.user.id,request.POST.get("txt_busqueda"))
        new_usuario = services.traer_usuario_por_id(request.user.id)
        return render(request, 'bienvenido.html', {"inmuebles_usuario": inmuebles_asociados_al_usuario, "usuario": new_usuario})
    else: 
        print('GET')  
        print(request.user.id)
        inmuebles_asociados_al_usuario = services.get_inmuebles_usuarios_por_usuario(request.user.id) 
        print(f'ESTE ES EL USUARIO_ID:{request.user.id}')
        new_usuario = services.traer_usuario_por_id(request.user.id)
        return render(request, 'bienvenido.html', {"inmuebles_usuario": inmuebles_asociados_al_usuario, "usuario": new_usuario})

        
#TODO: VISTA DETALLE
@login_required
def detalles(request, inmueble_id):
    if request.method == 'POST':
        print(request.POST.get("Actualizar"))
        form = InmueblePostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        # print('POST')
        # print(str(form.is_valid()))
        # print(form.cleaned_data.get('nombre'),form.cleaned_data.get('img_url'))
        
        print(request.user.id)
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            # print('POST form.is_valid')
            # print(f'''{**form.cleaned_data}''')
            if 'Actualizar' in request.POST: #TODO: CUANDO ES EL BOTON ACTUALIZAR
                print("boton actualizar")
                new_inmueble = services.actualizar_inmueble(inmueble_id,
                                        form.cleaned_data.get('nombre'),form.cleaned_data.get('descripcion'),
                                        form.cleaned_data.get('direccion'),form.cleaned_data.get('m2_construidos'),
                                        form.cleaned_data.get('m2_totales'),form.cleaned_data.get('num_estacionamientos'),
                                        form.cleaned_data.get('num_habitaciones'),form.cleaned_data.get('num_baños'),
                                        form.cleaned_data.get('precio'),form.cleaned_data.get('precio_ufs'),
                                        form.cleaned_data.get('disponible'),form.cleaned_data.get('tipo_inmueble'),
                                        form.cleaned_data.get('img_url'))
                
                new_inmueble_porid = services.get_inmuebles_por_id(inmueble_id)
                new_usuario =  services.traer_usuario_por_id(new_inmueble_porid.arrendador.id)
                new_inmueble_porid.tipo_usuario = new_usuario.tipo_usuario
                form = InmueblePostForm(initial=new_inmueble_porid.__dict__) 
                messages.success(request, "El inmueble fue actualizado correctamente.")
                return render(request, 'detalles.html', {'form' : form})
            
                # messages.success(request, "El inmueble fue actualizado correctamente.")
                # return render(request, 'detalles.html', {"form": form})    
                
            if 'Eliminar' in request.POST:
                print("boton Eliminar")      #TODO: CUANDO ES EL BOTON ELIMINAR
                services.eliminar_inmueble(inmueble_id)
                # messages.success(request, "El inmueble fue Eliminado correctamente.")
                inmuebles_asociados_al_usuario = services.get_inmuebles_usuarios_por_usuario(request.user.id) 
                new_usuario = services.traer_usuario_por_id(request.user.id)
                return render(request, 'bienvenido.html', {"inmuebles_usuario": inmuebles_asociados_al_usuario, "usuario": new_usuario})
      
            # return render(request, 'exito.html', {})
    else: 
        
        print('GET')
        print(f'INMUEBLE_ID: {inmueble_id}')
        print(request.user.id)
        # if inmueble_id != 0:
        
        new_inmueble_porid = services.get_inmuebles_por_id(inmueble_id)
        new_usuario =  services.traer_usuario_por_id(request.user.id)
        new_inmueble_porid.tipo_usuario = new_usuario.tipo_usuario
        
        # print(f'USUARIO xxxxxx: {new_usuario.tipo_usuario}')
        # print(f'USUARIO INMUEBLE xxxxxx: {new_inmueble_porid.tipo_usuario}')
        # print(f'INMUEBLE: {new_inmueble_porid}')
        print(f'ARRENDADOR: {new_inmueble_porid.arrendador.id}')
        form = InmueblePostForm(initial=new_inmueble_porid.__dict__)   
        if new_usuario.tipo_usuario != 'arrendador':
            for field in form.fields.values():
                field.disabled = True  # Deshabilitar todos los campos en la vista
        
        return render(request, 'detalles.html', {'form' : form})
        # else:
        #     print('ELSE')
        #     form = InmueblePostForm() 
        #     return render(request, 'detalles.html', {'form' : form})
            # pass
        # print(f'INMUEBLE_ID: {new_inmueble_porid.id},{new_inmueble_porid.nombre}')
    
    
@login_required
def agregar_inmueble(request, usuario_id):
    print(usuario_id)
    print(f' GET USUARIO_ID: {request.user.id}')
    if request.method == 'POST':
        # print('POST')
        # # pass
        print(f' GET USUARIO_ID: {request.user.id}')
        form = InmueblePostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        # form.usuario_id = request.POST.usuario_id
        # form.fields['usuario_id'] = request.POST.user.id
        # print(f' form.fields[usuario_id]: {form.fields['usuario_id']}')
        # form.fields.values['usuario_id'] = request.POST.user.id
        # form.fields['tipo_usuario'] = 'arrendador'
        # print(f' GET USUARIO_ID: {form.cleaned_data['usuario_id']}')
        # form.cleaned_data['usuario_id'] = request.user.id
        print('POST')
        print(str(form.is_valid()))
    #     # print(form.cleaned_data.get('nombre'),form.cleaned_data.get('img_url'))
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            # print('POST form.is_valid')
            new_inmueble = services.agregar_inmueble(
                                        form.cleaned_data.get('nombre'),form.cleaned_data.get('descripcion'),
                                        form.cleaned_data.get('direccion'),form.cleaned_data.get('m2_construidos'),
                                        form.cleaned_data.get('m2_totales'),form.cleaned_data.get('num_estacionamientos'),
                                        form.cleaned_data.get('num_habitaciones'),form.cleaned_data.get('num_baños'),
                                        form.cleaned_data.get('precio'),form.cleaned_data.get('precio_ufs'),
                                        form.cleaned_data.get('disponible'),form.cleaned_data.get('tipo_inmueble'),
                                        form.cleaned_data.get('img_url'),form.cleaned_data.get('tipo_usuario'),
                                        request.user.id
                                        )
            
            messages.success(request, "El inmueble fue actualizado correctamente.")
            return render(request, 'agregar_inmueble.html', {"form": form} )
            # return render(request, 'exito.html', {})
        else: print(f'FALTAN CAMPOS form.is_valid() ES INVALIDO: {usuario_id}')
    else: 
        print('GET')
        # print(f'USUARIO_ID xxxxxxxxxxxxx: {usuario_id}')
        # print(f' GET USUARIO_ID: {request.user.id}')
        new_inmueble =  InmueblePostForm() 
        new_inmueble.usuario_id = request.user.id
        # print(f'NEW_INMUEBLE.USUARIO_ID:{new_inmueble.usuario_id}')
        form = InmueblePostForm(initial={'usuario_id': request.user.id, 'tipo_usuario':'arrendador'}) 
        # print(f'''{form.data['usuario_id']}''')
        # print(f'''{form.cleaned_data}''')
        return render(request, 'agregar_inmueble.html', {'form' : form})
        
       
        # if inmueble_id != 0:
        # new_inmueble_porid = services.get_inmuebles_por_id(inmueble_id)
        # new_usuario =  services.traer_usuario_por_id(new_inmueble_porid.arrendador.id)
        # new_inmueble_porid.tipo_usuario = new_usuario.tipo_usuario
        
        # print(f'USUARIO xxxxxx: {new_usuario.tipo_usuario}')
        # print(f'USUARIO INMUEBLE xxxxxx: {new_inmueble_porid.tipo_usuario}')
        
        # print(f'INMUEBLE: {new_inmueble_porid}')
        # print(f'ARRENDADOR: {new_inmueble_porid.arrendador.id}')
        # form = InmueblePostForm(initial=new_inmueble_porid.__dict__)   
        # if new_usuario.tipo_usuario != 'arrendador':
        #     for field in form.fields.values():
        #         field.disabled = True  # Deshabilitar todos los campos en la vista
        
       
    
    
    
    
    # return render(request, 'detalles.html', {'inmueble' : new_inmueble_porid})


