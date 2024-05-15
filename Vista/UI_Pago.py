from Controlador.Controller_Pago import Controller_Pago

class UI_Pago:
    def __init__(self):
        self.controlador = Controller_Pago()

    def menu_pago(self):
        ''' Metodo que despliega el menú de pago y redirige a las opciones seleccionadas
        '''        
        while True:
            print("\n=== Menú Pago ===\n")
            print("1. Agregar Tarjeta Bancaria")
            print("2. Modificar Tarjeta Bancaria")
            print("3. Eliminar Tarjeta Bancaria")
            print("4. Mostrar Tarjetas Bancaias")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_tarjeta_bancaria()
            elif opcion == "2":
                self.modificar_tarjeta_bancaria()
            elif opcion == "3":
                self.eliminar_tarjeta_bancaria()
            elif opcion == "4":
                self.mostrar_tarjetas_bancarias()
            elif opcion == "5":
                print("Regresando al menú principal")
                break
            else:
                print("Opción no válida")

    def eliminar_tarjeta_bancaria(self):
        '''Metodo que solicita al controlador eliminar una tarjeta bancaria
        '''
        tarjetas = self.controlador.obtener_tarjetas_bancarias()
        if tarjetas:
            self.mostrar_tarjetas_bancarias()
            print("Seleccione la tarjeta que desea eliminar")
            tarjeta_seleccionada = self.seleccionar_tarjeta(tarjetas)
            respuesta = self.controlador.enviar_datos_bancarios_eliminar(tarjeta_seleccionada)
            if respuesta:
                print("\nTarjeta eliminada exitosamente")
            else:
                print("\nError al eliminar tarjeta")
                print("Regresando al menú principal")
                return
        else:
            print("\nNo hay tarjetas bancarias registradas")
    
    def solicitar_nuevo_dato(self):
        '''Metodo que solicita y recibe del usuario el nuevo dato de la tarjeta bancaria del dato seleccionado
        '''
        while True:
            print("\nSeleccione dato a modificar de la tarjeta")
            print("1. Número")
            print("2. Fecha de vencimiento")
            print("3. CVV")
            opcion = input("\nSeleccione una opción: ")
            if opcion != "1" and opcion != "2" and opcion != "3":
                print("Opción no válida")
            else:
                dato = input("\nIngrese el nuevo dato: ")
                if opcion == "1":
                    tipo = "numero"
                elif opcion == "2":
                    tipo = "fecha_vencimiento"
                else:
                    tipo = "cvv"
                return tipo, dato
            
    def seleccionar_tarjeta(self, tarjetas) -> int:
        '''Metodo que recibe una lista de tarjetas bancarias y solicita al usuario seleccionar una
        
        Args:
            numero (int) : Número de tarjeta bancaria
        '''
        while True:
            opcion = input("\nSeleccione una tarjeta: ")
            if opcion.isdigit() and int(opcion) > 0 and int(opcion) < len(tarjetas) + 1:
                return int(opcion)-1 # Regresamos el indice de la tarjeta seleccionada
            else:
                print("\nOpción no válida")

    def modificar_tarjeta_bancaria(self) -> None:
        '''Metodo que modifica una tarjeta bancaria
        '''
        tarjetas = self.controlador.obtener_tarjetas_bancarias()
        if tarjetas:
            self.mostrar_tarjetas_bancarias()
            print("\nSeleccione la tarjeta que desea modificar")
            tarjeta_seleccionada = self.seleccionar_tarjeta(tarjetas)
            tipo, dato = self.solicitar_nuevo_dato()
            respuesta = self.controlador.enviar_datos_bancarios_modificar(tarjeta_seleccionada, tipo, dato)
            if respuesta:
                print("\nTarjeta modificada exitosamente")
            else:
                print("\nError al modificar tarjeta")
                print("Regresando al menú principal")
                return
        else:
            print("\nNo hay tarjetas bancarias registradas")


    def mostrar_tarjetas_bancarias(self) -> None:
        '''Metodo que solicita al controlador las tarjetas bancarias y las muestra
        '''
        tarjetas = self.controlador.obtener_tarjetas_bancarias()
        if tarjetas:
            print("\n--Tarjetas Bancarias--\n")
            for i, tarjeta in enumerate(tarjetas):
                print("Tarjeta no. ", i+1)
                print("Tipo: ", tarjeta.get_tipo())
                print("Número: ", tarjeta.get_numero())
                print("Fecha de vencimiento: ", tarjeta.get_fecha_vencimiento())
                print("CVV: ", tarjeta.get_cvv())
                print("----------------------------")
        else:
            print("\nNo hay tarjetas bancarias registradas")

    def agregar_tarjeta_bancaria(self) -> None:
        '''Metodo que muestra UI para agregar tarjeta bancaria
        '''
        while True:
            tipo_tarjeta = self.seleccion_tipo_tarjeta()
            numero, fecha_vencimiento, cvv = self.recibir_datos_tarjeta()
            respuesta = self.controlador.enviar_datos_bancarios_agregar(tipo_tarjeta, numero, fecha_vencimiento, cvv)
            if respuesta:
                print("\nTarjeta agregada exitosamente")
                break
            else:
                print("\nDatos no válidos")
                print("Quiere intentar de nuevo? (s/n)")
                opcion = input("Seleccione una opción: ")
                if opcion.lower() == "n":
                    break # Salimos del ciclo

    def recibir_datos_tarjeta(self) -> tuple:
        '''Metodo que recibe los datos de una tarjeta bancaria

        Returns:
            numero: Número de tarjeta
        '''
        print("\nngrese los datos de la tarjeta")
        numero = input("Número de tarjeta: ")
        fecha_vencimiento = input("Fecha de vencimiento: ")
        cvv = input("CVV: ")
        return numero, fecha_vencimiento, cvv
            

    def seleccion_tipo_tarjeta(self) -> str:
        '''Metodo que solicita al usuario seleccionar el tipo de tarjeta

        Returns:
            str: Tipo de tarjeta seleccionada
        '''        
        while True:
            print("\nSeleccione el tipo de tarjeta")
            print("1. Tarjeta de Crédito")
            print("2. Tarjeta de Débito")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                return "credito"
            elif opcion == "2":
                return "debito"
            else:
                print("\nOpción no válida")