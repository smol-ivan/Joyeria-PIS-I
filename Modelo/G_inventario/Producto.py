class Producto:
    def __init__(self, nombre:str, modelo:str, marca:str, stock:str, material:str, color:str, piedra:str, precio:int):
        # Inicializa los atributos del producto
        self.nombre: str = nombre
        self.modelo: str = modelo
        self.marca: str = marca
        self.stock: str = stock
        self.material: str = material
        self.color: str = color
        self.piedra: str = piedra
        self.precio: int = precio

    '''
    Metodos get 
    '''
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_modelo(self) -> str:
        return self.modelo
    
    def get_marca(self) -> str:
        return self.marca
    
    def get_stock(self) -> str:
        return self.stock
    
    def get_material(self) -> str:
        return self.material
    
    def get_color(self) -> str:
        return self.color
    
    def get_piedra(self) -> str:
        return self.piedra
    
    def get_precio(self) -> int:
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
