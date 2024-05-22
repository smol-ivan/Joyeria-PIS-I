from Modelo.G_carrito.TablaCarritos import TablaCarritos
from Modelo.G_carrito.Carrito import Carrito
from Modelo.G_compra.Ticket import Ticket
from Modelo.G_compra.TablaCompra import TablaCompra
import datetime
from Modelo.G_usuario.Session import Session
# importar faltantes

class GestorCompra:
    '''Clase que se encarga de gestionar las compras de los usuarios
    '''    
    def __init__(self) -> None:
        # atributos faltantes
        self.__id_ticket: int = 0
        self.tabla: TablaCompra = TablaCompra()
        self.session: Session = Session()
        self.tabla_carritos: TablaCarritos = TablaCarritos()
        pass

    def obtener_carrito(self) -> Carrito:
        '''Metodo que regresa el ultimo carrito guardado en la tabla de carritos. En caso de no haber carritos guardados, regresa None.

        Returns:
            Carrito: Ultimo carrito guardado
        '''        
        return self.tabla_carritos.obtener_ultimo_carrito()

    def solicitud_compra(self) -> bool:
        carrito: Carrito = self.obtener_carrito()
        print("carrito: ", carrito)
        if not carrito:
            return False
        # Creacion del ticket
        identificador = self.__id_ticket + 1
        fecha = datetime.datetime.now()
        ticket = Ticket(identificador, fecha)
        # Agregar productos al ticket que son sacados del carrito
        for producto in carrito.obtener_carrito():
            ticket.agregar_producto(producto['modelo'], producto['cantidad'], producto['precio'])
        # Guardar ticket
        id_usuario = self.session.obtener_id_usuario()
        self.tabla.agregar_ticket(ticket, id_usuario)
        # limpiar carrito de compra
        self.tabla_carritos.eliminar_carrito()
        return True