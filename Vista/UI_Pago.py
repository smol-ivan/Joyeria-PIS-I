from Controlador.Controller_Pago import Controller_Pago

class UI_Pago:
    def __init__(self):
        self.controlador = Controller_Pago()

    def menu_pago(self):
        while True:
            print("Menú de pago")
            print("1. Agregar Tarjeta Bancaria")
            print("2. Modificar Tarjeta Bancaria")
            print("3. Eliminar Tarjeta Bancaria")
            print("4. Mostrar Tarjetas Bancaias")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_tarjeta_bancaria()
            elif opcion == "2":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "3":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "4":
                print("No implementado")
                print("Regresando al menú principal")
            elif opcion == "5":
                print("Regresando al menú principal")
                break
            else:
                print("Opción no válida")

    '''
    Metodo que muestra UI para agregar tarjeta bancaria
    '''
    def agregar_tarjeta_bancaria(self):
        while True:
            tipo_tarjeta = self.seleccion_tipo_tarjeta()
            numero, fecha_vencimiento, cvv = self.recibir_datos_tarjeta()
            respuesta = self.controlador.enviar_datos_bancarios_agregar(tipo_tarjeta, numero, fecha_vencimiento, cvv)
            if respuesta:
                print("Tarjeta agregada exitosamente")
                break
            else:
                print("Datos no válidos")
                print("Quiere intentar de nuevo? (s/n)")
                opcion = input("Seleccione una opción: ")
                if opcion.lower() == "n":
                    break # Salimos del ciclo


    '''
    Metodo que recibe los datos de una tarjeta bancaria
    '''
    def recibir_datos_tarjeta(self):
        print("Ingrese los datos de la tarjeta")
        numero = input("Número de tarjeta: ")
        fecha_vencimiento = input("Fecha de vencimiento: ")
        cvv = input("CVV: ")
        return numero, fecha_vencimiento, cvv
            

    def seleccion_tipo_tarjeta(self):
        while True:
            print("Seleccione el tipo de tarjeta")
            print("1. Tarjeta de Crédito")
            print("2. Tarjeta de Débito")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                return "credito"
            elif opcion == "2":
                return "debito"
            else:
                print("Opción no válida")