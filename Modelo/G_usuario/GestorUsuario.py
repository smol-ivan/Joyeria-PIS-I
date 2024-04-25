from .Autenticacion import Autenticacion
from .TablaUsuarios import TablaUsuarios
from .Miembro import Miembro
from .Administrador import Administrador

class GestorUsuario:
    def __init__(self):
        self.tabla_usuarios = TablaUsuarios()
        self.autenticacion = Autenticacion(self.tabla_usuarios)
        id_count = 0

    '''
    Metodo que inicializa la lista de usuarios
    '''
    def inicializar_usuarios(self):
        usuario1 = Miembro("Juan", "correo1@ejemplo", "1234")
        self.set_id(usuario1)
        usuario2 = Administrador("Pedro", "correo2@ejemplo", "1234")
        self.set_id(usuario2)
        self.tabla_usuarios.registrar_usuario(usuario1)
        self.tabla_usuarios.registrar_usuario(usuario2)

    '''
    Metodo que agrega un id a un usuario
    '''
    def set_id(self, usuario):
        self.id_count += 1
        usuario.set_id(self.id_count)

    '''
    Metodo que manda datos a la clase Autenticacion para solicitar la validacion de las credenciales
    '''
    def datos_iniciar_sesion(self, correo, contrasena):
        return self.autenticacion.validacion_credenciales(correo, contrasena)
    
    '''
    Metodo que regresa el tipo de usuario
    '''
    def tipo_usuario(self, usuario):
        if isinstance(usuario, Miembro):
            return "Miembro"
        elif isinstance(usuario, Administrador):
            return "Administrador"