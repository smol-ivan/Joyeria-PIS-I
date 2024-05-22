from Modelo.G_carrito.GestorCarrito import GestorCarrito
from Modelo.G_carrito.Carrito import Carrito

class Controller_Carrito:
    def __init__(self):
        self.carrito = GestorCarrito()

    def solicitar_datos_agregar_producto(self) -> bool:
        return True 

    def obtener_carrito(self) -> Carrito:
        '''Este metodo obtiene el carrito de compras

        Returns:
            Carrito: Carrito de compras
        '''        
        return self.carrito.obtener_carrito()

    def obtener_total(self) -> float:
        '''Este metodo obtiene el total de la compra

        Returns:
            float: Total de la compra
        '''        
        return self.carrito.obtener_total()

    def agregar_producto(self, identificador: str, cantidad: int) -> bool:
        '''Este metodo solicita y pasa al gestor agregar un producto al carrito

        Args:
            identificador (str): Modelo/Nombre del producto
            cantidad (int): Cantidad del producto

        Returns:
            bool: True si el producto fue agregado, False si no
        '''        
        return self.carrito.agregar_producto(identificador, cantidad)

    def eliminar_producto(self, modelo: str) -> bool:
        '''Este metodo solicita y pasa al gestor la informacion para eliminar un producto del carrito

        Args:
            modelo (str): Modelo que identifica a el producto

        Returns:
            bool: True si el producto fue eliminado, False si no
        '''        
        return self.carrito.eliminar_producto(modelo)
