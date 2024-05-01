from Controlador.Controller_Catalogo import Controller_Catalogo

class UI_Catalogo:
    def __init__(self):
        self.controller_catalogo = Controller_Catalogo()

    def menu_catalogo(self):
        while True:
            print("\n=== Menú Catalogo ===\n")
            print("1. Ver catalogo de productos")
            print("2. Buscar producto")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.menu_mostrar_catalogo()
            elif opcion == "2":
                self.menu_buscar_producto()
            elif opcion == "3":
                print("\nRegresando al menú principal")
                break
            else:
                print("\nOpción no válida")

    '''
    Metodo que solicita y recibe el dato de busqueda del usuario
    '''
    def solicitar_dato_busqueda(self):
        dato = input("\nIngrese el dato de busqueda: ")
        if dato == "" or dato == None:
            print("\nDato de busqueda no valido")
            print("Intente de nuevo la operacion")
            return None
        return dato

    '''
    Metodo que despliega menu de productos a buscar
    '''
    def menu_buscar_producto(self):
        while True:
            print("\n--Buscar producto--\n")
            dato = self.solicitar_dato_busqueda()
            if dato:
                productos = self.controller_catalogo.boton_buscar_producto(dato)
                if productos:
                    for producto in productos:
                        print(producto)
                else:
                    print("\nNo se encontraron productos")
            else:
                print("\nOperacion cancelada")
            opcion = input("\nDesea buscar otro producto? (s/n): ")
            if opcion.lower() == "n":
                break
    
    def menu_mostrar_catalogo(self):
        while True:
            print("\n--Ver catalogo de productos:...---\n")
            print("1. Aretes")
            print("2. Collares")
            print("3. Anillos")
            print("4. Piercings")
            print("5. Pulseras")
            print("6. Dijes")
            print("7. Regresar al menu principal")
            opcion = input("\nSeleccione una opcion: ")
            if opcion == "1":
                self.mostrar_catalogo("Aretes")
            elif opcion == "2":
                self.mostrar_catalogo("Collares")
            elif opcion == "3":
                self.mostrar_catalogo("Anillos")
            elif opcion == "4":
                self.mostrar_catalogo("Piercings")
            elif opcion == "5":
                self.mostrar_catalogo("Pulseras")
            elif opcion == "6":
                self.mostrar_catalogo("Dijes")
            elif opcion == "7":
                break
            else:
                print("\nOpcion no valida")

    def mostrar_catalogo(self, tipo_producto):
        print(f"Catalogo de {tipo_producto}")
        catalogo = self.controller_catalogo.boton_mostrar_catalogo(tipo_producto)
        productos = catalogo.obtener_productos()
        for producto in productos:
            print(producto)