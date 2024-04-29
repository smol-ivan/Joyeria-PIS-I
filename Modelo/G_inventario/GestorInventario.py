from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes
class GestorInventario:
    def __init__(self):
        # Inicialización del gestor de inventario con una instancia del inventario
        self.Inventario = Inventario()

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

    def obtener_inventario(self):
        # Método para obtener el inventario completo utilizando el método correspondiente en el inventario
        return self.Inventario.obtener_inventario()

    def inicializar_inventario(self):
        producto1 = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
        producto2 = Collares("Collar de oro", "456DEF", "MarcaY", 5, "Oro", "Dorado", "Diamante", 100)

        self.agregar_producto(producto1)
        self.agregar_producto(producto2)