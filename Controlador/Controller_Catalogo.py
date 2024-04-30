from Modelo.G_catalogo.GestorCatalogo import GestorCatalogo

class Controller_Catalogo:
    def __init__(self):
        self.gestor_catalogo = GestorCatalogo()

    def boton_mostrar_catalogo(self, tipo_producto):
        catalogo = self.gestor_catalogo.solicitar_catalogo(tipo_producto)
        return catalogo
    
    