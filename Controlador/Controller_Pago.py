from Modelo.G_pago.GestorPago import GestorPago

class Controller_Pago:
    def __init__(self):
        self.gestor_pago = GestorPago()

    def enviar_datos_bancarios_agregar(self, tipo_tarjeta, numero, fecha_vencimiento, cvv):
        return self.gestor_pago.recibir_datos_bancarios_agregar(tipo_tarjeta, numero, fecha_vencimiento, cvv)
