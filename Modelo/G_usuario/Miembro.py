from .Usuario import Usuario

class Miembro(Usuario):
    def __init__(self, nombre, correo, contrasena) -> None:
        super().__init__(nombre, correo, contrasena)