class Inventario:
    def __init__(self):
        # Inicializa el diccionario de productos donde se almacenará el inventario
        self.productos = {}
        self.productos_catalogo = []

        '''
    Metodo que crea una instancia de la clase Session si no existe una ya creada.
    En caso de que ya exista una instancia, regresa la instancia ya creada.
    '''
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialización de la instancia del inventario
        return cls._instance  

    def agregar_producto(self, producto):
        # Agrega un producto al inventario o actualiza su stock si ya existe
        if producto.nombre in self.productos:
            self.productos[producto.nombre] += producto.stock
        else:
            self.productos[producto.nombre] = producto.stock
        # Agregar instancia de producto a la lista para el catalogo
        self.productos_catalogo.append(producto)

    def eliminar_producto(self, nombre_producto):
        # Elimina un producto del inventario si existe, de lo contrario, imprime un mensaje
        if nombre_producto in self.productos:
            del self.productos[nombre_producto]
            print("\nProducto eliminado correctamente.")
        else:
            print("\nEl producto no existe en el inventario.")

    def buscar_producto(self, nombre_producto):
        # Busca un producto en el inventario y devuelve su nombre y stock si existe, de lo contrario, devuelve un mensaje
        if nombre_producto in self.productos:
            mensaje = f"{nombre_producto}: {self.productos[nombre_producto]}"
            print("\nProducto encontrado en el inventario.")
            return mensaje
        else:
            return "\nProducto no encontrado."

    def actualizar_stock(self, nombre_producto, stock):
        # Actualiza el stock de un producto en el inventario si existe, de lo contrario, imprime un mensaje
        if nombre_producto in self.productos:
            self.productos[nombre_producto] += stock
        else:
            print("\nEl producto no existe en el inventario.")

    def obtener_inventario(self):
        # Devuelve el inventario de productos
        return self.productos
    
    def obtener_lista_productos(self):
        return self.productos_catalogo
