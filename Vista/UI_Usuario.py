from Modelo.G_usuario.GestorUsuario import GestorUsuario

class UI_Usuario:
    def __init__(self):
        self.gestor_usuario = GestorUsuario()
        # self.gestor_datos_envio = GestorDatosEnvio()
        self.tipo_usuario = None
        self.usuario = None

    '''
    Metodo que envia los datos de inicio de sesion al gestor de usuario
    '''
    def envia_datos_inicio_sesion(self, correo, contraseña):
        auth = self.gestor_usuario.datos_iniciar_sesion(correo, contraseña)
        return auth
    
    '''
    Metodo para obtener el usuario y el tipo de usuario
    '''
    def get_usuario(self):
        return { "usuario": self.usuario, "tipo_usuario": self.tipo_usuario }
    
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
        print("Iniciar sesión")
        correo, contraseña = self.ingreso_datos_inicio_sesion()
        self.usuario = self.envia_datos_inicio_sesion(correo, contraseña)
        if self.usuario != None:
            self.tipo_usuario = self.gestor_usuario.tipo_usuario(self.usuario)
            print("Inicio de sesión correcto")
            return True
        else:
            print("Correo o contraseña incorrectos")
            print("¿Desea intentar de nuevo?")
            print("1. Sí")
            print("2. No")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                return False
            else:
                print("Opción no válida")
                self.iniciar_sesion()
        
    '''
    Metodo que recibe los datos de registro
    '''
    def ingreso_datos_registro(self):
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return nombre, correo, contraseña

    '''
    Metodo despliega UI para registrarse
    '''
    def registrarse(self):
        print("Registrarse")
        nombre, correo, contraseña = self.ingreso_datos_registro()
        