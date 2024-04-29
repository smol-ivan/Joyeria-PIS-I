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
                self.ver_datos_envio()
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
    '''
    def ver_datos_envio(self):

        print("Visualizar datos de envío")
        datos = self.controller.obtener_envio()
        # Si datos es un arreglo vacio, entonces no hay datos de envio
        if not datos:
            print("No hay datos de envio")
            return
        # Iterar sobre datos y mostrarlos en lista
        for i in range(len(datos)):
            print(len(datos))
            print(f"Direccion{i+1}\n {datos[i]}")

    def modificar_datos_envio(self):
        print("MODIFICAR DATOS DE ENVIO")
        while True:
            print("Seleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Direccion")
            print("3. Ciudad")
            print("4. Codigo Postal")
            print("5. Pais")
            print("6. Salir")
            op = input("Seleccione una opción: ")
            if op == "6":
                break
            dato = input("Ingrese el nuevo dato: ")
            respuesta = self.controller.enviar_modificacion(op, dato)

            if respuesta:
                print("Modificación exitosa")
                print(respuesta)

                break
            else:
                print("Error al modificar")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

