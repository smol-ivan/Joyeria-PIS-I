from Modelo.G_usuario.GestorUsuario import GestorUsuario

class Controller_Usuario:
    def __init__(self):
        self.gestor_usuario = GestorUsuario()

    '''
    Metodo que recibe los datos de inicio de sesion cuando en la UI se presiona el boton de iniciar sesion
    '''
    def enviar_datos_iniciar_sesion(self, usuario, contrasena):
        return self.gestor_usuario.recibir_datos_inicio_sesion(usuario, contrasena)
    
    '''
    Metodo que recibe los datos de registro de usuario cuando en la UI se presiona el boton de registrarse
    '''
    def enviar_datos_registro_usuario(self, nombre, correo, contrasena):
        return self.gestor_usuario.recibir_datos_registro_usuario(nombre, correo, contrasena)