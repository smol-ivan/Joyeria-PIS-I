from DatoEnvio import DatoEnvio
from TablaDatosEnvio import TablaDatosEnvio

class GestorDatosEnvio:
    def __init__(self):
        self.tabla_datos_envio = TablaDatosEnvio()
        self.dato_temporal = None

    '''
    Metodo que recibe y crea un nuevo dato de envio
    '''
    def recibe_datos_envio(self, nombre, direccion, ciudad, codigo_postal, pais):
        self.dato_temporal = DatoEnvio(nombre, direccion, ciudad, codigo_postal, pais)

    def agregar_datos_envio(self, id_usuario):
        self.tabla_datos_envio.agregar_dato_envio(id_usuario, self.dato_temporal)

    def obtener_datos_envio(self, id_usuario):
        return self.tabla_datos_envio.obtener_datos_envio(id_usuario)