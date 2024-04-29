from .Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, correo, contrasena, id_usuario):
        super().__init__(nombre, correo, contrasena, id_usuario)
        self.puesto = "CEO"

    '''
    Metodo getter y setter
    '''
    def get_puesto(self):
        return self.puesto
    
    def set_puesto(self, puesto):
        self.puesto = puesto