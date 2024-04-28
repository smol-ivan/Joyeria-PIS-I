from .Session import Session

class TablaUsuarios:
    def __init__(self):
        self.usuarios = []
        self.session = Session()

    '''
    Metodo que recibe instancia usuario y agrega a la lista de usuarios
    '''
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return True

    '''
    Metodo que valida las credenciales recibidas de inicio de sesion
    '''
    def validar_credenciales(self, correo, contrasena):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo and usuario.get_contrasena() == contrasena:
                return usuario
            
    '''
    Metodo que obtiene el usuario por id
    '''        
    def obtener_usuario_por_id(self, id):
        for usuario in self.usuarios:
            if usuario.get_id() == id:
                return usuario

    '''
    Metodo que cambia el dato de usuario segun la opcion elegida
    '''
    def modificar_dato_usuario(self, opcion, dato):
        id_usuario = self.session.obtener_id_usuario()
        usuario = self.obtener_usuario_por_id(id_usuario)
        if opcion == 1:
            usuario.set_nombre(dato)
        elif opcion == 2:
            usuario.set_correo(dato)
        elif opcion == 3:
            usuario.set_contrasena(dato)
        return True