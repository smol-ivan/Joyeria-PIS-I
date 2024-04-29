from .UI_Usuario import UI_Usuario
from .UI_DatosEnvio import UI_DatosEnvio
from .UI_Pago import UI_Pago
from .UI_Catalogo import UI_Catalogo
from .UI_Inventario import UI_Inventario
from Modelo.G_usuario.Session import Session
from Controlador.Controller_Inventario import Controller_Inventario

class UI_Principal:
    def __init__(self):
        self.usuario = UI_Usuario()
        self.datos_envio = UI_DatosEnvio()
        self.pago = UI_Pago()
        self.catalogo = UI_Catalogo()
        self.controlador_inventario = Controller_Inventario()
        self.inventario = UI_Inventario(self.controlador_inventario)
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
                self.desplegar_menu_usuario()
            elif opcion == "2":
                self.usuario.registrarse()
            elif opcion == "3":
                # self.catalogo.mostrar_catalogo()
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "4":
                print("Saliendo de la tienda en línea")
                exit()
            else:
                print("Opción no válida")

    '''
    Metodo para seleccionar que tipo de menu desplegar
    '''
    def desplegar_menu_usuario(self):
        if not self.session.esta_autenticado():
            print("No se ha iniciado sesión")
            return
        if self.session.es_administrador():
            self.menu_administrador()
        else:
            self.menu_miembro()

    '''
    Metodo que despliega menu principal para administradores
    '''
    def menu_administrador(self):
        while True:
            print("Menú de administrador")
            print("1. Inventario")
            print("2. Usuario")
            print("3. Ganancia")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.inventario.menu_inventario()
            elif opcion == "2":
                self.usuario.menu_cuenta_administrador()
            elif opcion == "3":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "4":
                print("Saliendo de la tienda en línea")
                exit()
            else:
                print("Opción no válida")

    '''
    Metodo que despliegua menu principal para miembros
    '''
    def menu_miembro(self):
        while True:
            print("Menú de miembro")
            print("1. Catálogo")
            print("2. Datos de envío")
            print("3. Pago")
            print("4. Cuenta")
            print("5. Carrito")
            print("6. Comprar")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.catalogo.mostrar_catalogo()
            elif opcion == "2":
                self.datos_envio.menu_datos_envio()
            elif opcion == "3":
                self.pago.menu_pago()
            elif opcion == "4":
                self.usuario.menu_cuenta_miembro()
                if not self.session.esta_autenticado():
                    break
            elif opcion == "5":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "6":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "7":
                print("Saliendo de la tienda en línea")
                print("Gracias por visitarnos")
                exit()
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