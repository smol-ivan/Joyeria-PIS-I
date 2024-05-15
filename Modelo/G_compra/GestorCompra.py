from Modelo.G_carrito.TablaCarritos import TablaCarritos
from Modelo.G_carrito.Carrito import Carrito
# importar faltantes

class GestorCompra:
    '''Clase que se encarga de gestionar las compras de los usuarios
    '''    
    def __init__(self) -> None:
        # atributos faltantes
        pass

    def obtener_carrito(self) -> Carrito:
        '''Metodo que regresa el ultimo carrito guardado en la tabla de carritos. En caso de no haber carritos guardados, regresa None.

        Returns:
            Carrito: Ultimo carrito guardado
        '''        
        tabla: TablaCarritos = TablaCarritos()
        return tabla.obtener_ultimo_carrito()