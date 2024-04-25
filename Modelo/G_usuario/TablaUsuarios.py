class TablaUsuarios:
    def __init__(self):
        self.usuarios = []

    '''
    Metodo que verifica si el correo ya fue registrado
    '''
    def valida_usuario_existente(self, correo):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                return True
        return False

    '''
    Metodo que recibe instancia usuario y agrega a la lista de usuarios
    '''
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return True

    '''
    Metodo que valida las credenciales recibidas de inicio de sesion
    '''
    def obtener_usuario(self, correo, contrasena):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo & usuario.get_contrasena() == contrasena:
                return usuario