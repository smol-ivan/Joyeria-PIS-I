from .DatoEnvio import DatoEnvio
from .TablaDatosEnvio import TablaDatosEnvio


class GestorDatosEnvio:
    def __init__(self):
        self.tabla_datos_envio = TablaDatosEnvio()

    '''
    Metodo que verifica datos de envio
    '''

    def verificar_datos_envio(self, nombre, direccion, ciudad, cp, pais):
        if nombre == "" or direccion == "" or ciudad == "" or cp == "" or pais == "":
            return False
        return True

    '''
    Metodo que recibe los datos de envio
    '''

    def recibir_datos_agregar_datos_envio(self, nombre, direccion, ciudad, cp, pais):
        if self.verificar_datos_envio(nombre, direccion, ciudad, cp, pais):
            dato_envio = DatoEnvio(nombre, direccion, ciudad, cp, pais)
            return self.tabla_datos_envio.agregar_dato_envio(dato_envio)
        return False

    def obtener_datos_envio(self):

        return self.tabla_datos_envio.obtener_datos_envio()

    def recibir_modificacion(self, tipo_dato, dato, indice):
        return self.tabla_datos_envio.modificar_dato(tipo_dato, dato, indice)

    def recibir_eliminar_dato(self, indice):
        return self.tabla_datos_envio.eliminar_dato(indice)





