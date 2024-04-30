class TarjetaBancaria:
    def __init__(self, numero, fecha_vencimiento, cvv):
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv

    '''
    Metodos get y set
    '''
    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero

    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento
    
    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def get_cvv(self):
        return self.cvv
    
    def set_cvv(self, cvv):
        self.cvv = cvv