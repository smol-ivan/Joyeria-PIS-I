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
                print("No implementado")
            elif opcion == "3":
                # self.modificar_datos_envio()
                print("No implementado")
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

        print(datos)

    def modificar_datos_envio(self):
        print("MODIFICAR DATOS DE ENVIO")
        return self.controller.enviar_modificacion()
