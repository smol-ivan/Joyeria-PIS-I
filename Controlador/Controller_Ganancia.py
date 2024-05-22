from Modelo.G_ganancia.GestorGanancia import GestorGanancia
from Modelo.G_ganancia.Reporte import Reporte

class Controller_Ganancia:
    def __init__(self):
        self.gestor_ganancia = GestorGanancia()

    def solicitud_actualizar_reporte(self) -> None:
        '''Metodo que solicita al gestor de ganancia actualizar los reportes
        '''        
        self.gestor_ganancia.actualizar_reportes()

    def solicitud_consultar_reporte(self) -> Reporte:
        '''Metodo que solicita al gestor de ganancia consultar los reportes

        Returns:
            Reporte: Reportes de ganancia
        '''        
        reporte: Reporte = self.gestor_ganancia.consultar_reportes()
        return reporte