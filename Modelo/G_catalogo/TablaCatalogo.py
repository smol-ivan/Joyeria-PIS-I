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
    
    '''
    Metodo que regresa una lista de productos que coinciden con el dato de busqueda
    '''
    def buscar_producto(self, dato):
        productos = []
        for catalogo in self.catalogos.values():
            for producto in catalogo.obtener_productos():
                if producto.get_nombre().lower() == dato.lower() or producto.get_marca().lower() == dato.lower() or producto.get_material().lower() == dato.lower() or producto.get_color().lower() == dato.lower() or producto.get_piedra().lower() == dato.lower():
                    productos.append(producto)
        return productos
