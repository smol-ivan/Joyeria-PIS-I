class Catalogo():
    def __init__(self):
        self.productos = []

    def agregar_productos(self, productos):
        for producto in productos:
            self.productos.append(producto)

    def obtener_productos(self):
        return self.productos
    
    '''
    Metodo que regresa str de los productos en el catalogo con formato
    '''
    def __str__(self):
        productos = ""
        for producto in self.productos:
            nombre = producto.get_nombre()
            modelo = producto.get_modelo()
            precio = producto.get_precio()
            stock = producto.get_stock()
            if stock > 0:
                estado = "Disponible"
            else:
                estado = "Agotado"
            productos += f"Nombre: {nombre}\nModelo: {modelo}\nPrecio: {precio}\nEstado: {estado}\n\n"
        return productos