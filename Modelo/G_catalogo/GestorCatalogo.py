from .TablaCatalogo import TablaCatalogo
from .Catalogo import Catalogo

class GestorCatalogo():
    def __init__(self):
        self.tabla_catalogo = TablaCatalogo()

    def recibir_dato_catalogo(self, tipo_producto):
        # Crear catalogo con los productos del tipo de producto
        catalogo = Catalogo()
        productos = self.tabla_catalogo.obtener_catalogo(tipo_producto)
        catalogo.agregar_productos(productos)
        return catalogo
    
    def recibir_dato_busqueda(self, dato):
        # Crear catalogo con los productos que coinciden con el dato de busqueda
        catalogo = Catalogo()
        productos = self.tabla_catalogo.buscar_producto(dato)
        catalogo.agregar_productos(productos)
        return catalogo