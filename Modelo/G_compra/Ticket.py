from Modelo.G_inventario.Producto import Producto

class Ticket:
    def __init__(self, id_ticket: int, fecha: str) -> None:
        self.id_ticket: int = id_ticket
        self.fecha:str = fecha
        self.productos: list[dict[str: any]] = []
        """
        [
            {
                "modelo": "modelo",
                "cantidad": 1,
                "precio": 100
            },
            {
                "modelo": "modelo",
                "cantidad": 1,
                "precio": 100
            }
        ]
        """

    def agregar_producto(self, modelo: str, cantidad: int, precio: int) -> None:
        '''Metodo que agrega un producto al ticket

        Args:
            modelo (str): Modelo del producto
            cantidad (int): Cantidad del producto
            precio (int): Precio del producto
        '''        
        self.productos.append({
            "modelo": modelo,
            "cantidad": cantidad,
            "precio": precio
        })

    def obtener_total(self) -> int:
        '''Metodo que obtiene el total del ticket

        Returns:
            int: Total del ticket
        '''        
        total: int = 0
        for producto in self.productos:
            cantidad = producto["cantidad"]
            total += producto["precio"] * cantidad
        return total
    
    def obtener_productos(self) -> list[dict[str: any]]:
        '''Metodo que obtiene los productos del ticket

        Returns:
            list[dict[str: any]]: Productos del ticket
        '''        
        return self.productos
    
    def __str__(self) -> str:
        '''Metodo que regresa el ticket en formato str

        Returns:
            str: Ticket en formato str
        '''        
        return f"Ticket: {self.id_ticket} - {self.fecha} - {self.obtener_total()}"