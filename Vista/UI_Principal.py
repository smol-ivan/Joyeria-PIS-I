from .UI_Usuario import UI_Usuario
from .UI_DatosEnvio import UI_DatosEnvio
from .UI_Pago import UI_Pago
from .UI_Catalogo import UI_Catalogo

class UI_Principal:
    def __init__(self) -> None:
        self.usuario = UI_Usuario()
        self.datos_envio = UI_DatosEnvio()
        self.pago = UI_Pago()
        self.catalogo = UI_Catalogo()
        self.cuenta_inicio_sesion = None
        self.administrador = None

    def setCuentaInicioSesion(self):
        '''
        Ejemplio de diccionario esperado:
        { "usuario": self.usuario, "tipo_usuario": self.tipo_usuario }
        '''
        data = self.usuario.get_usuario()
        self.cuenta_inicio_sesion = data["usuario"]
        if data["tipo_usuario"] == "administrador":
            self.administrador = True

    def menu_principal(self):
        print("Bienvenido a la tienda en línea")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Entrar como invitado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            self.usuario.iniciar_sesion()
        elif opcion == "2":
            self.usuario.registrarse()
        elif opcion == "3":
            self.catalogo.mostrar_catalogo()
        elif opcion == "4":
            exit()
        else:
            print("Opción no válida")
            self.menu_principal()