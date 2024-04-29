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
    
    '''
    Metodo que recibe los datos de modificacion de usuario cuando en la UI se presiona el boton de modificar
    '''
    def enviar_datos_modificacion_usuario(self, opcion, dato):
        return self.gestor_usuario.recibir_datos_modificacion_usuario(opcion, dato)
    
    '''
    Metodo que fungue como evento para solicitar la informacion de un usuario
    '''
    def solicitar_datos_usuario(self):
        return self.gestor_usuario.solicitud_datos_usuario()
    
    '''
    Metodo que fungue como evento para solicitar eliminacion de cuenta por parte del usuario
    '''
    def boton_eliminar_cuenta(self):
        return self.gestor_usuario.solicitud_eliminar_cuenta()
    
    '''
    Metodo que fungue como evento para solicitar la eliminacion de la cuenta de un miembro por parte del administrador
    '''
    def boton_eliminar_cuenta_miembro(self):
        return self.gestor_usuario.solicitud_eliminar_cuenta_miembro()