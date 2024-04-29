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

    def modificar_dato(self, opcion, dato):
        # Obtener el ID del usuario actual
        id_usuario = self.session.obtener_id_usuario()
        # Obtener los datos de envío para el usuario actual
        dato_envio = self.tabla_datos_envio[id_usuario]

        if datos_envio:

            # Toma el primer dato de envío para modificar
             # Asegúrate de acceder al objeto correcto

            # Modificar el atributo según la opción
            if opcion == "1":
                # Imprimir el nombre usando el getter}

                print(dato_envio)

            '''
            elif opcion == "2":
                dato_envio.set_direccion(dato)  # Usa el setter para modificar
            elif opcion == "3":
                dato_envio.set_ciudad(dato)
            elif opcion == "4":
                dato_envio.set_codigo_postal(dato)
            elif opcion == "5":
                dato_envio.set_pais(dato)

            return True  # Indicar que la modificación fue exitosa
        else:
            return False  # Si no hay datos de envío para modificar
 '''
#correo1@ejemplo