from Modelo.G_datos_envio import GestorDatosEnvio

class Controller_DatosEnvio:
    def __init__(self):
        self.gestor_datos_envio = GestorDatosEnvio()

    '''
    Metodo que recibe los datos de envio y los envia al gestor de datos de envio
    '''
    def enviar_datos_agregar_datos_envio(self, nombre, direccion, ciudad, cp, pais):
        return self.gestor_datos_envio.recibir_datos_agregar_datos_envio(nombre, direccion, ciudad, cp, pais)

    '''
    Metodo que solicita los datos de envio al gestor de datos de envio cuando se oprime la opcion de ver datos de envio
    '''
    def obtener_datos_envio(self):
        # Método para buscar un producto en el inventario a través del gestor de inventario
        return self.gestor_datos_envio.obtener_datos_envio()

    '''
    Metodo que solicita al gestor de datos de envio la modificacion de un dato de envio
    '''
    def enviar_modificacion(self, tipo_dato, dato, indice):
        return self.gestor_datos_envio.recibir_modificacion(tipo_dato, dato, indice)

    def enviar_eliminar_dato(self, indice):
        return self.gestor_datos_envio.recibir_eliminar_dato(indice)