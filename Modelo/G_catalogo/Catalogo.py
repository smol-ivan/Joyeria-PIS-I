class Catalogo():
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_productos(self):
        return self.productos