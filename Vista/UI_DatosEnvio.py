from Controlador.Controller_DatosEnvio import Controller_DatosEnvio


class UI_DatosEnvio:
    def __init__(self):
        self.controller = Controller_DatosEnvio()

    '''
    Metodo que despliega UI de Datos de Envio
    '''

    def menu_datos_envio(self):
        while True:
            print("\n=== Menú Datos Envio ===\n")
            print("1. Agregar datos de envio")
            print("2. Ver datos de envio")
            print("3. Modificar datos de envio")
            print("4. Eliminar datos de envio")
            print("5. Salir")
            opcion = input("\nSeleccione una opcion: ")
            if opcion == "1":
                self.agregar_datos_envio()
            elif opcion == "2":
                self.mostrar_datos_envio()
            elif opcion == "3":
                self.modificar_datos_envio()
                # print("No implementado")
            elif opcion == "4":
                 self.eliminar_datos_envio()
                #print("No implementado")
            elif opcion == "5":
                break
            else:
                print("\nOpcion no valida")

    '''
    Metodo que despliega que despliega la UI para agregar datos de envio y se encuentra a la espera de exito o fracaso de la operacion
    '''

    def agregar_datos_envio(self):
        nombre, direccion, ciudad, cp, pais = self.recibir_datos_envio()
        respuesta = self.controller.enviar_datos_agregar_datos_envio(nombre, direccion, ciudad, cp, pais)
        if respuesta:
            print("\nDatos de envio agregados exitosamente")
        else:
            print("\nError al validar los datos de envio")
            print("¿Desea intentar de nuevo?")
            respuesta = input("S/N: ")
            if respuesta.lower() == "n":
                return

    '''
    Metodo que recibe datos de enivo
    '''

    def recibir_datos_envio(self):
        print("\nIngrese los datos de envio")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        ciudad = input("Ciudad: ")
        cp = input("Codigo Postal: ")
        pais = input("Pais: ")
        return nombre, direccion, ciudad, cp, pais

    '''
    Metodo que despliega UI para ver los datos de envio
    '''

    def mostrar_datos_envio(self):
        datos = self.controller.obtener_datos_envio()
        # Si datos es un arreglo vacio, entonces no hay datos de envio
        if not datos:
            print("\nNo hay datos de envio")
            return False
        # Iterar sobre datos y mostrarlos en lista
        print("\nDatos de envio")
        for i, dato in enumerate(datos):
            print(f'Direccion {i + 1}\n {dato}\n')
            print("----------------------------")

    '''
    Metodo que obtiene el indice de el dato de envio solicitado
    '''

    def seleccionar_dato_envio(self, datos):
        while True:
            opcion = input("\nSeleccione la direccion que desea modificar:")

            if opcion.isdigit() and int(opcion) > 0 and int(opcion) < len(datos) + 1:
                return int(opcion) - 1  # Regresamos el indice de la tarjeta seleccionada
            else:
                print("O\npción no válida")

    '''
    Metodo que despliega la UI para modificar datos de envio
    '''

    def modificar_datos_envio(self):
        print("\n --Modificar datos envio-- \n")
        if self.mostrar_datos_envio():
            return
        datos = self.controller.obtener_datos_envio()

        indice = self.seleccionar_dato_envio(datos)
        print("1. Nombre")
        print("2. Direccion")
        print("3. Ciudad")
        print("4. Codigo Postal")
        print("5. Pais")
        print("6. Salir")
        opcion = input("\nSeleccione el dato que desea modificar:")

        tipo_dato, dato = self.seleccionar_dato_modificar(opcion)
        respuesta = self.controller.enviar_modificacion(tipo_dato, dato, indice)
        if respuesta:
            print("\nDato modificado exitosamente")
        else:
            print("\nError al modificar el dato")
            print("¿Desea intentar de nuevo?")
            respuesta = input("S/N: ")
            if respuesta.lower() == "n":
                return

    '''
    Metodo que solicita al usuario que dato de la cuenta desea modificar y el nuevo dato
    '''

    def seleccionar_dato_modificar(self, opcion):
        tipo_dato = None  # Inicializar para evitar errores
        dato = None  # Inicializar para evitar errores

        if opcion == "6":
            return None, None

        if opcion == "1":
            tipo_dato = "nombre"
        elif opcion == "2":
            tipo_dato = "direccion"
        elif opcion == "3":
            tipo_dato = "ciudad"
        elif opcion == "4":
            tipo_dato = "cp"
        elif opcion == "5":
            tipo_dato = "pais"

        if tipo_dato:
            dato = input("\nIngrese el nuevo dato: ")
            return tipo_dato, dato  # Retorna siempre una tupla
        else:
            print("\nOpción no válida, intente de nuevo.")
            return None, None  # Devuelve valores vacíos si la opción es inválida

    def eliminar_datos_envio(self ):
        print("\n --Eliminar datos envio-- \n")
        if self.mostrar_datos_envio():
            return
        datos = self.controller.obtener_datos_envio()

        indice = self.seleccionar_dato_envio(datos)
        delete = self.controller.enviar_eliminar_dato(indice)
        if(delete):
            print("\nDato eliminado exitosamente")
        else:
            print("\nError al modificar el dato")
            print("¿Desea intentar de nuevo?")
            respuesta = input("S/N: ")
            if respuesta.lower() == "n":
                return




