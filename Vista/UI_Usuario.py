from Controlador.Controller_Usuario import Controller_Usuario

class UI_Usuario:
    def __init__(self):
        self.controlador_usuario = Controller_Usuario()

    '''
    Metodo que envia los datos de inicio de sesion al gestor de usuario
    '''
    def envia_datos_inicio_sesion(self, correo, contraseña):
        auth = self.controlador_usuario.enviar_datos_iniciar_sesion(correo, contraseña)
        return auth
    
    '''
    Metodo donde se ingresan los datos de inicio de sesion
    '''
    def ingreso_datos_inicio_sesion(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return correo, contraseña
    
    '''
    Metodo despliegua UI para iniciar sesion
    '''
    def iniciar_sesion(self):
        while True:
            print("Iniciar sesión")
            correo, contraseña = self.ingreso_datos_inicio_sesion()
            respuesta_validacion = self.envia_datos_inicio_sesion(correo, contraseña)
            if respuesta_validacion:
                print("Inicio de sesión correcto")
                break
            else:
                print("Correo o contraseña incorrectos")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

    '''
    Metodo que envia los datos de registro al gestor de usuario
    '''
    def envia_datos_registro(self, nombre, correo, contraseña):
        return self.controlador_usuario.enviar_datos_registro_usuario(nombre, correo, contraseña)
    
    '''
    Metodo que recibe los datos de registro
    '''
    def ingreso_datos_registro(self):
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        return nombre, correo, contraseña
        
    '''
    Metodo que despliega UI para registrarse
    '''
    def registrarse(self):
        while True:
            print("Registrarse")
            print("Desea continuar con el proceso de registro?")
            print("S/N:")
            respuesta = input()
            if respuesta.lower() == "n":
                break
            nombre, correo, contraseña = self.ingreso_datos_registro()
            respuesta_validacion = self.envia_datos_registro(nombre, correo, contraseña)
            if respuesta_validacion:
                print("Registro exitoso")
                print("Por favor inicie sesión")
                break
            else:
                print("Correo ya registrado")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

    '''
    Metodo que envia los datos de modificacion al gestor de usuario
    '''
    def envia_datos_modificacion(self, opcion, dato):
        return self.controlador_usuario.enviar_datos_modificacion_usuario(opcion, dato)
    
    '''
    Metodo que muestra el mnenu cuenta Administrador
    '''
    def menu_cuenta_administrador(self):
        while True:
            print("Menú de cuenta de usuario")
            print("1. Modificar cuenta Administrador")
            print("2. Ver datos cuenta Administrador")
            print("3. Eliminar Miembro")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.modificar_usuario_administrador()
            elif opcion == "2":
                self.ver_datos_usuario()
            elif opcion == "3":
                self.eliminar_cuenta_miembro()
            elif opcion == "4":
                break
            else:
                print("Opción no válida")

    '''
    Metodo que despliega UI para eliminar cuenta de miembro
    '''
    def eliminar_cuenta_miembro(self):
        while True:
            print("Eliminar cuenta de miembro")
            respuesta = self.controlador_usuario.boton_eliminar_cuenta_miembro()
            if respuesta:
                print("Cuenta eliminada")
                break
            else:
                print("Operacion cancelada")
                break
    
    '''
    Metodo que muestra el menu cuenta Miembro
    '''
    def menu_cuenta_miembro(self):
        while True:
            print("Menú de cuenta de usuario")
            print("1. Modificar usuario")
            print("2. Ver datos de usuarios")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.modificar_usuario_miembro()
            elif opcion == "2":
                self.ver_datos_usuario()
            elif opcion == "3":
                self.eliminar_cuenta()
                # Si el usuario se elimino, regresar al menu principal
                if not self.controlador_usuario.solicitar_datos_usuario():
                    break
            elif opcion == "4":
                break
            else:
                print("Opción no válida")

    '''
    Metodo que recibe confirmacion de eliminacion de usuario
    '''
    def obtener_confirmacion_eliminacion_usuario(self):
        print("¿Está seguro que desea eliminar el usuario?")
        print("Esta acción no se puede deshacer")
        print("S/N")
        respuesta = input()
        return respuesta.lower() == "s"

    '''
    Metodo que despliega UI para eliminar la propia cuenta
    '''
    def eliminar_cuenta(self):
        while True:
            confirmacion = self.obtener_confirmacion_eliminacion_usuario()
            if confirmacion:
                self.controlador_usuario.boton_eliminar_cuenta()
                print("Usuario eliminado")
                break
            else:
                print("Operacion cancelada")
                break


    '''
    Metodo que el controlador recibe como evento para mostrar los datos del usuario
    Espera recibir un diccionario con los datos del usuario
    '''
    def ver_datos_usuario(self):
        datos = self.controlador_usuario.solicitar_datos_usuario()
        self.mostrar_datos_usuario(datos)


    '''
    Metodo que despliega los datos del usuario, recibe un diccionario con los datos del usuario
    '''
    def mostrar_datos_usuario(self, datos):
        for key, value in datos.items():
            print(f"{key}: {value}")

    '''
    Metodo que despliega UI de modificacion de usuario para el administrador
    '''
    def modificar_usuario_administrador(self):
        while True:
            print("Seleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Correo")
            print("3. Contraseña")
            print("4. Regresar al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "4":
                break
            dato = input("Ingrese el nuevo dato: ")
            respuesta = self.envia_datos_modificacion(int(opcion), dato)
            if respuesta:
                print("Modificación exitosa")
                break
            else:
                print("Error al modificar")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break
            
    '''
    Metodo que despliega UI de modificacion de usuario para el miembro
    '''
    def modificar_usuario_miembro(self):
        while True:
            print("Seleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Correo")
            print("3. Contraseña")
            print("4. Fecha de nacimiento")
            print("5. Genero")
            print("6. Pais")
            print("7. Regresar al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "7":
                break
            dato = input("Ingrese el nuevo dato: ")
            respuesta = self.envia_datos_modificacion(int(opcion), dato)
            if respuesta:
                print("Modificación exitosa")
                break
            else:
                print("Error al modificar")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break