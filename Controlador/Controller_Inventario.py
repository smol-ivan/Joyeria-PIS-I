from Modelo.G_inventario.GestorInventario import GestorInventario

class Controller_Inventario:
    def __init__(self):
        # Inicialización del controlador con instancias del gestor de inventario y la interfaz de usuario
        self.GestorInventario = GestorInventario()

    def iniciar_aplicacion(self):
        # Método para iniciar la aplicación, mostrando el menú principal de la interfaz de usuario
        self.UI_Inventario.menu_inventario()

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario a través del gestor de inventario
        self.GestorInventario.agregar_producto(producto)

    def eliminar_producto(self, nombre_producto):
        # Método para eliminar un producto del inventario a través del gestor de inventario
        self.GestorInventario.eliminar_producto(nombre_producto)

    def buscar_producto(self, nombre_producto):
        # Método para buscar un producto en el inventario a través del gestor de inventario
        return self.GestorInventario.buscar_producto(nombre_producto)

    def actualizar_stock(self, nombre_producto, stock):
        # Método para actualizar el stock de un producto en el inventario a través del gestor de inventario
        self.GestorInventario.actualizar_stock(nombre_producto, stock)

    def obtener_inventario(self):
        # Obtiene el inventario del gestor de inventario
        inventario = self.GestorInventario.obtener_inventario()

        # Devuelve el inventario actualizado
        return self.GestorInventario.obtener_inventario()

