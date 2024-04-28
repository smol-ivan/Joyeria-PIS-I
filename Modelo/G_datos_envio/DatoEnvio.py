class DatoEnvio:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, pais):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    def __str__(self):
        return f'{self.nombre}\n {self.direccion}\n {self.ciudad}\n {self.codigo_postal}\n {self.pais}'
    
#arreglo de datos de envio
dato1 = DatoEnvio("Juan Perez", "Calle 123", "CDMX", "12345", "Mexico")
dato2 = DatoEnvio("Maria Lopez", "Calle 456", "GDL", "54321", "Mexico")

arr = [dato1, dato2]

# Iterar sobre el arreglo de datos de envio e imprimir cada uno
for i in range(len(arr)):
    print(f'Dato de envio {i+1}:')
    print(arr[i])

# seleccionar dato envio
index = int(input("Seleccione el dato de envio: "))
index -= 1