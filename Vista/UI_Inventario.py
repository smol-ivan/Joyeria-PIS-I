from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes
from Controlador.Controller_Inventario import Controller_Inventario

class UI_Inventario:
    def __init__(self):
        self.controlador = Controller_Inventario()

    def menu_inventario(self):
        while True:
            # Mostrar las opciones del menú principal
            print("\n=== Menú Inventario ===\n")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Buscar producto")
            print("4. Actualizar stock")
            print("5. Mostrar inventario")
            print("6. Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_stock()
            elif opcion == "5":
                self.mostrar_inventario()
            elif opcion == "6":
                break
            else:
                print("\nOpción no válida. \nInténtelo de nuevo.")

    def agregar_producto(self):
        while True:
            # Mostrar los tipos de productos disponibles para agregar
            print("\nTipos de productos disponibles:\n")
            print("1. Aretes")
            print("2. Collares")
            print("3. Anillos")
            print("4. Piercings")
            print("5. Pulseras")
            print("6. Dijes")

            tipo_producto = input("\nSeleccione el tipo de producto: ")

            if tipo_producto not in ["1", "2", "3", "4", "5", "6"]:
                print("\nTipo de producto no válido. Inténtelo de nuevo.")
                continue

            # Solicitar al usuario ingresar los detalles del producto
            nombre = input("Ingrese el nombre del producto: ")
            modelo = input("Ingrese el modelo del producto: ")
            marca = input("Ingrese la marca del producto: ")
            stock = input("Ingrese la cantidad del producto: ")
            material = input("Ingrese el material del producto: ")
            color = input("Ingrese el color del producto: ")
            piedra = input("Ingrese el tipo de piedra del producto: ")
            precio = input("Ingrese el precio del producto: $ ")

            # Validar que stock y precio sean números enteros positivos
            if not stock.isdigit() or not precio.isdigit() or int(stock) < 0 or int(precio) < 0:
                print("\nLa cantidad y el precio deben ser números enteros positivos. \nInténtelo de nuevo.")
                continue

            stock = int(stock)
            precio = int(precio)

            # Crear una instancia del producto según el tipo seleccionado
            if tipo_producto == "1":
                producto = Aretes(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "2":
                producto = Collares(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "3":
                producto = Anillos(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "4":
                producto = Piercings(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "5":
                producto = Pulseras(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "6":
                producto = Dijes(nombre, modelo, marca, stock, material, color, piedra, precio)

            # Agregar el producto al inventario a través del controlador y mostrar un mensaje de confirmación
            self.controlador.agregar_producto(producto)
            print("\nProducto agregado correctamente.")
            break

    def eliminar_producto(self):
        # Solicitar al usuario el nombre del producto a eliminar y eliminarlo del inventario a través del controlador
        nombre_producto = input("\nIngrese el nombre del producto a eliminar: ")
        self.controlador.eliminar_producto(nombre_producto)

    def buscar_producto(self):
        # Solicitar al usuario el nombre del producto a buscar y mostrar el resultado de la búsqueda
        nombre_producto = input("\nIngrese el nombre del producto a buscar: ")
        resultado = self.controlador.buscar_producto(nombre_producto)
        print(resultado)

    def actualizar_stock(self):
        # Solicitar al usuario el nombre del producto y la cantidad adicional para actualizar el stock
        nombre_producto = input("\nIngrese el nombre del producto a actualizar: ")
        stock = int(input("Ingrese la cantidad adicional: "))
        self.controlador.actualizar_stock(nombre_producto, stock)

    def mostrar_inventario(self):
        inventario = self.controlador.obtener_inventario()
        print("\n=== Inventario ===\n")
        for nombre_producto, stock in inventario.items():
            print(f"Nombre: {nombre_producto}\n Stock: {stock}\n")
