from Modelo.G_inventario.Producto import Producto

class Carrito:
    def __init__(self) -> None:
        self.productos: dict[
            str: str,
            str: str,
            str: int,
            str: int
            ] = []
        """
        lista de productos esperados:
        productos = [
            {
                "modelo": "modelo",
                "nombre": "nombre",
                "precio": 0.0,
                "cantidad": 0
            }
        ]
        """

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        '''Este metodo agrega un producto al carrito

        Args:
            producto (Producto): Instancia del producto a agregar
            cantidad (int): Cantidad del producto
        '''        
        self.productos.append({
            "modelo": producto.get_modelo(),
            "nombre": producto.get_nombre(),
            "precio": producto.get_precio(),
            "cantidad": int(cantidad)
        })

    def eliminar_producto(self, modelo: str) -> None:
        '''Este metodo elimina un producto del carrito

        Args:
            modelo (str): Modelo que identifica al producto
        '''        
        for producto in self.productos:
            if producto["modelo"] == modelo:
                self.productos.remove(producto)
                break

    def obtener_carrito(self) -> list:
        '''Este metodo obtiene el carrito de compras

        Returns:
            list: Carrito de compras
        '''        
        return self.productos

    def obtener_total(self) -> float:
        '''Este metodo obtiene el total de la compra

        Returns:
            float: Total de la compra
        '''        
        total = 0
        for producto in self.productos:
            total += producto["precio"] * producto["cantidad"]
        return total    
    
    def mostrar_carrito(self) -> None:
        '''Este metodo muestra los productos del carrito
        '''        
        if self.productos:
            print("\n=== Carrito ===\n")
            for producto in self.productos:
                print(f"Producto: {producto['nombre']} Precio: {producto['precio']} Cantidad: {producto['cantidad']}")
            print(f"\nTotal: {self.obtener_total()}")
        else:
            print("\nCarrito vacío")