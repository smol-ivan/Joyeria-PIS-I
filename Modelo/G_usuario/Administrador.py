from .Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, correo, contrasena) -> None:
        super().__init__(nombre, correo, contrasena)
