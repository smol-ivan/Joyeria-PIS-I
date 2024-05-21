from .Carrito import Carrito
from .TablaCarritos import TablaCarritos
from Modelo.G_inventario.Inventario import Inventario

class GestorCarrito:
    def __init__(self):
        self.carrito = Carrito()
        self.tabla_carritos = TablaCarritos()

    def guardar_carrito(self) -> None:
        '''Este metodo guarda el carrito de compras en la tabla de carritos
        '''        
        self.tabla_carritos.guardar_carrito(self.carrito)

    def obtener_carrito(self) -> Carrito:
        '''Este metodo obtiene el carrito de compras

        Returns:
            Carrito: Carrito de compras
        '''        
        return self.tabla_carritos.obtener_ultimo_carrito()

    def obtener_total(self) -> float:
        '''Este metodo obtiene el total de la compra

        Returns:
            float: Total de la compra
        '''        
        return self.carrito.obtener_total()

    def agregar_producto(self, identificador: str, cantidad: int) -> bool:
        '''Este metodo recibe y procesa la informacion para agregar un producto al carrito

        Args:
            identificador (str): Modelo/Nombre del producto
            cantidad (int): Cantidad del producto

        Returns:
            bool: True si el producto fue agregado, False si no
        '''        
        inventario = Inventario()
        producto = inventario.obtener_producto(identificador)
        if not producto:
            return False
        self.carrito.agregar_producto(producto, cantidad)
        self.guardar_carrito()
        return True

    def eliminar_producto(self, modelo: str) -> bool:
        '''Este metodo solicita y pasa al gestor la informacion para eliminar un producto del carrito

        Args:
            modelo (str): Modelo que identifica a el producto

        Returns:
            bool: True si el producto fue eliminado, False si no
        '''        
        if not self.carrito:
            return False
        self.carrito.eliminar_producto(modelo)
        self.guardar_carrito()
        return True
    
    def limpiar_carrito(self) -> None:
        '''Este metodo limpia el carrito de compras
        '''        
        self.carrito.limpiar_carrito()
        self.guardar_carrito()