from Controlador.Controller_DatosEnvio import Controller_DatosEnvio

class UI_DatosEnvio:
    def __init__(self):
        self.controller = Controller_DatosEnvio()

    '''
    Metodo que despliega UI de Datos de Envio
    '''
    def menu_datos_envio(self):
        while True:
            print("Menu de Datos de Envio")
            print("1. Agregar datos de envio")
            print("2. Ver datos de envio")
            print("3. Modificar datos de envio")
            print("4. Eliminar datos de envio")
            print("5. Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.agregar_datos_envio()
            elif opcion == "2":
                self.mostrar_datos_envio()
            elif opcion == "3":
                self.modificar_datos_envio()
                #print("No implementado")
            elif opcion == "4":
                # self.eliminar_datos_envio()
                print("No implementado")
            elif opcion == "5":
                break
            else:
                print("Opcion no valida")

    '''
    Metodo que despliega que despliega la UI para agregar datos de envio y se encuentra a la espera de exito o fracaso de la operacion
    '''
    def agregar_datos_envio(self):
        nombre, direccion, ciudad, cp, pais = self.recibir_datos_envio()
        respuesta = self.controller.enviar_datos_agregar_datos_envio(nombre, direccion, ciudad, cp, pais)
        if respuesta:
            print("Datos de envio agregados exitosamente")
        else:
            print("Error al validar los datos de envio")
            print("¿Desea intentar de nuevo?")
            respuesta = input("S/N: ")
            if respuesta.lower() == "n":
                return

    '''
    Metodo que recibe datos de enivo
    '''
    def recibir_datos_envio(self):
        print("Ingrese los datos de envio")
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
            print("No hay datos de envio")
            return False
        # Iterar sobre datos y mostrarlos en lista
        print("Datos de envio")
        for i, dato in enumerate(datos):
            print(f'Direccion {i+1}\n {dato}\n')
            print("----------------------------")

    '''
    Metodo que obtiene el indice de el dato de envio solicitado
    '''
    def seleccionar_dato_envio(self, datos):
        while True:
            opcion = input("Seleccione una tarjeta: ")
            if opcion.isdigit() and int(opcion) > 0 and int(opcion) < len(datos) + 1:
                return int(opcion)-1 # Regresamos el indice de la tarjeta seleccionada
            else:
                print("Opción no válida")

    '''
    Metodo que despliega la UI para modificar datos de envio
    '''
    def modificar_datos_envio(self):
        print("MODIFICAR DATOS DE ENVIO")
        if self.mostrar_datos_envio():
            return
        datos = self.controller.obtener_datos_envio()
        indice = self.seleccionar_dato_envio(datos)
        tipo_dato, dato = self.seleccionar_dato_modificar()
        respuesta = self.controller.enviar_modificacion(tipo_dato, dato, indice)
        if respuesta:
            print("Dato modificado exitosamente")
        else:
            print("Error al modificar el dato")
            print("¿Desea intentar de nuevo?")
            respuesta = input("S/N: ")
            if respuesta.lower() == "n":
                return

    '''
    Metodo que solicita al usuario que dato de la cuenta desea modificar y el nuevo dato
    '''
    def seleccionar_dato_modificar(self):
        while True:
            print("Seleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Direccion")
            print("3. Ciudad")
            print("4. Codigo Postal")
            print("5. Pais")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "6":
                break
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
            dato = input("Ingrese el nuevo dato: ")
            return tipo_dato, dato
            
