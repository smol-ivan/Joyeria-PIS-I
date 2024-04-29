from .Usuario import Usuario

class Miembro(Usuario):
    def __init__(self, nombre, correo, contrasena, id_usuario):
        super().__init__(nombre, correo, contrasena, id_usuario)
        self.fecha_nacimiento = "Aun no se ha ingresado una fecha de nacimiento"
        self.genero = "Aun no se ha ingresado un genero"
        self.pais = "Aun no se ha ingresado un pais"


    '''
    Metodos getter y setter
    '''

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def get_genero(self):
        return self.genero
    
    def set_genero(self, genero):
        self.genero = genero

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais