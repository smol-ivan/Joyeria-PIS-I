from .Carrito import Carrito

class TablaCarritos:
    _instance = None

    def __new__ (cls, *args, **kwargs):
        '''Metodo que crea una instancia de la clase TablaCarritos si no existe una ya creada.

        Returns:
            Tipo: TablaCarritos
        '''        
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialización de la tabla de carritos
        return cls._instance

    def __init__ (self) -> None:
        self.carritos: list[Carrito] = []

    def guardar_carrito(self, carrito: Carrito) -> None:
        '''Metodo que guarda un carrito en la tabla de carritoss

        Args:
            carrito (Carrito): Carrito a guardar
        '''        
        self.carritos.append(carrito)

    def obtener_ultimo_carrito(self) -> Carrito:
        '''Metodo que regresa el ultimo carrito guardado en la tabla de carritos. En caso de no haber carritos guardados, regresa None.

        Returns:
            Carrito: Ultimo carrito guardado
        '''        
        return self.carritos[-1] if self.carritos else None