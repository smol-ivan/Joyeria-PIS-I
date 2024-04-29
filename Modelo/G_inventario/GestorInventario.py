from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes
class GestorInventario:
    def __init__(self):
        # Inicialización del gestor de inventario con una instancia del inventario
        self.Inventario = Inventario()
        self.inicializar_inventario()

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario utilizando el método correspondiente en el inventario
        self.Inventario.agregar_producto(producto)

    def eliminar_producto(self, nombre_producto):
        # Método para eliminar un producto del inventario utilizando el método correspondiente en el inventario
        self.Inventario.eliminar_producto(nombre_producto)

    def buscar_producto(self, nombre_producto):
        # Método para buscar un producto en el inventario utilizando el método correspondiente en el inventario
        return self.Inventario.buscar_producto(nombre_producto)

    def actualizar_stock(self, nombre_producto, stock):
        # Método para actualizar el stock de un producto en el inventario utilizando el método correspondiente en el inventario
        self.Inventario.actualizar_stock(nombre_producto, stock)
        # Actualizar stock en la lista de productos del catalogo
        for producto in self.Inventario.productos_catalogo:
            if producto.get_nombre() == nombre_producto:
                producto.set_stock(stock)

    def obtener_inventario(self):
        # Método para obtener el inventario completo utilizando el método correspondiente en el inventario
        return self.Inventario.obtener_inventario()

    def inicializar_inventario(self):
        producto1 = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
        producto2 = Collares("Collar de oro", "456DEF", "MarcaY", 5, "Oro", "Dorado", "Diamante", 100)
        producto3 = Anillos("Anillo de plata", "789GHI", "MarcaZ", 15, "Plata", "Plateado", "Zirconia", 30)
        producto4 = Piercings("Piercing de oro", "321JKL", "MarcaW", 3, "Oro", "Dorado", "Diamante", 50)
        producto5 = Pulseras("Pulsera de plata", "654MNO", "MarcaV", 7, "Plata", "Plateado", "Zirconia", 40)
        producto6 = Dijes("Dije de oro", "987PQR", "MarcaU", 2, "Oro", "Dorado", "Diamante", 60)
        producto7 = Aretes("Aretes de oro", "123STU", "MarcaT", 8, "Oro", "Dorado", "Diamante", 80)
        producto8 = Collares("Collar de plata", "456VWX", "MarcaS", 4, "Plata", "Plateado", "Zirconia", 25)
        producto9 = Anillos("Anillo de oro", "789YZA", "MarcaR", 12, "Oro", "Dorado", "Diamante", 70)   
        producto10 = Piercings("Piercing de plata", "321BCD", "MarcaQ", 1, "Plata", "Plateado", "Zirconia", 35)

        self.agregar_producto(producto1)
        self.agregar_producto(producto2)
        self.agregar_producto(producto3)
        self.agregar_producto(producto4)
        self.agregar_producto(producto5)
        self.agregar_producto(producto6)
        self.agregar_producto(producto7)
        self.agregar_producto(producto8)
        self.agregar_producto(producto9)
        self.agregar_producto(producto10)