from DatoEnvio import DatoEnvio

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
        self.inicializar_datos_envio()

    '''
    Metodo que inicializa los datos de envio
    '''
    def inicializar_datos_envio(self):
        self.tabla_datos_envio.append(DatoEnvio("1", "Calle 123", "CDMX", "12345", "México"))
        self.tabla_datos_envio.append(DatoEnvio("2", "Av. Principal", "Guadalajara", "54321", "México"))
        self.tabla_datos_envio.append(DatoEnvio("3", "Calle 456", "Monterrey", "67890", "México"))
    
    '''
    Metodo que agrega un nuevo dato de envio
    '''
    def agregar_dato_envio(self, id_usuario, dato_envio):
        self.tabla_datos_envio[id_usuario].append(dato_envio)

    '''
    Metodo que obtiene los datos de envio
    '''
    def obtener_datos_envio(self, id_usuario):
        return self.tabla_datos_envio[id_usuario]
    
    '''
    Metodo que modifica un dato de envio
    '''
    def modificar_dato_envio(self, id_usuario, indice, dato_envio):
        self.tabla_datos_envio[id_usuario][indice] = dato_envio

    '''
    Metodo que elimina un dato de envio
    '''
    def eliminar_dato_envio(self, id_usuario, indice):
        self.tabla_datos_envio[id_usuario].pop(indice)