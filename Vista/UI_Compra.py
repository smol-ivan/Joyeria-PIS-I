from Controlador.Controller_Compra import Controller_Compra
from Controlador.Controller_Compra import Controller_Compra

class UI_Compra:
    '''Clase que despliega la interfaz de compras
    '''
    def __init__(self):
        self.controlador = Controller_Compra()

    def menu_compra(self):
        while True:
            print("Sistema de Compras")
<<<<<<< HEAD
            print("1. Verificar Datos de Envío y Pago")
            print("2. Realizar Compra")
            print("3. Salir")
=======
            print("[1] Verificar Datos de Envío y Pago")
            print("[2] Realizar Compra")
            print("[3] Salir")
>>>>>>> 0d22782 ("9:40")

            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.verificar_datos()
            elif opcion == '2':
                self.realizar_compra()
            elif opcion == '3':
                print("Saliendo del sistema de compras.")
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")

    def verificar_datos(self):
        '''Método que verifica si el usuario tiene datos de envío y de pago
        '''
        if self.controlador.puede_comprar():
<<<<<<< HEAD
            print("\nTienes los datos de envío y pago completos. Puedes realizar la compra.\n")
            print(self.controlador.puede_comprar())
        else:
            print("\nNo tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.\n")
=======
            print("Tienes los datos de envío y pago completos. Puedes realizar la compra.")
            print(self.controlador.puede_comprar())
        else:
            print("No tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.")
>>>>>>> 0d22782 ("9:40")

    def realizar_compra(self):
        '''Método que realiza la compra
        '''
        if self.controlador.puede_comprar():
            if self.controlador.realizar_compras():
                print("\nCompra realizada con éxito.\n")
            else:
                print("\nNo se pudo realizar la compra.\n")
        else:
<<<<<<< HEAD
            print("\nNo tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.\n")
=======
            print("No tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.")
>>>>>>> 0d22782 ("9:40")
#1234567890123456