from .Session import Session

class Autenticacion:
    def __init__(self, tabla_usuarios):
        self.tabla_usuarios = tabla_usuarios
        self.session = Session()

    def validacion_credenciales(self, correo, contrasena):
        for usuario in self.tabla_usuarios.obtener_usuarios():
            if usuario.get_correo() == correo and usuario.get_contrasena() == contrasena:
                return True
        return False