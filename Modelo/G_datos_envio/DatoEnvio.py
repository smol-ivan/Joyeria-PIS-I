class DatoEnvio:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, pais):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    @property
    def nombre(self):
            return self._nombre

    @property
    def direccion(self):
            return self._direccion

    @property
    def ciudad(self):
            return self._ciudad

    @property
    def codigo_postal(self):
            return self._codigo_postal

    @property
    def pais(self):
            return self._pais

    @nombre.setter
    def nombre(self, valor):
            if not valor:
                raise ValueError("El nombre no puede estar vacío")
            self._nombre = valor

    @direccion.setter
    def direccion(self, valor):
            if not valor:
                raise ValueError("La dirección no puede estar vacía")
            self._direccion = valor

    @ciudad.setter
    def ciudad(self, valor):
            if not valor:
                raise ValueError("La ciudad no puede estar vacía")
            self._ciudad = valor

    @codigo_postal.setter
    def codigo_postal(self, valor):
            if not valor:
                raise ValueError("El código postal no puede estar vacío")
            self._codigo_postal = valor

    @pais.setter
    def pais(self, valor):
            if not valor:
                raise ValueError("El país no puede estar vacío")
            self._pais = valor

    def __str__(self):
            return f"{self.nombre}, {self.direccion}, {self.ciudad}, {self.codigo_postal}, {self.pais}"


