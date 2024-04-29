from Modelo.G_usuario.Session import Session
#from Modelo.G_datos_envio.DatoEnvio import DatoEnvio

class TablaDatosEnvio:
    def __init__(self):
        '''
        Formato diccionario de datos de envío
        {
            id_usuario1: [DatoEnvio1, DatoEnvio2, DatoEnvio3],
            id_usuario2: [DatoEnvio1, DatoEnvio2, DatoEnvio3]
        }
        '''
        self.tabla_datos_envio = {}
        self.session = Session()

    '''
    Método que agrega un nuevo dato de envío
    '''
    def agregar_dato_envio(self, dato_envio):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario not in self.tabla_datos_envio:
            self.tabla_datos_envio[id_usuario] = []
        self.tabla_datos_envio[id_usuario].append(dato_envio)
        return True

    '''
    Método que obtiene los datos de envío
    '''
    def obtener_datos_envio(self):
        # Obtener el ID del usuario actual desde la sesión
        id_usuario = self.session.obtener_id_usuario()

        # Verificar si el usuario tiene datos de envío
        if id_usuario in self.tabla_datos_envio:
            return self.tabla_datos_envio[id_usuario]
        else:
            # Si el usuario no tiene datos de envío
            return []

