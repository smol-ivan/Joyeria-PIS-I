from .TarjetaBancaria import TarjetaBancaria

class TarjetaDebito(TarjetaBancaria):
    def __init__(self, numero, fecha_vencimiento, cvv):
        super().__init__(numero, fecha_vencimiento, cvv)
        self.tipo = "Debito"

    '''
    Metodos get
    '''
    def get_tipo(self):
        return self.tipo