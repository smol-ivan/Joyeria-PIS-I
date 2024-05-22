from Controlador.Controller_Carrito import Controller_Carrito
from Modelo.G_carrito.Carrito import Carrito
from Vista.UI_Compra import UI_Compra

class UI_Carrito:
    def __init__(self) -> None:
        self.controller = Controller_Carrito()
        self.compra = UI_Compra()

    def menu_carrito(self) -> None:
        while True:
            print("\n=== Carrito ===\n")
            print("1. Ver Carrito")
            print("2. Agregar Producto")
            print("3. Eliminar Producto")
            print("4. Realizar Pago")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.ver_carrito()
            elif opcion == "2":
                self.agregar_producto()
            elif opcion == "3":
                self.eliminar_producto()
            elif opcion == "4":
                self.realizar_pago()
            elif opcion == "5":
                print("Regresando al menú principal")
                break
            else:
                print("Opción no válida")

    def ver_carrito(self) -> None:
        carrito = self.controller.obtener_carrito()
        if not carrito:
            print("\nCarrito vacío")
            return
        carrito.mostrar_carrito()

    def agregar_producto(self) -> None:
        '''Este metodo solicita al usuario el id/modelo/nombre del producto a agregar al carrito. Se indica la cantidad a agregar
        '''
        while True:
            print("\n--Agregar producto--\n")
            if not self.controller.solicitar_datos_agregar_producto():
                break
            id_producto = input("Ingrese el id del producto: ")
            cantidad = input("Ingrese la cantidad: ")
            if id_producto and cantidad:
                if self.controller.agregar_producto(id_producto, cantidad):
                    print("\nProducto agregado al carrito")
                else:
                    print("\nProducto no encontrado ó cantidad no valida")
            else:
                print("\nOperacion cancelada")
            opcion = input("\nDesea agregar otro producto? (s/n): ")
            if opcion.lower() == "n":
                break

    def eliminar_producto(self) -> None:
        '''Este metodo muestra los productos del carrito y solicita al usuario el id del producto a eliminar
        '''
        while True:
            print("\n--Eliminar producto--\n")
            carrito = self.controller.obtener_carrito()
            if not carrito:
                print("\nCarrito vacío")
                break
            print("\nProductos en el carrito:")
            # for producto in carrito.obtener_carrito():
            #     print(f"Producto: {producto['nombre']} Precio: {producto['precio']}")
            carrito.mostrar_carrito()
            modelo = input("\nIngrese el modelo del producto a eliminar: ")
            if modelo:
                if self.controller.eliminar_producto(modelo):
                    print("\nProducto eliminado del carrito")
                else:
                    print("\nProducto no encontrado")
            else:
                print("\nOperacion cancelada")
            opcion = input("\nDesea eliminar otro producto? (s/n): ")
            if opcion.lower() == "n":
                break

    def realizar_pago(self) -> None:
        '''Este metodo dirige al usuario a la vista de pago
        '''        
        self.compra.menu_compra()