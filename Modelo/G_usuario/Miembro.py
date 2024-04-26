from .Usuario import Usuario

class Miembro(Usuario):
    def __init__(self, nombre, correo, contrasena, id_usuario):
        super().__init__(nombre, correo, contrasena, id_usuario)