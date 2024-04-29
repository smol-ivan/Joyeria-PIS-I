from .TarjetaCredito import TarjetaCredito
from .TarjetaDebito import TarjetaDebito
from .TablaPago import TablaPago

class GestorPago:
    def __init__(self):
        self.__tabla_pago = TablaPago()


    '''
    Metodo que valida los datos necesarios para agregar una tarjeta bancaria
    '''
    def validar_datos(self, numero, fecha_vencimiento, cvv):
        if len(numero) != 16:
            return False
        if len(fecha_vencimiento) != 5:
            return False
        if len(cvv) != 3:
            return False
        return True

    def recibir_datos_bancarios_agregar(self, tipo_tarjeta, numero, fecha_vencimiento, cvv):
        if self.validar_datos(numero, fecha_vencimiento, cvv):
            if tipo_tarjeta == "credito":
                tarjeta = TarjetaCredito(numero, fecha_vencimiento, cvv)
            else:
                tarjeta = TarjetaDebito(numero, fecha_vencimiento, cvv)
            return self.__tabla_pago.agregar_tarjeta(tarjeta)
        return False

    def solicitud_obtener_tarjetas_bancarias(self):
        return self.__tabla_pago.obtener_tarjetas()

    def recibir_datos_bancarios_modificar(self, tarjeta_seleccionada, tipo, dato):
        return self.__tabla_pago.modificar_tarjeta(tarjeta_seleccionada, tipo, dato)
    
    def recibir_datos_bancarios_eliminar(self, tarjeta_seleccionada):
        return self.__tabla_pago.eliminar_tarjeta(tarjeta_seleccionada)

    