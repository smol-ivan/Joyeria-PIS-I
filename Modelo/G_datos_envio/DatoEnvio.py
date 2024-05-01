class DatoEnvio:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, pais):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    '''
    Metodos get y set de la clase DatoEnvio
    '''

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    def get_ciudad(self):
        return self._ciudad

    def get_codigo_postal(self):
        return self._codigo_postal

    def get_pais(self):
        return self._pais

    def set_nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = valor

    def set_direccion(self, valor):
        if not valor:
            raise ValueError("La dirección no puede estar vacía")
        self.direccion = valor

    def set_ciudad(self, valor):
        if not valor:
            raise ValueError("La ciudad no puede estar vacía")
        self.ciudad = valor

    def set_codigo_postal(self, valor):
        if not valor:
            raise ValueError("El código postal no puede estar vacío")
        self.codigo_postal = valor

    def set_pais(self, valor):
        if not valor:
            raise ValueError("El país no puede estar vacío")
        self.pais = valor

    def __str__(self):
        return f"Nombre: {self.nombre}\n Direccion:{self.direccion}\n Ciudad:{self.ciudad}\n Codigo Postal:{self.codigo_postal}\n Pais:{self.pais}"

