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
        while True:
            print("Iniciar sesión")
            correo, contraseña = self.ingreso_datos_inicio_sesion()
            respuesta_validacion = self.envia_datos_inicio_sesion(correo, contraseña)
            if respuesta_validacion:
                print("Inicio de sesión correcto")
                break
            else:
                print("Correo o contraseña incorrectos")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

    '''
    Metodo que envia los datos de registro al gestor de usuario
    '''
    def envia_datos_registro(self, nombre, correo, contraseña):
        return self.controlador_usuario.enviar_datos_registro_usuario(nombre, correo, contraseña)
    
    '''
    Metodo que recibe los datos de registro
    '''
    def ingreso_datos_registro(self):
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return nombre, correo, contraseña
        
    '''
    Metodo que despliega UI para registrarse
    '''
    def registrarse(self):
        while True:
            print("Registrarse")
            nombre, correo, contraseña = self.ingreso_datos_registro()
            respuesta_validacion = self.envia_datos_registro(nombre, correo, contraseña)
            if respuesta_validacion:
                print("Registro exitoso")
                print("Por favor inicie sesión")
                break
            else:
                print("Correo ya registrado")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break