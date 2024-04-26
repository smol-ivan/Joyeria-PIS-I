from .Session import Session

class Autenticacion:
    def __init__(self, tabla_usuarios):
        self.tabla_usuarios = tabla_usuarios
        self.session = Session()

    def validacion_credenciales(self, correo, contrasena):
        usuario = self.tabla_usuarios.obtener_usuario(correo, contrasena)
        if usuario:
            self.session.iniciar_sesion(usuario)
            return True
        return False