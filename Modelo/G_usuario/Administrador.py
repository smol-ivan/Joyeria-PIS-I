from .Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, correo, contrasena) -> None:
        super().__init__(nombre, correo, contrasena)
        self.id = None  # id del administrador

    '''
    Metodos getter y setter
    '''
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
