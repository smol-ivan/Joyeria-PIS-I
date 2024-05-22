from .TablaGanancia import TablaGanancia
from .Reporte import Reporte
from Modelo.G_compra.Ticket import Ticket
from Modelo.G_compra.TablaCompra import TablaCompra

class GestorGanancia:
    def __init__ (self) -> None:
        self.tabla: TablaGanancia = TablaGanancia()
        self.__identificador: int = 0

    def prepara_tickets(self) -> list[Ticket]:
        '''Metodo que accede a la la tabla de compras y obtiene los ultimos tickets vendidos, los 5 mas recientes
        '''
        tabla_compra: TablaCompra = TablaCompra()
        tickets: list[Ticket] = tabla_compra.obtener_tickets()
        if len(tickets) > 5:
            return tickets[-5:]
        else: 
            return tickets
        
    def generar_reporte(self) -> Reporte:
        '''Metodo que genera un reporte de ganancias a partir de los tickets obtenidos
        '''
        identidicador: int = self.__identificador + 1 
        self.__identificador = identidicador
        tickets: list[Ticket] = self.prepara_tickets()
        reporte: Reporte = Reporte(tickets, identidicador)
        return reporte
    
    def guardar_reporte(self, reporte: Reporte) -> None:
        '''Metodo que guarda un reporte en la tabla de ganancia
        '''
        self.tabla.agregar_reporte(reporte)

    def actualizar_reportes(self) -> None:
        '''Metodo que actualiza los reportes de ganancias
        '''
        reporte: Reporte = self.generar_reporte()
        self.guardar_reporte(reporte)

    def consultar_reportes(self) -> Reporte:
        '''Consulta el ultimo reporte de ganancias
        [reporte, reporte, reporte]
        '''
        reportes: list[Reporte] = self.tabla.obtener_reportes()
        if len(reportes) > 0:
            return reportes[-1]
        else:
            return []
        