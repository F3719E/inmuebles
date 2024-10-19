from INMUEBLESAPP.models import Persona,Usuario,Inmueble,Region,Comuna


def recuperar_personas():
    personas = Persona.objects.all()
    
    todas_las_personas = []
    for persona in personas: 
        persona_item = {
            'personas': persona,
        }
        todas_las_personas.append(persona_item)
    return todas_las_personas

def add_personas(nombre = "" , apellido='', correo="correo@correo.cl"):
    persona = Persona(nombre=nombre, apellido=apellido, correo=correo)
    persona.save()
    return persona

def elimina_persona(persona_id):
    persona = Persona.objects.get(pk=persona_id)
    persona.eliminada = True 
    persona.save()
    return recuperar_personas() 

# MyModel.objects.filter(pk=some_value).update(field1='some value')
def update_persona(persona_id,nombre,apellido,correo):
    persona = Persona.objects.filter(pk=persona_id).update(nombre=nombre,apellido=apellido,correo=correo)
    return recuperar_personas() 

def imprimir_personas(personas=[]):
    for itm_persona in personas:
        print(f'''{itm_persona['personas'].id} : {itm_persona['personas'].nombre} : {itm_persona['personas'].apellido},{itm_persona['personas'].correo},{itm_persona['personas'].eliminada}''')
        # print(t['subtareas'].descripcion)
        # print(f'{t['tareas'].id} ')
        
        # for v in t['subtareas']:
        #     print(f'----->{v.id} : {v.descripcion} ---> tarea: {v.tarea.id}')
        
'''
*********************************************************************
**************************** HITO USUARIOS ************************** 
*********************************************************************'''     
def get_usuarios():
    usuarios = Usuario.objects.all()
    todos_los_usuarios = []
    for itm_usuario in usuarios: 
        usuario_item = {
            'usuarios': itm_usuario,
        }
        todos_los_usuarios.append(usuario_item)
    return todos_los_usuarios 

def traer_usuario_por_id(usuario_id):
    new_usuarios = Usuario.objects.get(id=usuario_id)
    return new_usuarios 


def add_usuario(nombres = "" , apellidos='',rut='',direccion='',telefono='', correo="correo@correo.cl",tipo_usuario='',eliminado=False,password="123"):
    usuario = Usuario(nombres=nombres, apellidos=apellidos,rut=rut,direccion=direccion,telefono=telefono, correo=correo,tipo_usuario=tipo_usuario, eliminado=eliminado,password=password)
    usuario.save()
    return usuario  



# def create_user(new_user):
#     user = User.objects.create_user(
#         username=new_user['username'],
#         email=new_user['email'],
#         first_name=new_user['first_name'],
#         last_name=new_user['last_name'],
#         password=new_user['password']
#     )
#     return user

def valida_login(nombres = "" ,password=""):
    new_usuario = Usuario.objects.get(nombres=nombres)
    print(new_usuario.nombres, new_usuario.password)
    if new_usuario.password == password:
        return True
    else: return False   
    '''
from INMUEBLESAPP.services import get_usuarios, add_usuario,mostrar_usuarios,actualizar_usuario,valida_login
valida_login('bruce','123')
    
    '''
  
def mostrar_usuarios(usuarios=[]):
    for itm_usuario in usuarios:
        print(f'''{itm_usuario['usuarios'].id} : {itm_usuario['usuarios'].nombres} : {itm_usuario['usuarios'].apellidos},{itm_usuario['usuarios'].direccion},{itm_usuario['usuarios'].telefono},{itm_usuario['usuarios'].correo},{itm_usuario['usuarios'].tipo_usuario}''')
        # print(t['subtareas'].descripcion)
        # print(f'{t['tareas'].id} ')
        
        # for v in t['subtareas']:
        #     print(f'----->{v.id} : {v.descripcion} ---> tarea: {v.tarea.id}')  

def actualizar_usuario(id_usuario, nombres,apellidos,rut,direccion,telefono,correo,tipo_usuario,eliminado):
        usuario = Usuario.objects.get(pk=id_usuario)  # Buscar el inmueble por ID
        usuario.nombres         = nombres
        usuario.apellidos       = apellidos
        usuario.rut             = rut        
        usuario.direccion       = direccion
        correo                  = correo
        usuario.telefono        = telefono
        usuario.tipo_usuario    = tipo_usuario
        usuario.eliminado       = eliminado
        usuario.save()  # Guardar los cambios
        return {usuario}

'''
*********************************************************************
**************************** HITO INMUEBLES ************************** 
*********************************************************************''' 

def get_inmuebles_usuarios_por_usuario(id_usuario, comuna=''):
    print(f'entro comuna: {comuna}')
    
    new_usuario = Usuario.objects.get(id=id_usuario)
    print(new_usuario.__str__())
    
    if  comuna != '':  #"07304"
        print(f'ENTRO: {comuna}')
        new_comuna = Comuna.objects.get(nombre=comuna)
        # new_libros = Region.objects.select_related('inmuebles').all()
        print(f'ENTRO: {Comuna.nombre}')
        inmuebles = Inmueble.objects.filter(arrendador_id=id_usuario, comuna_id=new_comuna.cod,eliminado=False)
    if  comuna == '': 
        inmuebles = Inmueble.objects.filter(arrendador_id=id_usuario,eliminado=False)
    if  new_usuario.__str__() == 'arrendatario': 
        if  comuna != '':  #"07304"
            inmuebles = Inmueble.objects.filter(disponible=True,comuna=comuna,eliminado=False)
        else: inmuebles = Inmueble.objects.filter(disponible=True,eliminado=False)
        

    # todos_los_inmuebles = []
    # for itm_inmueble in inmuebles: 
    #     Inmueble_item = {
    #         'inmuebles': itm_inmueble
    #     }
    #     todos_los_inmuebles.append(Inmueble_item)
        # print(todos_los_inmuebles)      #[{'inmuebles': <Inmueble: Inmueble object (1)>}]
        # print(todos_los_inmuebles[0].get('inmuebles').nombre) #Casa Acogedora
    return inmuebles 

def get_inmuebles_por_id(id_inmueble):
    inmuebles = Inmueble.objects.get(pk=id_inmueble)
    # el_inmueble = []
    # for itm_inmueble in inmuebles: 
    #     inmueble_item = {
    #         'inmueble': itm_inmueble,
    #     }
    # el_inmueble.append(inmueble_item)
        # print(todos_los_inmuebles)      #[{'inmuebles': <Inmueble: Inmueble object (1)>}]
        # print(todos_los_inmuebles[0].get('inmuebles').nombre) #Casa Acogedora
    return inmuebles 

def agregar_inmueble( nombre,descripcion,direccion,m2_construidos:0,m2_totales,num_estacionamientos,
                        num_habitaciones,num_baños,precio,precio_ufs,disponible,tipo_inmueble,img_url,
                        tipo_usuario,usuario_id):
            inmueble = Inmueble.objects.create(
                                                nombre                  = nombre,
                                                descripcion             = descripcion,
                                                direccion               = direccion,
                                                m2_construidos          = m2_construidos,
                                                m2_totales              = m2_totales,
                                                num_estacionamientos    = num_estacionamientos,
                                                num_habitaciones        = num_habitaciones,
                                                num_baños               = num_baños,
                                                precio                  = precio,
                                                precio_ufs              = precio_ufs,
                                                disponible              = disponible,
                                                tipo_inmueble           = tipo_inmueble,
                                                img_url                 = img_url,
                                                tipo_usuario            = tipo_usuario,
                                                arrendador_id           = usuario_id,
                                                comuna_id                  =   '01101'
                                                )
            return inmueble
            
def actualizar_inmueble(id_inmueble, nombre,descripcion,direccion,m2_construidos:0,m2_totales,num_estacionamientos,
                        num_habitaciones,num_baños,precio,precio_ufs,disponible,tipo_inmueble,img_url):
    
        inmueble = Inmueble.objects.get(pk=id_inmueble)  # Buscar el inmueble por ID
        inmueble.nombre                   =   nombre         
        inmueble.descripcion              =   descripcion      
        inmueble.direccion                =   direccion   
        inmueble.m2_construidos           =   m2_construidos 
        inmueble.m2_totales               =   m2_totales  
        inmueble.num_estacionamientos     =   num_estacionamientos
        inmueble.num_habitaciones         =   num_habitaciones
        inmueble.num_baños                =   num_baños 
        inmueble.precio                   =   precio 
        inmueble.precio_ufs               =   precio_ufs 
        inmueble.disponible               =   disponible  
        inmueble.tipo_inmueble            =   tipo_inmueble 
        inmueble.img_url                  =   img_url            
        inmueble.save()  # Guardar los cambios
        return {inmueble}  
    
    
def eliminar_inmueble(id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    inmueble.eliminado = True
    inmueble.save()
    return inmueble   

'''
*********************************************************************
**************************** HITO INMUEBLES ************************** 
********************************************************************* 
python manage.py shell
from INMUEBLESAPP.services import get_usuarios, add_usuario,mostrar_usuarios,actualizar_usuario,valida_login,get_inmuebles_usuarios_por_usuario
new_inmuebles = get_inmuebles_usuarios_por_usuario(1)
new_inmuebles[0].get('inmuebles').nombre

'''


'''
*********************************************************************
******************************* HITO USUARIOS *********************** 
*********************************************************************
python manage.py shell
from INMUEBLESAPP.services import get_usuarios, add_usuario,mostrar_usuarios,actualizar_usuario,valida_login

new_usuario = add_usuario('nombre nombre','apellido apellido','rut','direccion','telefono','uno@uno.cl','tipo') 
new_usuario.nombres, new_usuario.apellidos,new_usuario.rut,new_usuario.direccion,new_usuario.telefono, new_usuario.correo,new_usuario.tipo_usuario

new_usuario = get_usuarios()
mostrar_usuarios(new_usuario)


new_usuario = actualizar_usuario(36,'xxxxxx','xxxxx apellido','xxxx','xxxxdireccion','xxxxtelefono','xxx@uno.cl','arrendatario',True) 

valida_login('bruce','123')

*********************************************************************
******************************* HITO ******************************** 
*********************************************************************

python manage.py shell
from INMUEBLESAPP.services import add_personas, recuperar_personas,imprimir_personas,elimina_persona,update_persona
new_persona = recuperar_personas() 
new_persona[0].nombre, new_persona[0].apellido,new_persona[0].correo

python manage.py shell
from INMUEBLESAPP.services import add_personas, recuperar_personas,imprimir_personas,elimina_persona,update_persona
new_persona = add_personas('uno','uno','uno@uno.cl') 
new_persona.nombre, new_persona.apellido, new_persona.correo

python manage.py shell
from INMUEBLESAPP.services import add_personas, recuperar_personas,imprimir_personas,elimina_persona,update_persona
new_persona = recuperar_personas()  
imprimir_personas(new_persona)

python manage.py shell
from INMUEBLESAPP.services import add_personas, recuperar_personas,imprimir_personas,elimina_persona,update_persona
new_persona = elimina_persona(1)  
imprimir_personas(new_persona)

python manage.py shell
from INMUEBLESAPP.services import add_personas, recuperar_personas,imprimir_personas,elimina_persona,update_persona
new_persona = update_persona(1,'nombre modificado','apellido modificado','correomodificado@correo.cl')  
imprimir_personas(new_persona)



'''
