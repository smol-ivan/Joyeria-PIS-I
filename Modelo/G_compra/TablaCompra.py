from .Ticket import Ticket

class TablaCompra:
    def __init__(self) -> None:
        self.tickets: list[dict[int: list[Ticket]]] = []
        """
        forma de tabla
        [
            {
                1: [ticket1, ticket2]
            },
            {
                2: [ticket3, ticket4]
            }
        ]
        """
        self.init_test()

    
    def agregar_ticket(self, ticket: Ticket, identificador: int) -> None:
        '''Metodo que agrega un ticket a la tabla de compra

        Args:
            ticket (Ticket): Ticket a agregar
            identificador (int): Identificador del usuario
        '''        
        if len(self.tickets) == 0:
            self.tickets.append({
                identificador: [ticket]
            })
        else:
            for i in range(len(self.tickets)):
                if identificador in self.tickets[i]:
                    self.tickets[i][identificador].append(ticket)
                    break
            else:
                self.tickets.append({
                    identificador: [ticket]
                })
    
    def obtener_tickets(self) -> list[dict[int: list[Ticket]]]:
        '''Metodo que obtiene todos los tickets de la tabla de compra

        Returns:
            list[Ticket]: Una lista de todos los tickets de cada usuario
        '''        
        array_tickets = []
        for ticket in self.tickets:
            for key in ticket:
                array_tickets += ticket[key]
        return array_tickets
    
    def init_test(self):
        '''Metodo que inicializa la tabla de compra con tickets de prueba
        '''        
        ticket1 = Ticket(1, "2021-10-10")
        ticket1.agregar_producto("modelo1", 1, 100)
        ticket1.agregar_producto("modelo2", 2, 200)
        self.agregar_ticket(ticket1, 1)
        ticket2 = Ticket(2, "2021-10-11")
        ticket2.agregar_producto("modelo3", 1, 300)
        ticket2.agregar_producto("modelo4", 2, 400)
        self.agregar_ticket(ticket2, 2)