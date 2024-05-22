from Modelo.G_compra.GestorCompra import GestorCompra
from Modelo.G_datos_envio.TablaDatosEnvio import TablaDatosEnvio
from Modelo.G_pago.TablaPago import TablaPago
from Modelo.G_carrito.GestorCarrito import GestorCarrito

class Controller_Compra:
    def __init__(self) -> None:
        self.gestor_compra: GestorCompra = GestorCompra()
        self.tabla_datos_envio: TablaDatosEnvio = TablaDatosEnvio()
        self.tabla_pago: TablaPago = TablaPago()
        pass

    def puede_comprar(self) -> bool:
        '''Este metodo verifica si el usuario tiene datos de envio y de pago

        Returns:
            bool: True si el usuario tiene datos de envio y de pago, False si nos
        '''        
        return self.tabla_datos_envio.tiene_datos_envio() and self.tabla_pago.tiene_datos_pago()   
    
    def realizar_compras(self) -> bool:
        '''Solicutid al gestor de compra que realice la compra
        '''
        if self.gestor_compra.solicitud_compra():
            return True
        else:
            return False