from .Autenticacion import Autenticacion
from .TablaUsuarios import TablaUsuarios
from .Miembro import Miembro
from .Administrador import Administrador
from .Session import Session

class GestorUsuario:
    def __init__(self):
        self.id_count = 0
        self.tabla_usuarios = TablaUsuarios()
        self.inicializar_usuarios()
        self.autenticacion = Autenticacion(self.tabla_usuarios)
        self.session = Session()

    '''
    Metodo que actualiza el contador de id
    '''
    def set_id(self):
        self.id_count += 1
        return self.id_count

    '''
    Metodo que inicializa la lista de usuarios
    '''
    def inicializar_usuarios(self):
        id_usuario = self.set_id()
        usuario1 = Miembro("Juan", "correo1@ejemplo", "1234", id_usuario)
        id_usuario = self.set_id()
        usuario2 = Administrador("Pedro", "correo2@ejemplo", "1234", id_usuario)
        self.tabla_usuarios.registrar_usuario(usuario1)
        self.tabla_usuarios.registrar_usuario(usuario2)

    '''
    Metodo que recibe los datos de inicio de sesion y manda a la clase Autenticacion para validarlos
    '''

    def recibir_datos_inicio_sesion(self, correo, contrasena):
        return self.autenticacion.validacion_credenciales(correo, contrasena)
    
    '''
    Metodo que recibe los datos de registro de usuario y manda a la clase Autenticacion para validarlos
    '''
    def recibir_datos_registro_usuario(self, nombre, correo, contrasena):
        if self.tabla_usuarios.obtener_usuario(correo, contrasena):
            return False
        id_usuario = self.set_id()
        usuario = Miembro(nombre, correo, contrasena, id_usuario)
        self.tabla_usuarios.registrar_usuario(usuario)
        return True