# import controlador
from Controlador.Controller_Ganancia import Controller_Ganancia
from Modelo.G_ganancia.Reporte import Reporte

class UI_Ganancia:
    '''Clase que despliega la interfaz de ganancias
    '''
    def __init__(self) -> None:
        # controlador como atributo
        self.controlador = Controller_Ganancia()
        pass

    def menu_ganancia(self):
        '''Metodo que despliega el menu de ganancias
        '''
        while True:
            print("Menu de Ganancias")
            print("1.- Consultar Ganancias")
            print("2.- Actualizar reporte de ganancias")
            print("3.- Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.consultar_ganancias()
            elif opcion == "2":
                self.actualizar_reporte()
            elif opcion == "3":
                break
            else:
                print("Opcion no valida")
            
    def consultar_ganancias(self):
        '''Metodo que consulta las ganancias
        '''        
        reporte: Reporte = self.controlador.solicitud_consultar_reporte()
        if reporte:
            print(reporte)
            print(f"Total de ganancias: {reporte.obtener_total()}\n")
        else:
            print("\nNo hay reportes de ganancias\n")

    def actualizar_reporte(self):
        '''Metodo que actualiza el reporte de ganancias
        '''        
        self.controlador.solicitud_actualizar_reporte()
        print("\nReporte actualizado\n")