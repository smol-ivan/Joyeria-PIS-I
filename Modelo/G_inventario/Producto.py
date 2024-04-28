class Producto:
    def __init__(self, nombre, modelo, marca, stock, material, color, piedra, precio):
        # Inicializa los atributos del producto
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca
        self.stock = stock
        self.material = material
        self.color = color
        self.piedra = piedra
        self.precio = precio

class Aretes(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto

class Collares(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto

class Anillos(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto

class Piercings(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto

class Pulseras(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto

class Dijes(Producto):
    pass  # No se añaden atributos o métodos específicos, hereda todo de Producto
