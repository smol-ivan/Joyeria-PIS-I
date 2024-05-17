from .UI_Usuario import UI_Usuario
from .UI_DatosEnvio import UI_DatosEnvio
from .UI_Pago import UI_Pago
from .UI_Catalogo import UI_Catalogo
from .UI_Inventario import UI_Inventario
from .UI_Ganancia import UI_Ganancia
from .UI_Carrito import UI_Carrito
from .UI_Compra import UI_Compra
from Modelo.G_usuario.Session import Session

class UI_Principal:
    ''' Esta clase es la encargada de desplegar el menu principal de la tienda en línea
    '''    
    def __init__(self):
        ''' Constructor de la clase UI_Principal. Inicializa las instancias de las clases UI's que se van a utilizar
        '''        
        self.usuario = UI_Usuario()
        self.datos_envio = UI_DatosEnvio()
        self.pago = UI_Pago()
        self.catalogo = UI_Catalogo()
        self.inventario = UI_Inventario()
        self.session = Session()
        self.ganancia = UI_Ganancia()
        self.carrito = UI_Carrito()
        self.compra = UI_Compra()

    def menu_principal(self):
        ''' Metodo que despliega el menu principal y redirige a las opciones seleccionadas
        '''        
        while True:
            print("\n~~ Bienvenido a la tienda en línea ~~\n")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Entrar como invitado")
            print("4. Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.usuario.iniciar_sesion()
                self.desplegar_menu_usuario()
            elif opcion == "2":
                self.usuario.registrarse()
            elif opcion == "3":
                self.catalogo.menu_catalogo()
            elif opcion == "4":
                print("\nSaliendo de la tienda en línea")
                exit()
            else:
                print("\nOpción no válida")

    def desplegar_menu_usuario(self):
        '''Metodo para seleccionar que tipo de menu desplegar
        '''
        if not self.session.esta_autenticado():
            print("No se ha iniciado sesión")
            return
        if self.session.es_administrador():
            self.menu_administrador()
        else:
            self.menu_miembro()

    def menu_administrador(self):
        '''Metodo que despliega menu principal para administradores
        '''
        while True:
            print("\n=== Menú Administrador ===\n")
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
                self.ganancia.menu_ganancia()
            elif opcion == "4":
                print("\nSaliendo de la tienda en línea")
                exit()
            else:
                print("\nOpción no válida")

    def menu_miembro(self):
        '''Metodo que despliegua menu principal para miembros
        '''
        while True:
            print("\n=== Menú Miembro ===\n")
            print("1. Catálogo")
            print("2. Datos de envío")
            print("3. Pago")
            print("4. Cuenta")
            print("5. Carrito")
            print("6. Comprar")
            print("7. Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.catalogo.menu_catalogo()
            elif opcion == "2":
                self.datos_envio.menu_datos_envio()
            elif opcion == "3":
                self.pago.menu_pago()
            elif opcion == "4":
                self.usuario.menu_cuenta_miembro()
                if not self.session.esta_autenticado():
                    break
            elif opcion == "5":
                self.carrito.menu_carrito()
            elif opcion == "6":
                self.compra.menu_compra()
            elif opcion == "7":
                print("\nSaliendo de la tienda en línea")
                print("Gracias por visitarnos")
                exit()
            else:
                print("\nOpción no válida")