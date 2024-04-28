from Modelo.G_usuario.Session import Session

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
    Metodo que inicializa los datos de envio
    '''
    # def inicializar_datos_envio(self
    
    '''
    Metodo que agrega un nuevo dato de envio
    '''
    def agregar_dato_envio(self, dato_envio):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario not in self.tabla_datos_envio:
            self.tabla_datos_envio[id_usuario] = []
        self.tabla_datos_envio[id_usuario].append(dato_envio)
        return True

    '''
    Metodo que obtiene los datos de envio
    '''
    # def obtener_datos_envio(self):
        
    
    '''
    Metodo que modifica un dato de envio
    '''
    # def modificar_dato_envio(self, indice):

    '''
    Metodo que elimina un dato de envio
    '''
    # def eliminar_dato_envio(self, indice):