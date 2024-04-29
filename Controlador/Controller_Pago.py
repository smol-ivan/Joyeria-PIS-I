from Modelo.G_pago.GestorPago import GestorPago

class Controller_Pago:
    def __init__(self):
        self.gestor_pago = GestorPago()

    def enviar_datos_bancarios_agregar(self, tipo_tarjeta, numero, fecha_vencimiento, cvv):
        return self.gestor_pago.recibir_datos_bancarios_agregar(tipo_tarjeta, numero, fecha_vencimiento, cvv)

    def obtener_tarjetas_bancarias(self):
        return self.gestor_pago.solicitud_obtener_tarjetas_bancarias()
    
    def enviar_datos_bancarios_modificar(self, tarjeta_seleccionada, tipo, dato):
        return self.gestor_pago.recibir_datos_bancarios_modificar(tarjeta_seleccionada, tipo, dato)
    
    def enviar_datos_bancarios_eliminar(self, tarjeta_seleccionada):
        return self.gestor_pago.recibir_datos_bancarios_eliminar(tarjeta_seleccionada)