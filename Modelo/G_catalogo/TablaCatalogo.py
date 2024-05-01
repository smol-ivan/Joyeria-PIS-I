from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes

class TablaCatalogo():
    def __init__(self):
        self.productos_inventario = None
        self.obtener_productos_inventario()

    def obtener_productos_inventario(self):
        self.productos_inventario = Inventario().obtener_lista_productos()

    def obtener_catalogo(self, tipo_producto):
        lista_productos = []
        for producto in self.productos_inventario:
            if tipo_producto == "Aretes" and isinstance(producto, Aretes):
                lista_productos.append(producto)
            elif tipo_producto == "Collares" and isinstance(producto, Collares):
                lista_productos.append(producto)
            elif tipo_producto == "Anillos" and isinstance(producto, Anillos):
                lista_productos.append(producto)
            elif tipo_producto == "Piercings" and isinstance(producto, Piercings):
                lista_productos.append(producto)
            elif tipo_producto == "Pulseras" and isinstance(producto, Pulseras):
                lista_productos.append(producto)
            elif tipo_producto == "Dijes" and isinstance(producto, Dijes):
                lista_productos.append(producto)
        return lista_productos
    
    '''
    Metodo que regresa una lista de productos que coinciden con el dato de busqueda
    '''
    def buscar_producto(self, dato):
        productos = []
        for producto in self.productos_inventario:
            if producto.get_nombre().lower() == dato.lower() or producto.get_marca().lower() == dato.lower() or producto.get_material().lower() == dato.lower() or producto.get_color().lower() == dato.lower() or producto.get_piedra().lower() == dato.lower():
                productos.append(producto)
        return productos
