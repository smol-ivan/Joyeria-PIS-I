class Usuario:
    def __init__(self, nombre, correo, contrasena, id_usuario) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.id_usuario = id_usuario

    '''
    Metodos getter y setter
    '''
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correo(self):
        return self.correo
    
    def set_correo(self, correo):
        self.correo = correo

    def get_contrasena(self):
        return self.contrasena
    
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def get_id(self):
        return self.id_usuario
        