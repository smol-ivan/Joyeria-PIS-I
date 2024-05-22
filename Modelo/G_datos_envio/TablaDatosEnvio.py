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

    def modificar_dato(self, tipo_dato, dato, indice):
        # Obtener el ID del usuario actual
        id_usuario = self.session.obtener_id_usuario()
        # Obtener los datos de envío para el usuario actual
        dato_envio = self.tabla_datos_envio[id_usuario]
        # Modificar el dato de envío
        if tipo_dato == "nombre":
            dato_envio[indice].set_nombre(dato)
        elif tipo_dato == "direccion":
            dato_envio[indice].set_direccion(dato)
        elif tipo_dato == "ciudad":
            dato_envio[indice].set_ciudad(dato)
        elif tipo_dato == "cp":
            dato_envio[indice].set_codigo_postal(dato)
        elif tipo_dato == "pais":
            dato_envio[indice].set_pais(dato)
        return True

    def eliminar_dato(self, indice):
        # Obtener el ID del usuario actual
        id_usuario = self.session.obtener_id_usuario()

        # Verificar que el usuario tenga datos de envío
        if id_usuario in self.tabla_datos_envio:
            datos_envio = self.tabla_datos_envio[id_usuario]

            # Asegurarse de que el índice esté dentro del rango
            if 0 <= indice < len(datos_envio):
                del datos_envio[indice]
                return True

        # Si el índice es inválido o el usuario no tiene datos de envío
        return False

    def tiene_datos_envio(self) -> bool:

            '''Metodo que verifica si el usuario tiene datos de envío

            Returns:
                bool: True si el usuario tiene datos de envío, False si no
            '''
            # Obtener el ID del usuario actual
            id_usuario = self.session.obtener_id_usuario()
            if id_usuario in self.tabla_datos_envio:
                return True
            else:
                return False

#correo1@ejemplo