from Modelo.G_datos_envio import GestorDatosEnvio

class Controller_DatosEnvio:
    def __init__(self):
        self.gestor_datos_envio = GestorDatosEnvio()

    '''
    Metodo que recibe los datos de envio y los envia al gestor de datos de envio
    '''
    def enviar_datos_agregar_datos_envio(self, nombre, direccion, ciudad, cp, pais):
        return self.gestor_datos_envio.recibir_datos_agregar_datos_envio(nombre, direccion, ciudad, cp, pais)