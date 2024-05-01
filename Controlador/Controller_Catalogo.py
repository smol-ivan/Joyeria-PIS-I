from Modelo.G_catalogo.GestorCatalogo import GestorCatalogo

class Controller_Catalogo:
    def __init__(self):
        self.gestor_catalogo = GestorCatalogo()

    def boton_mostrar_catalogo(self, tipo_producto):
        catalogo = self.gestor_catalogo.recibir_dato_catalogo(tipo_producto)
        return catalogo
    
    def boton_buscar_producto(self, dato):
        productos = self.gestor_catalogo.recibir_dato_busqueda(dato)
        return productos