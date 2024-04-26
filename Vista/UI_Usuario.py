from Controlador.Controller_Usuario import Controller_Usuario

class UI_Usuario:
    def __init__(self):
        self.controlador_usuario = Controller_Usuario()

    '''
    Metodo que envia los datos de inicio de sesion al gestor de usuario
    '''
    def envia_datos_inicio_sesion(self, correo, contraseña):
        auth = self.controlador_usuario.enviar_datos_iniciar_sesion(correo, contraseña)
        return auth
    
    '''
    Metodo donde se ingresan los datos de inicio de sesion
    '''
    def ingreso_datos_inicio_sesion(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return correo, contraseña
    
    '''
    Metodo despliegua UI para iniciar sesion
    '''
    def iniciar_sesion(self):
        inicio_sesion = False
        while True:
            print("Iniciar sesión")
            correo, contraseña = self.ingreso_datos_inicio_sesion()
            self.usuario = self.envia_datos_inicio_sesion(correo, contraseña)
            if self.usuario != None:
                self.tipo_usuario = self.gestor_usuario.tipo_usuario(self.usuario)
                print("Inicio de sesión correcto")
                inicio_sesion = True
                break
            else:
                print("Correo o contraseña incorrectos")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta == "N":
                    break
        return inicio_sesion
    
    '''
    Metodo que recibe los datos de registro
    '''
    def ingreso_datos_registro(self):
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return nombre, correo, contraseña
        