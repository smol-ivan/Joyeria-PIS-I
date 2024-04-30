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

    '''
    Metodos get 
    '''
    def get_nombre(self):
        return self.nombre
    
    def get_modelo(self):
        return self.modelo
    
    def get_marca(self):
        return self.marca
    
    def get_stock(self):
        return self.stock
    
    def get_material(self):
        return self.material
    
    def get_color(self):
        return self.color
    
    def get_piedra(self):
        return self.piedra
    
    def get_precio(self):
        return self.precio
    
    '''
    Metodos set
    '''
    def set_stock(self, stock):
        self.stock = stock
    
    def __str__(self):
        # Define la representación en cadena de texto del producto
        return f"Nombre: {self.nombre}\nModelo: {self.modelo}\nMarca: {self.marca}\nStock: {self.stock}\nMaterial: {self.material}\nColor: {self.color}\nPiedra: {self.piedra}\nPrecio: {self.precio}"

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
