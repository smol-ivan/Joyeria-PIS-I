from .Autenticacion import Autenticacion
from .TablaUsuarios import TablaUsuarios
from .Miembro import Miembro
from .Administrador import Administrador

class GestorUsuario:
    def __init__(self):
        self.id_count = 0
        self.tabla_usuarios = TablaUsuarios()
        self.inicializar_usuarios()
        self.autenticacion = Autenticacion(self.tabla_usuarios)

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
    
    '''
    Metodo que recibe el dato de modificacion de usuario y solicita a la clase TablaUsuarios que lo modifique
    '''
    def recibir_datos_modificacion_usuario(self, opcion, dato):
        return self.tabla_usuarios.modificar_dato_usuario(opcion, dato)
    
    '''
    Metodo que recibe solicitud de controlador para obtener los datos de un usuario
    Obtiene el usuario de la clase session
    '''
    def solicitud_datos_usuario(self):
        usuario = self.tabla_usuarios.obtener_usuario()
        return self.preparar_datos_usuario(usuario)

    '''
    Metodo que prepara los datos de el usuario(Miembro) en un diccionario
    '''
    def preparar_datos_usuario(self, usuario):
        # Si el usuario es un miembro
        if isinstance(usuario, Miembro):
            return {
                "Nombre": usuario.get_nombre(),
                "Correo": usuario.get_correo(),
                "Fecha de nacimiento": usuario.get_fecha_nacimiento(),
                "Genero": usuario.get_genero(),
                "Pais": usuario.get_pais()
            }
        # Si el usuario es un administrador
        elif isinstance(usuario, Administrador):
            return {
                "Nombre": usuario.get_nombre(),
                "Correo": usuario.get_correo(),
                "Puesto": usuario.get_puesto()
            }
        
    '''
    Metodo que recibe solicitud de controlador para eliminar un usuario
    '''
    def solicitud_eliminar_cuenta(self):
        return self.tabla_usuarios.eliminar_cuenta()