from Modelo.G_usuario.Session import Session

class TablaPago:
    def __init__(self):
        '''
        Formato diccionario de datos de pago
        {
            id_usuario1: [Tarjeta1, Tarjeta2, Tarjeta3],
            id_usuario2: [Tarjeta1, Tarjeta2, Tarjeta3]
        }
        '''
        self.__pagos = {}
        self.session = Session()

    _instance = None

    '''
    Metodo que crea una instancia de la clase Session si no existe una ya creada.
    En caso de que ya exista una instancia, regresa la instancia ya creada.
    '''
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialización de la sesión
        return cls._instance

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
    
    def eliminar_tarjeta(self, tarjeta_seleccionada):
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario in self.__pagos:
            self.__pagos[id_usuario].pop(tarjeta_seleccionada)
            return True
        return False

    def tiene_datos_pago(self) -> bool:
        '''Este metodo verifica si el usuario tiene datos de pago

        Returns:
            bool: True si el usuario tiene datos de pago, False si no
        '''
        id_usuario = self.session.obtener_id_usuario()
        if id_usuario in self.__pagos:
            return True
        else:
            return False