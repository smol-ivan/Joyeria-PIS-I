from Modelo.G_compra.Ticket import Ticket

class Reporte:
    def __init__(self, tickets: list[Ticket], identificador: int) -> None:
        self.tickets: list[Ticket] = tickets
        self.identificador: int = identificador

    def obtener_total(self) -> int:
        '''Metodo que obtiene el total de los tickets

        Returns:
            int: Total de los tickets
        '''        
        total: int = 0
        for ticket in self.tickets:
            total += ticket.obtener_total()
        return total
    
    def __str__(self) -> str:
        '''Metodo que da formato a los tickets para mostrar el reporte de ventas

        Returns:
            str: Reporte de ventas
        '''
        reporte: str = ""

        for ticket in self.tickets:
            reporte += f"Ticket: {ticket.id_ticket}, Fecha: {ticket.fecha}\n"
            for producto in ticket.obtener_productos():
                reporte += f"Modelo: {producto['modelo']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}\n"
            reporte += f"Total: {ticket.obtener_total()}\n\n"

        return  reporte

