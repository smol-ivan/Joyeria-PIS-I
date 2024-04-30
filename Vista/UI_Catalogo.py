from Controlador.Controller_Catalogo import Controller_Catalogo

class UI_Catalogo:
    def __init__(self):
        self.controller_catalogo = Controller_Catalogo()

    def menu_catalogo(self):
        while True:
            print("1. Mostrar catalogo de Aretes")
            print("2. Mostrar catalogo de Collares")
            print("3. Mostrar catalogo de Anillos")
            print("4. Mostrar catalogo de Piercings")
            print("5. Mostrar catalogo de Pulseras")
            print("6. Mostrar catalogo de Dijes")
            print("7. Regresar al menu principal")
            opcion = input("Seleccione una opcion: ")
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
                print("Opcion no valida")

    def mostrar_catalogo(self, tipo_producto):
        print(f"Catalogo de {tipo_producto}")
        catalogo = self.controller_catalogo.boton_mostrar_catalogo(tipo_producto)
        productos = catalogo.obtener_productos()
        for producto in productos:
            print(producto)