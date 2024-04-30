from Modelo.G_inventario.Inventario import Inventario

class TablaCatalogo():
    def __init__(self):
        self.productos_inventario = Inventario().obtener_lista_productos()
        '''
        Estructura diccionario
        {
            catalogo_Aretes: Instancia de Catalogo,
            catalogo_Collares: Instancia de Catalogo,
            catalogo_Pulseras: Instancia de Catalogo,
            ...
        }
        '''
        self.catalogos = {}

    def obtener_productos_inventario(self):
        arr = self.productos_inventario
        return arr
    
    def agregar_catalogo(self, catalogo, tipo_producto):
        self.catalogos[tipo_producto] = catalogo

    def obtener_catalogo(self, tipo_producto):
        return self.catalogos[tipo_producto]
