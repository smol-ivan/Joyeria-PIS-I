from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes, Producto

class Inventario:
    _instance = None
    
    def __init__(self):
        # Inicializa el diccionario de productos donde se almacenará el inventario
        self.productos = {}
        self.productos_catalogo: list[Producto] = []
        self.inicializar_inventario()
        

    '''
    Metodo que crea una instancia de la clase Session si no existe una ya creada.
    En caso de que ya exista una instancia, regresa la instancia ya creada.
    '''
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialización de la instancia del inventario
        return cls._instance 
     
    def inicializar_inventario(self):
        producto1 = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
        producto2 = Collares("Collar de oro", "456DEF", "MarcaY", 5, "Oro", "Dorado", "Diamante", 100)
        producto3 = Anillos("Anillo de plata", "789GHI", "MarcaZ", 15, "Plata", "Plateado", "Zirconia", 30)
        producto4 = Piercings("Piercing de oro", "321JKL", "MarcaW", 3, "Oro", "Dorado", "Diamante", 50)
        producto5 = Pulseras("Pulsera de plata", "654MNO", "MarcaV", 7, "Plata", "Plateado", "Zirconia", 40)
        producto6 = Dijes("Dije de oro", "987PQR", "MarcaU", 2, "Oro", "Dorado", "Diamante", 60)
        producto7 = Aretes("Aretes de oro", "123STU", "MarcaT", 8, "Oro", "Dorado", "Diamante", 80)
        producto8 = Collares("Collar de plata", "456VWX", "MarcaS", 4, "Plata", "Plateado", "Zirconia", 25)
        producto9 = Anillos("Anillo de oro", "789YZA", "MarcaR", 12, "Oro", "Dorado", "Diamante", 70)   
        producto10 = Piercings("Piercing de plata", "321BCD", "MarcaQ", 1, "Plata", "Plateado", "Zirconia", 35)

        self.agregar_producto(producto1)
        self.agregar_producto(producto2)
        self.agregar_producto(producto3)
        self.agregar_producto(producto4)
        self.agregar_producto(producto5)
        self.agregar_producto(producto6)
        self.agregar_producto(producto7)
        self.agregar_producto(producto8)
        self.agregar_producto(producto9)
        self.agregar_producto(producto10)

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
    
    def obtener_producto(self, identificador: str) -> Producto:
        '''Este metodo obtiene un producto del catalogo dado un identificador

        Args:
            identificador (str): Nombre o modelo del producto

        Returns:
            Producto: Producto encontrado en el catalogo
        '''        
        for producto in self.productos_catalogo:
            if producto.get_nombre().lower() == identificador or producto.get_modelo().lower() == identificador:
                return producto
        return None
