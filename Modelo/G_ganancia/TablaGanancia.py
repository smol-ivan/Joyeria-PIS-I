from .Reporte import Reporte

class TablaGanancia:
    def __init__(self) -> None:
        self.reportes: list[Reporte] = []

    def agregar_reporte(self, reporte: Reporte) -> None:
        '''Metodo que agrega un reporte a la tabla de ganancia

        Args:
            reporte (Reporte): Reporte a agregar
        '''        
        self.reportes.append(reporte)

    def obtener_reportes(self) -> list[Reporte]:
        '''Metodo que obtiene los reportes de la tabla de ganancia

        Returns:
            list[Reporte]: Reportes de la tabla de ganancia
        '''        
        return self.reportes

    def obtener_total(self) -> int:
        '''Metodo que obtiene el total de los reportes

        Returns:
            int: Total de los reportes
        '''        
        total: int = 0
        for reporte in self.reportes:
            total += reporte.obtener_total()
        return total