from Controlador.Controller_Compra import Controller_Compra

class UI_Compra:
    '''Clase que despliega la interfaz de compras
    '''
    def __init__(self):
        self.controlador = Controller_Compra()

    def menu_compra(self):
        while True:
            print("Sistema de Compras")
            print("[1] Verificar Datos de Envío y Pago")
            print("[2] Realizar Compra")
            print("[3] Salir")

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
            print("Tienes los datos de envío y pago completos. Puedes realizar la compra.")
            print(self.controlador.puede_comprar())
        else:
            print("No tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.")

    def realizar_compra(self):
        '''Método que realiza la compra
        '''
        if self.controlador.puede_comprar():
            if self.controlador.realizar_compras():
                print("Compra realizada con éxito.")
            else:
                print("No se pudo realizar la compra.")
        else:
            print("No tienes datos de envío o de pago. Por favor, agrega datos antes de realizar la compra.")
#1234567890123456