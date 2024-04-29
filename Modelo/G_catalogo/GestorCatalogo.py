from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes
from .TablaCatalogo import TablaCatalogo
from .Catalogo import Catalogo

class GestorCatalogo():
    def __init__(self):
        self.tabla_catalogo = TablaCatalogo()
        self.inicializar_catalogos()

    '''
    Metodo que actualiza los catalogos de productos
    '''
    def actualizar_catalogos(self):
        self.tabla_catalogo = TablaCatalogo()
        self.inicializar_catalogos()

    '''
    Metodo que inicializa los catalogos de productos
    '''
    def inicializar_catalogos(self):
        catalogos = self.crear_catalogos()
        for tipo_producto, catalogo in catalogos.items():
            self.tabla_catalogo.agregar_catalogo(catalogo, tipo_producto)

    def crear_catalogos(self):
        tabla_productos = self.obtener_productos_inventario()
        catalogo_Aretes = Catalogo()
        catalogo_Collares = Catalogo()
        catalogo_Anillos = Catalogo()
        catalogo_Piercings = Catalogo()
        catalogo_Pulseras = Catalogo()
        catalogo_Dijes = Catalogo()

        for producto in tabla_productos:
            if isinstance(producto, Aretes):
                catalogo_Aretes.agregar_producto(producto)
            elif isinstance(producto, Collares):
                catalogo_Collares.agregar_producto(producto)
            elif isinstance(producto, Anillos):
                catalogo_Anillos.agregar_producto(producto)
            elif isinstance(producto, Piercings):
                catalogo_Piercings.agregar_producto(producto)
            elif isinstance(producto, Pulseras):
                catalogo_Pulseras.agregar_producto(producto)
            elif isinstance(producto, Dijes):
                catalogo_Dijes.agregar_producto(producto)

        return {"Aretes": catalogo_Aretes, "Collares": catalogo_Collares, "Anillos": catalogo_Anillos, "Piercings": catalogo_Piercings, "Pulseras": catalogo_Pulseras, "Dijes": catalogo_Dijes}
    
    '''
    Metodo que regresa el catalogo del tipo de producto solicitado
    '''
    def solicitar_catalogo(self, tipo_producto):
        return self.tabla_catalogo.obtener_catalogo(tipo_producto)