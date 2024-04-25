class DatoEnvio:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, pais):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    def __str__(self):
        return f'{self.nombre}\n {self.direccion}\n {self.ciudad}\n {self.codigo_postal}\n {self.pais}'