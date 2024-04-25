from .Usuario import Usuario

class Miembro(Usuario):
    def __init__(self, nombre, correo, contrasena) -> None:
        super().__init__(nombre, correo, contrasena)
        self.id = None  # id del miembro

    '''
    Metodos getter y setter
    '''
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id