from Modelo.G_usuario.Session import Session

class TablaPago:
    def __init__(self):
        '''
        Formato diccionario de datos de envío
        {
            id_usuario1: [DatoEnvio1, DatoEnvio2, DatoEnvio3],
            id_usuario2: [DatoEnvio1, DatoEnvio2, DatoEnvio3]
        }
        '''
        self.__pagos = {}
        self.session = Session()

    def agregar_tarjeta(self, tarjeta):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario not in self.__pagos: # Si el usuario no tiene datos de envío
            self.__pagos[id_usuario] = []
        self.__pagos[id_usuario].append(tarjeta) # Agregaramos la tarjeta al usuario
        return True
    
    def obtener_tarjetas(self):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario in self.__pagos:
            return self.__pagos[id_usuario]
        return None
    
    def modificar_tarjeta(self, tarjeta_seleccionada, tipo, dato):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario in self.__pagos:
            if tipo == "numero":
                self.__pagos[id_usuario][tarjeta_seleccionada].set_numero(dato)
            elif tipo == "fecha_vencimiento":
                self.__pagos[id_usuario][tarjeta_seleccionada].set_fecha_vencimiento(dato)
            else:
                self.__pagos[id_usuario][tarjeta_seleccionada].set_cvv(dato)
            return True
        return False