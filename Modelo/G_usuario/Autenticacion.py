from .Session import Session

class Autenticacion:
    def __init__(self, tabla_usuarios):
        self.tabla_usuarios = tabla_usuarios
        self.session = Session()

    '''
    Metodo que valida los datos
    Regresa True si las credenciales existen en la base de datos
    Regresa False si las credenciales no existen en la base de datos 
    '''
    def validacion_credenciales(self, correo, contrasena):
        usuario = self.tabla_usuarios.validar_credenciales(correo, contrasena)
        if usuario:
            self.session.iniciar_sesion(usuario)
            return True
        return False