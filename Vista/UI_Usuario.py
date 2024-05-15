from Controlador.Controller_Usuario import Controller_Usuario

class UI_Usuario:
    def __init__(self):
        self.controlador_usuario = Controller_Usuario()

    def envia_datos_inicio_sesion(self, correo, contraseña):
        '''Metodo que envia los datos de inicio de sesion al gestor de usuario
        '''
        auth = self.controlador_usuario.enviar_datos_iniciar_sesion(correo, contraseña)
        return auth
    
    def ingreso_datos_inicio_sesion(self):
        '''Metodo donde se ingresan los datos de inicio de sesion
        '''
        correo = input("\nCorreo: ")
        contraseña = input("Contraseña: ")
        return correo, contraseña
    
    def iniciar_sesion(self):
        '''Metodo despliegua UI para iniciar sesion
        '''
        while True:
            print("\nIniciar sesión")
            correo, contraseña = self.ingreso_datos_inicio_sesion()
            respuesta_validacion = self.envia_datos_inicio_sesion(correo, contraseña)
            if respuesta_validacion:
                print("\nInicio de sesión correcto")
                break
            else:
                print("\nCorreo o contraseña incorrectos")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

    def envia_datos_registro(self, nombre, correo, contraseña):
        '''Metodo que envia los datos de registro al gestor de usuario
        '''
        return self.controlador_usuario.enviar_datos_registro_usuario(nombre, correo, contraseña)
    
    def ingreso_datos_registro(self):
        '''Metodo que recibe los datos de registro
        '''
        nombre = input("\nNombre: ")
        correo = input("\nCorreo: ")
        contraseña = input("\nContraseña: ")
        return nombre, correo, contraseña
        
    def registrarse(self):
        '''Metodo que despliega UI para registrarse
        '''
        while True:
            print("\nRegistrarse")
            print("Desea continuar con el proceso de registro?")
            print("S/N:")
            respuesta = input("\n")
            if respuesta.lower() == "n":
                break
            nombre, correo, contraseña = self.ingreso_datos_registro()
            respuesta_validacion = self.envia_datos_registro(nombre, correo, contraseña)
            if respuesta_validacion:
                print("\nRegistro exitoso")
                print("Por favor inicie sesión")
                break
            else:
                print("\nCorreo ya registrado")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break

    def envia_datos_modificacion(self, opcion, dato):
        '''Metodo que envia los datos de modificacion al gestor de usuario
        '''
        return self.controlador_usuario.enviar_datos_modificacion_usuario(opcion, dato)
    
    def menu_cuenta_administrador(self):
        '''Metodo que muestra el mnenu cuenta Administrador
        '''
        while True:
            print("\n=== Menú Administrador - Cuenta ===\n")
            print("1. Modificar cuenta Administrador")
            print("2. Ver datos cuenta Administrador")
            print("3. Eliminar Miembro")
            print("4. Salir")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.modificar_usuario_administrador()
            elif opcion == "2":
                self.ver_datos_usuario()
            elif opcion == "3":
                self.eliminar_cuenta_miembro()
            elif opcion == "4":
                break
            else:
                print("\nOpción no válida")

    def eliminar_cuenta_miembro(self):
        '''Metodo que despliega UI para eliminar cuenta de miembro
        '''
        while True:
            print("\n--Eliminar cuenta de miembro--\n")
            respuesta = self.controlador_usuario.boton_eliminar_cuenta_miembro()
            if respuesta:
                print("\nCuenta eliminada")
                break
            else:
                print("\nOperacion cancelada")
                break
    
    def menu_cuenta_miembro(self):
        '''Metodo que muestra el menu cuenta Miembro
        '''
        while True:
            print("\n=== Menú Cuenta Usuario ===\n")
            print("1. Modificar usuario")
            print("2. Ver datos de usuarios")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("\nSeleccione una opción: ")
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
                print("\nOpción no válida")

    def obtener_confirmacion_eliminacion_usuario(self):
        '''Metodo que recibe confirmacion de eliminacion de usuario
        '''
        print("\n¿Está seguro que desea eliminar el usuario?")
        print("Esta acción no se puede deshacer")
        print("S/N")
        respuesta = input("\n")
        return respuesta.lower() == "s"

    def eliminar_cuenta(self):
        '''Metodo que despliega UI para eliminar la propia cuenta
        '''
        while True:
            confirmacion = self.obtener_confirmacion_eliminacion_usuario()
            if confirmacion:
                self.controlador_usuario.boton_eliminar_cuenta()
                print("\nUsuario eliminado")
                break
            else:
                print("\nOperacion cancelada")
                break

    def ver_datos_usuario(self):
        '''Metodo que el controlador recibe como evento para mostrar los datos del usuario. Espera recibir un diccionario con los datos del usuario
        '''
        datos = self.controlador_usuario.solicitar_datos_usuario()
        self.mostrar_datos_usuario(datos)

    def mostrar_datos_usuario(self, datos):
        '''Metodo que despliega los datos del usuario, recibe un diccionario con los datos del usuario
        '''
        for key, value in datos.items():
            print(f"{key}: {value}")

    def modificar_usuario_administrador(self):
        '''Metodo que despliega UI de modificacion de usuario para el administrador
        '''
        while True:
            print("\nSeleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Correo")
            print("3. Contraseña")
            print("4. Regresar al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "4":
                break
            dato = input("\nIngrese el nuevo dato: ")
            respuesta = self.envia_datos_modificacion(int(opcion), dato)
            if respuesta:
                print("\nModificación exitosa")
                break
            else:
                print("\nError al modificar")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break
            
    def modificar_usuario_miembro(self):
        '''Metodo que despliega UI de modificacion de usuario para el miembro
        '''
        while True:
            print("\nSeleccione dato a modificar de la cuenta")
            print("1. Nombre")
            print("2. Correo")
            print("3. Contraseña")
            print("4. Fecha de nacimiento")
            print("5. Genero")
            print("6. Pais")
            print("7. Regresar al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "7":
                break
            dato = input("\nIngrese el nuevo dato: ")
            respuesta = self.envia_datos_modificacion(int(opcion), dato)
            if respuesta:
                print("Modificación exitosa")
                break
            else:
                print("\nError al modificar")
                print("¿Desea intentar de nuevo?")
                respuesta = input("S/N: ")
                if respuesta.lower() == "n":
                    break