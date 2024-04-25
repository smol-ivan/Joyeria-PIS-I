class Usuario:
    def __init__(self, nombre, correo, contrasena) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

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
        