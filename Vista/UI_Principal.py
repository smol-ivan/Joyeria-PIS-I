from .UI_Usuario import UI_Usuario
from .UI_DatosEnvio import UI_DatosEnvio
from .UI_Pago import UI_Pago
from .UI_Catalogo import UI_Catalogo
from .UI_Inventario import UI_Inventario
from Modelo.Session import Session

class UI_Principal:
    def __init__(self):
        self.usuario = UI_Usuario()
        self.datos_envio = UI_DatosEnvio()
        self.pago = UI_Pago()
        self.catalogo = UI_Catalogo()
        self.inventario = UI_Inventario()
        self.session = Session()

    """
    Trabajo Ivan
    """

    '''
    Metodo que despliega el menu principal y redirige a las opciones seleccionadas
    '''
    def menu_principal(self):
        while True:
            print("Bienvenido a la tienda en línea")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Entrar como invitado")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.usuario.iniciar_sesion()
            elif opcion == "2":
                # self.usuario.registrarse()
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "3":
                # self.catalogo.mostrar_catalogo()
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "4":
                break
            else:
                print("Opción no válida")
    
    """
    Trabajo Mariana
    """

    """
    Trabajo Karla
    """

    """
    Trabajo Gabriel
    """