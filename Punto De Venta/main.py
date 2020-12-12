from BaseDeDatos import BaseDeDatos,Error #importamos la base de datos y la clase error para capturar cualquier excepccion con la base de datos
from VentanaPuntoDeVenta import Ui_VentanaPuntoDeVenta #Ventana del punto de venta
from VentanaLogin import Ui_VentanaLogin #Ventana de login
from VentanaRegistro import Ui_VentanaRegistro #ventana de registo
from VentanaAgregarProducto import Ui_VentanaAgregarProducto #Ventana de agregar producto
from PyQt5 import QtWidgets #importamos los widgets
import sys #importamos sistema
from os import environ #Para solucionar el error de los warnings(solo a mi (omar) le pasa)
import PyQt5.QtCore  #Qtcore, muy importante para colocar Flags y diferentes propiedades
from datetime import datetime
from style import login,venta,registro,registro_producto

#caracteres especiale y letras contiene todos los posibles valores invalidos a la hora de captura de informacion
caracteres_especiales = ["°","|","!","\"","#","$","%","&","/","(",")","=","?","\'","¿","¡","+","-","*","/",".",",",";",":",">","<","-","_"]
letras = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
# Si funciona este metodo tener todas las demas clases por separado
# todas las ventanas aparte y trabajar con main para su manipulacion
def singleton(myClass): #clase que nos dio el profe para que no se multipliquen ventanas
    instances = dict()
    
    def wrap(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    
    return wrap
###########REGLASE DE DEFINICION DE FUNCIONES Y METODOS#######


#CLASE DE LA INTERFAZ DE Login
@singleton #metodo de la clase para no repetir ventanas
class VentanaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.interfaz_login = Ui_VentanaLogin()
        self.interfaz_login.setupUi(self)
        self.setWindowTitle("Login")
        self.inicializar_interfaz_login()#Carga todos los elementos por defecto de la ventana login
        self.setStyleSheet(login)
        #base de datos solo hace consultos, lleva parametros de afuerzas
    
    def inicializar_interfaz_login(self):
        self.interfaz_login.User.setText("Usuario")
        self.interfaz_login.Password.setText("Contraseña")
        self.interfaz_login.BotonLogin.mousePressEvent = self._login_  #nueva ventanas
        self.interfaz_login.BotonRegistro.mousePressEvent = self._registro_  #nueva ventana
        self.interfaz_login.User.mouseDoubleClickEvent = self.limpiarLineUser  #limpiar lineEdit
        self.interfaz_login.Password.mouseDoubleClickEvent = self.limpiarLinePassword  #limpiar lineEdit
        self.interfaz_login.User.textChanged.connect(self.estadoBotonLogin)  #Comprobar que puedes iniciar sesion
        self.interfaz_login.Password.textChanged.connect(self.estadoBotonLogin)  #Comprobar que puedes iniciar sesion

    #Limpiar lineEdit
    def limpiarLineUser(self, event):#limpia el line de user con doble click
        self.interfaz_login.User.setText("")

    def limpiarLinePassword(self, event):#limpia el line de user con doble click
        self.interfaz_login.Password.setText("")

    #Dejarte iniciar sesion
    def estadoBotonLogin(self): #comprueba que el texto de user/password no sea vacio, para dejarte iniciar sesion
        if len(self.interfaz_login.Password.text()) != 0 and len(
                self.interfaz_login.User.text()) != 0:
            self.interfaz_login.BotonLogin.setEnabled(True)
        else:
            self.interfaz_login.BotonLogin.setEnabled(False)

    #Tratar de iniciar sesion
    def _login_(self, event):#Iniciar sesion
        try:#Si en la base de datos esta el user y password ingresados,te puedes loguear
                assert base_de_datos.loginUser(str(self.interfaz_login.User.text()),str(self.interfaz_login.Password.text())) , "Nombre/Contraseña de usuario incorrecta"
                ventana_login.close()
                ventana_punto_de_venta.inicializar_interfaz_punto_de_venta()
                ventana_punto_de_venta.interfaz_punto_de_venta.TablaDeVentas.setRowCount(0)#Esto es para que al entrar en el punto de venta se borre los datos anteriores
                ventana_punto_de_venta.interfaz_punto_de_venta.TablaConsultarProducto.setRowCount(0)#Elimina todas las filas
                ventana_punto_de_venta.interfaz_punto_de_venta.TablaDeVentas.removeRow(0)#Esto es para que al entrar en el punto de venta se borre los datos anteriores
                ventana_punto_de_venta.interfaz_punto_de_venta.TablaConsultarProducto.removeRow(0)#Elimina todas las filas
                ventana_punto_de_venta.setWindowTitle(f"Punto de Venta | {self.interfaz_login.User.text()}")#Nombre de ventana personalizado para cada usuario
                ventana_punto_de_venta.interfaz_punto_de_venta.LayoutNombreDeUsuario.setText(f"  Usuario: {self.interfaz_login.User.text()}")#Nombre de ventana personalizado para cada usuario
                ventana_punto_de_venta.user = self.interfaz_login.User.text()
                ventana_punto_de_venta.show()#se muestra la ventana
                #constructor de login
        except AssertionError as msj:#si no se completo el inicio de sesion se levanta una excepcion
            QtWidgets.QMessageBox.information(self," ",f"{msj}")
        except Error as msj:#Si ocure un error con la base de datos levanta una excepccion
            QtWidgets.QMessageBox.information(self,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ")        

    #Registrar un nuevo usuario ver que pedo con los hide y show
    def _registro_(self, event):#ventana de registro, cierra login y carga registro, junto con una inicializacion
        ventana_login.close()
        ventana_registro_usuario.show()
        ventana_registro_usuario.inicializar_interfaz_registro()

#CLASE DE LA INTERFAZ DE Registro
@singleton#unica instancia
class VentanaRegistroUsuario(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.interfaz_registro_usuario = Ui_VentanaRegistro()
        self.interfaz_registro_usuario.setupUi(self)
        self.setStyleSheet(registro)#le asignamos el estilo ala ventana de registo
        self.setWindowTitle("Registro")
        self.inicializar_interfaz_registro()#Aplica los valores por defecto de la ventana
        self.interfaz_registro_usuario.BotonRealizarRegistro.setEnabled(False)#Desactiva el boton de registro

    def inicializar_interfaz_registro(self):
        self.volver = True #Puedes volver al menu si no haz movido nada
        self.interfaz_registro_usuario.User.setText("Ingrese su nombre de usuario")#inicializamos texto
        self.interfaz_registro_usuario.Password.setText("Ingrese su contraseña")#inicializamos texto
        self.interfaz_registro_usuario.BotonRealizarRegistro.mousePressEvent = self._realizar_registro_#Registrar en database
        self.interfaz_registro_usuario.BotonVolver.mousePressEvent = self._volver_ #volver a login
        self.interfaz_registro_usuario.User.mouseDoubleClickEvent = self.limpiarLabelUser #limpiar labelUser
        self.interfaz_registro_usuario.Password.mouseDoubleClickEvent = self.limpiarLabelPassword#limpiar labelPassword
        self.interfaz_registro_usuario.User.textChanged.connect(self.estadoBotonRegistrar)#Dejarte registrar
        self.interfaz_registro_usuario.Password.textChanged.connect(self.estadoBotonRegistrar)#Dejarte registrar

    def _realizar_registro_(self,event):
        try:
            for i in self.interfaz_registro_usuario.User.text():#toma todo el texto del line de user y verifica que no contenga caracteres especiales
                assert i not in caracteres_especiales[::] ,"El nombre de usuario no debe contener caracteres especiales"#verifica que el texto no contenga caracteres especiall
            assert len(self.interfaz_registro_usuario.User.text()) > 0 , "Nombre de usuario invalido"#verifica que tenga texto el line
            assert len(self.interfaz_registro_usuario.Password.text()) > 0 , "Contraseña invalida"#verifica que tenga texto el line
            assert len(self.interfaz_registro_usuario.User.text()) < 30,"La longitud del nombre de usuario debe ser de 30 caracteres o menos "#verifica que el texto sea menor de 30 caracteres
            assert len(self.interfaz_registro_usuario.Password.text()) < 30,"La longitud de la contraseña debe ser de 30 caracteres o menos "#verifica que el texto sea menor de 30 caracteres
            assert base_de_datos.comoprobarUser(self.interfaz_registro_usuario.User.text()),f"Ya existe un usuario registrado como: {self.interfaz_registro_usuario.User.text()}"#comprueba que no hay otro usuario con ese nick en la database
            assert base_de_datos.registrarUser(str(self.interfaz_registro_usuario.User.text()), str(self.interfaz_registro_usuario.Password.text())) , "No se pudo completar el registro"#Una vez todo comprobado te deja registrar al usuario
            QtWidgets.QMessageBox.information(self," ","Registro exitoso",)#AGREGAR ICONO
            self.volver = False #volver se vuelve false lo que elimina la opcion de cancelar registro
            ventana_registro_usuario.close()#se cierra la ventana de registro
            ventana_login.show()#se muestra la ventana de login
            ventana_login.inicializar_interfaz_login()#se inicializa la ventana de login
        except AssertionError as msj:#alguna excepcion devuelve un assertion error con msj como parametro
            QtWidgets.QMessageBox.information(self,"Error de Registro",f"{msj}")#AGREGAR ICONO
            
    def _volver_(self,event):#vuelve ala ventana de login
        self.volver = False #volver se vuelva false lo que te evita que te muestre el mensaje de cancelar registro
        ventana_registro_usuario.close() #se cierra la ventana de registro
        ventana_login.show() #se muestra la ventana de login
        ventana_login.inicializar_interfaz_login() #se inicializa la ventana de login

    def limpiarLabelUser(self,event):#limpia el texto de user
        self.interfaz_registro_usuario.User.setText("")

    def limpiarLabelPassword(self,event):#limpia el texto de password
        self.interfaz_registro_usuario.Password.setText("")
    
    #Dejarte Registrar
    def estadoBotonRegistrar(self):#verifica que puedas acceder al boton registrarte
        if len(self.interfaz_registro_usuario.Password.text()) != 0 and len(self.interfaz_registro_usuario.User.text()) != 0:#si el tamaño de ambos es diferente de 0 te deja oprimir el boton
            self.interfaz_registro_usuario.BotonRealizarRegistro.setEnabled(True)
        else:
            self.interfaz_registro_usuario.BotonRealizarRegistro.setEnabled(False)#si no, queda en falso

    #cerrar ventana
    def closeEvent(self, event):#te muestra un QMessageBox.question para saber si realmente desas salir
        if self.volver:#AGREGAR ICONO
            opcion = QtWidgets.QMessageBox.question(self, " ", "¿Estás seguro que quieres cancelar el registro?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if opcion == QtWidgets.QMessageBox.Yes:#si presionas yes
                ventana_registro_usuario.close()#se cierra la entana de registro
                ventana_login.show() #se muestra la ventana de login
                ventana_login.inicializar_interfaz_login() #se inicializa login
            else:
                event.ignore()#si presionas no, simplemente se ignora el evento



@singleton   #Genera una unica instancia de clase
class VentanaPuntoDeVenta(QtWidgets.QMainWindow):#clase de la ventana de punto de ventga

    #NOTAS
    #ACTUALIZAR PRODUCTOS SE HACE CON EL BOTON DE ACTUALIZAR

    def __init__(self):
        super().__init__()
        self.interfaz_punto_de_venta = Ui_VentanaPuntoDeVenta()
        self.interfaz_punto_de_venta.setupUi(self)
        self.inicializar_interfaz_punto_de_venta()#se inicializa la interfaz de punto de venta
        self.user = str() #nombre del usuario
        self.setStyleSheet(venta) #asigna la hoja de estilos ala ventana
        #self.
    def inicializar_interfaz_punto_de_venta(self):
        #MENUS
        self.salir = True #salir se vuelve true lo que te permite cerrar sesion si que te muestre el mensaje de salir
        self.tengoProductos = False #como se acaba de inicializar, no tienes ningun producto
        self.total_productos = 0 #tal iniciar tienes 0 productos
        self.interfaz_punto_de_venta.TablaDeVentas.setAlternatingRowColors(True) #cambiar colores
        self.interfaz_punto_de_venta.menuPunto_de_venta.mousePressEvent = self._mostrarPuntoDeVenta_ #mostrar frame al tocar el boton
        self.interfaz_punto_de_venta.menuInventario.mousePressEvent = self._mostrarInventario_ #mostrar frame al tocar el boton
        self.interfaz_punto_de_venta.menuTickets.mousePressEvent = self._mostrarTickets_ #mostrar frame al tocar el boton
        self.interfaz_punto_de_venta.FrameInventario.setVisible(False) #ocultar frame inventario
        self.interfaz_punto_de_venta.FrameTickets.setVisible(False) #ocultar frame tickets
        self.interfaz_punto_de_venta.menuPunto_de_venta.setEnabled(False) #activar boton punto de venta
        self.interfaz_punto_de_venta.BotonCerrarSesion.mousePressEvent = self.cerrarSesion#cerrar sesion actual
        self.interfaz_punto_de_venta.BotonRealizarPago.mousePressEvent = self.realizarPago

        #MENUS 
        #INTERFAZ PUNTO DE VENTA-FRAME VENTAS
        self.interfaz_punto_de_venta.TablaConsultarProducto.setDragEnabled(True) #tabla consultar puede arrojar objetos
        self.interfaz_punto_de_venta.TablaDeVentas.setAcceptDrops(True) #tabla de ventas puede recibir objetos
        self.interfaz_punto_de_venta.TablaDeVentas.setColumnWidth(0,60) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeVentas.setColumnWidth(1,280) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeVentas.setColumnWidth(2,108) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeVentas.setColumnWidth(3,90) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeVentas.setColumnWidth(4,100) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaConsultarProducto.setColumnWidth(0,80) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaConsultarProducto.setColumnWidth(1,150) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaConsultarProducto.setColumnWidth(2,110) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaConsultarProducto.setColumnWidth(2,100) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeVentas.mouseDoubleClickEvent = self.actualizarTotal #cuando das doble click sobre tabla de ventas se actualiza el total
        QtWidgets.QDoubleSpinBox.mouseDoubleClickEvent = self.actualizarTotal #Cuando das doble click sobre un spin box se actualiza el total
        self.interfaz_punto_de_venta.TablaDeVentas.dropEvent = self.agregarProducto #Cuando se hace un drop event se llama ala funcion de agregar producto
        self.interfaz_punto_de_venta.TablaDeVentas.keyPressEvent = self.eliminarProducto #cuando se presiona una tecla se llama ala funcion de eliminar producto si la tecla es suprimir
        self.interfaz_punto_de_venta.LineBuscarProductoPuntoDeVenta.setText("Ingrese el producto a buscar: ") #asignamos un texto por defecto al line de buscar producto
        self.interfaz_punto_de_venta.LabelCostoTotal.setText("$ 0.0") #asignamos un texto por defecto al costo total
        self.interfaz_punto_de_venta.LabelUnidadProductos.setText("0 Unidades") #asignamos un texto por defecto al total de unidades
        self.interfaz_punto_de_venta.LineBuscarProductoPuntoDeVenta.textChanged.connect(self.actualizarBusquedaProducto) #actualizar busqueda cada vez que cabia el texto
        self.interfaz_punto_de_venta.LineBuscarProductoPuntoDeVenta.mouseDoubleClickEvent = self.limpiarLabelBusquedaVenta #cuando se da doble click sobre el line de buscar se limpia el texto

        #INTERFAZ PUNTO DE VENTA-FRAME VENTAS

        #INTERFAZ PUNTO DE VENTA-FRAME Inventario
        self.interfaz_punto_de_venta.TablaDeInventario.setColumnWidth(0,100) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeInventario.setColumnWidth(1,520) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeInventario.setColumnWidth(2,250) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeInventario.setColumnWidth(3,124) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeInventario.setDragEnabled(True) #Puede arrojar elementos que tenga en sí.
        self.interfaz_punto_de_venta.LineBuscarProductoInventario.textChanged.connect(self.actualizarBusquedaInventario) #cuando el texto del line buscar producto cambia llama ala funcion de actualizar busqueda de inventario
        self.interfaz_punto_de_venta.LineBuscarProductoInventario.mouseDoubleClickEvent = self.limpiarLabelBusquedaInventario #cuando se da doble click sobre el line de buscar limpia el texto
        self.interfaz_punto_de_venta.TablaDeInventario.keyPressEvent =  self.modificarInventario #cuando se presiona una tecla dentro de la tabla de inventario se llama ala funcion modificar inventario
        self.interfaz_punto_de_venta.BotonAgregarProducto.mousePressEvent = self._agregar_producto_ #cuando se presiona el boton de agregar producto llama ala interfaz de agregar producto
        #INTERFAZ PUNTO DE VENTA_FRAME Inventario

        #INTERFAZ PUNTO DE VENTA-FRAME Tickets
        self.interfaz_punto_de_venta.TablaDeTickets.setColumnWidth(0,60) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeTickets.setColumnWidth(1,550) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeTickets.setColumnWidth(2,150) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeTickets.setColumnWidth(3,169) #tamaño de columnas
        self.interfaz_punto_de_venta.TablaDeTickets.setColumnWidth(4,180) #tamaño de columnas
        self.interfaz_punto_de_venta.LineBuscarTickets.textChanged.connect(self.actualizarBusquedaIickets)#llama ala funcion de buscar ticket cuando cambia el texto del line
        self.interfaz_punto_de_venta.LineBuscarTickets.mouseDoubleClickEvent = self.limpiarLabelBusquedaTickets #limpia el line de tickets cuando se da doble click
        QtWidgets.QPushButton.mousePressEvent = self.mostrarTicket #cuando se da click sobre un boton de la tabla muestra su ticket
#CERRAR SESION    
    def cerrarSesion(self,event):#funcion de cerrar sesion
        opcion = QtWidgets.QMessageBox.question(self, " ", "¿Esta seguro que desea cerrar sesion?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if opcion == QtWidgets.QMessageBox.Yes: #si el question fue yes
            self.salir = False #salir evita que se llame a close
            self.tengoProductos = False #cuando sales se borran todos los productos
            self._mostrarPuntoDeVenta_(self.cerrarSesion) #se llama al evento mostrar punto de venta con el evento cerrar sesion
            ventana_punto_de_venta.close() #se cierra la ventana de punto de venta
            ventana_login.inicializar_interfaz_login()# se inicializa la ventana de login
            ventana_login.show() #se muestra la ventana de login


#cerrar ventana
    def closeEvent(self, event): # se llama a este evento cuando se cierra la pestaña
        if self.salir:#AGREGAR ICONO
            reply = QtWidgets.QMessageBox.question(self, " ", "¿Esta seguro que desea salir?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes :
                event.accept()
            else:
                event.ignore()

#MOSTRAR INTERFAZ DE CADA UNO
    def _mostrarPuntoDeVenta_(self,event):#HACE VISIBLES LOS ELEMENTOS DE PUNTO DE VENTA
        self.interfaz_punto_de_venta.FrameInventario.setVisible(False)
        self.interfaz_punto_de_venta.FrameTickets.setVisible(False)
        self.interfaz_punto_de_venta.FramePuntoDeVenta.setVisible(True)
        self.interfaz_punto_de_venta.menuPunto_de_venta.setEnabled(False)
        self.interfaz_punto_de_venta.menuInventario.setEnabled(True)
        self.interfaz_punto_de_venta.menuTickets.setEnabled(True)
        self.mostrarTotalCosto(self._mostrarPuntoDeVenta_)
        self.mostrarTotalProductos(self._mostrarPuntoDeVenta_)
    def _mostrarInventario_(self,event):#HACE VISIBLES LOS ELEMENTOS DE INVENTARIO
        self.interfaz_punto_de_venta.FramePuntoDeVenta.setVisible(False)
        self.interfaz_punto_de_venta.FrameInventario.setVisible(True)
        self.interfaz_punto_de_venta.FrameTickets.setVisible(False)
        self.interfaz_punto_de_venta.menuInventario.setEnabled(False)
        self.interfaz_punto_de_venta.menuTickets.setEnabled(True)
        self.interfaz_punto_de_venta.menuPunto_de_venta.setEnabled(True)
        self.actualizarBusquedaInventario()
    def _mostrarTickets_(self,event):#HACE VISIBLES LOS ELEMENTOS DE TICKETS
        self.interfaz_punto_de_venta.FrameInventario.setVisible(False)
        self.interfaz_punto_de_venta.FramePuntoDeVenta.setVisible(False)
        self.interfaz_punto_de_venta.FrameTickets.setVisible(True)
        self.interfaz_punto_de_venta.menuTickets.setEnabled(False)
        self.interfaz_punto_de_venta.menuPunto_de_venta.setEnabled(True)
        self.interfaz_punto_de_venta.menuInventario.setEnabled(True)
        self.interfaz_punto_de_venta.BotonCerrarSesion.setEnabled(True)
        self.actualizarBusquedaIickets()
    # PUNTO DE VENTA

    def limpiarLabelBusquedaVenta(self,event):#limpiar texto de busqueda
        self.interfaz_punto_de_venta.LineBuscarProductoPuntoDeVenta.setText("")

    def actualizarTotal(self,event):#actualizar total a pagar
        if self.tengoProductos: #Si se tiene algun producto dentro de la tabla de ventas
            total = 0 #se inicializa el total en 0
            for fila_iterador in range(self.interfaz_punto_de_venta.TablaDeVentas.rowCount()): #iteramos por todas las filas de la tabla
                total = float(self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,2).text().replace("$","")) * float(self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador,3).text())#se hace una multiplicacion de las uniades por el costo del producto
                self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,4).setText("$"+str(total)) # se le asigna al total el valor obtenido 
                self.mostrarTotalCosto(self.actualizarTotal) # se actualiza el total
                self.mostrarTotalProductos(self.actualizarTotal) # se actualiza la la cantidad de productos

    def mostrarTotalCosto(self,event):
        if self.tengoProductos:#Si se tiene algun producto dentro de la tabla de ventas
            total = 0 #se inicializa el total en 0
            for fila_total_iterador in range(self.interfaz_punto_de_venta.TablaDeVentas.rowCount()):#iteramos por todas las filas de la tabla
                total += float(self.interfaz_punto_de_venta.TablaDeVentas.item(fila_total_iterador,4).text().replace("$",""))#se hace una sumatoria de todos los totales de cada producto
            self.interfaz_punto_de_venta.LabelCostoTotal.setText("$"+str(total)) # se muestrea el costo total en el label costo total
    
    def mostrarTotalProductos(self,event):
        if self.tengoProductos:#Si se tiene algun producto dentro de la tabla de ventas
            total = 0 #se inicializa el total en 0
            for fila_total_iterador in range(self.interfaz_punto_de_venta.TablaDeVentas.rowCount()):#iteramos por todas las filas de la tabla
                total += self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_total_iterador,3).value() #hacemos una sumatora de todos las unidades productos
            self.interfaz_punto_de_venta.LabelUnidadProductos.setText(str(int(total))+" Unidades") #se muestra el total de productos en el label unidad productos

    def agregarProducto(self,event):#evento drop hacia venta
        try:    #obtenemos el codigo del producto al que se hace drop event
            productoAgregar = self.interfaz_punto_de_venta.TablaConsultarProducto.item(self.interfaz_punto_de_venta.TablaConsultarProducto.currentRow(),0).text()
            for fila_iterador in range(self.interfaz_punto_de_venta.TablaDeVentas.rowCount()):#iteramos por todas las filas de la tabla
                if productoAgregar == self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,0).text():#si el codigo del producto a agregar es el mismo que el codigo de esa iteracion
                    self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador,3).setValue(self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador,3).value()+1)#se le suma 1 alas unidades producto 
                    if self.tengoProductos: # si se tiene productos
                        self.actualizarTotal(self.mostrarTotalCosto) #se llama a actualizar total
                        self.mostrarTotalCosto(self.mostrarTotalProductos)#se llama a mostrar total productos
                        break
                    self.tengoProductos = True#tengo productos se vuelve true, 
            else:#si ningun codigo fue coinciente en toda la tabla
                producto = base_de_datos.getProducto(productoAgregar)#se obtiene de la base de datos toda la informacion sobre ese producto
                self.total_productos +=1 #se le suma 1 al total de productos
                self.interfaz_punto_de_venta.TablaDeVentas.setRowCount(self.total_productos) #asignamos el total de filas tantos productos sean
                for columna_iterador in range(5): #setTextAlignment( alineación ) en 2 , 3 y 4
                    if columna_iterador == 3: #si la columna es la 3
                        self.interfaz_punto_de_venta.TablaDeVentas.setCellWidget(self.total_productos-1,columna_iterador,QtWidgets.QDoubleSpinBox(self))#se añade un spinbox como un cellwidget
                        self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(self.total_productos-1,columna_iterador).setValue(1)#se le asigna el valor 1 por defecto
                    elif columna_iterador == 4:#si la columna es la 4
                        total = float(self.interfaz_punto_de_venta.TablaDeVentas.item(self.total_productos-1,2).text().replace("$","")) * float(self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(self.total_productos-1,3).value())#se obtiene el total multiplicando las unidades por el costo
                        self.interfaz_punto_de_venta.TablaDeVentas.setItem(self.total_productos-1,columna_iterador,QtWidgets.QTableWidgetItem("$"+str(total))) #se asigna el item de total con el valor obtenido
                    else:#si no fue ni 3 y ni 4
                        if columna_iterador == 2:#si la columna es la 2
                            self.interfaz_punto_de_venta.TablaDeVentas.setItem(self.total_productos-1,columna_iterador,QtWidgets.QTableWidgetItem("$"+producto[0][columna_iterador])) #se añade un signo de precio ya que representa el costo del producto
                        else:
                            self.interfaz_punto_de_venta.TablaDeVentas.setItem(self.total_productos-1,columna_iterador,QtWidgets.QTableWidgetItem(producto[0][columna_iterador]))#se asigna al item de la tabla el valor en esa posicion
                self.tengoProductos = True # tengo productos se vuelve true
                self.actualizarTotal(self.agregarProducto) # se llama al evento actualizar total
                self.mostrarTotalCosto(self.agregarProducto) #se llama al evento total costo
                self.mostrarTotalProductos(self.agregarProducto) #se llama al evento de total de productos
        except Error as msj:#AGREGAR ICONO
            QtWidgets.QMessageBox.information(self,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ")
        #Consultas a base de datos

    def eliminarProducto(self,event):
        if event.key() == 16777223 and self.interfaz_punto_de_venta.TablaDeVentas.currentRow() != -1 :#cuando se presiona la tecla sup y se tiene un elemento de la tabla selecconado
            fila_borrar = self.interfaz_punto_de_venta.TablaDeVentas.currentRow()#obtenemos la fila que bamos a borrar con el metodo current row
            for fila_iterador_restante in range(fila_borrar,self.total_productos):#iteramos por todos los elementos restantes despues del selecionado
                    if fila_iterador_restante == self.total_productos-1:#si la fila iterador es igual ala ultima
                        self.total_productos -= 1 #le restamos 1 a productos
                        if self.total_productos == 0: #si productos es igual a 0
                            self.tengoProductos = False #tengo productos se volvera false
                        self.interfaz_punto_de_venta.TablaDeVentas.setRowCount(self.total_productos)#asignamos el tamaño de filas como tantos productos tengas
                        break
                    else:#si no estas en la ultima fila se va a reemplazar cada valor de cada columna con el superior         
                        for columna_iterador in range(self.interfaz_punto_de_venta.TablaDeVentas.columnCount()):#itero por todas las columnas
                            if columna_iterador == 3:#si la columna es la tercera (unidades)
                                valor = self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador_restante+1,columna_iterador).value()#valor de el arriba
                                self.interfaz_punto_de_venta.TablaDeVentas.setCellWidget(fila_iterador_restante,columna_iterador,QtWidgets.QDoubleSpinBox(self))#iniccializas el elemento el que estas
                                self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador_restante,columna_iterador).setValue(valor)#se asigna el valor del de arriba
                            elif columna_iterador == 4:#si la columna es la 4ta (total)
                                valor = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador_restante+1,columna_iterador).text()#valor de el arriba
                                self.interfaz_punto_de_venta.TablaDeVentas.setItem(fila_iterador_restante,columna_iterador,QtWidgets.QTableWidgetItem(valor))#se asigna el valor del de arriba
                            else:
                                if columna_iterador == 2:#si la columna es la segunta (costo)
                                    valor = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador_restante+1,columna_iterador).text()#valor de el arriba
                                    self.interfaz_punto_de_venta.TablaDeVentas.setItem(fila_iterador_restante,columna_iterador,QtWidgets.QTableWidgetItem(valor))#se asigna el valor del de arriba
                                else:#asigna simplemente el valor que tiene (codigo y nombre)
                                    valor = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador_restante+1,columna_iterador).text()#valor de el arriba
                                    self.interfaz_punto_de_venta.TablaDeVentas.setItem(fila_iterador_restante,columna_iterador,QtWidgets.QTableWidgetItem(valor))#se asigna el valor del de arriba              

            self.actualizarTotal(self.eliminarProducto)#se vuelven a llamar a los eventos de actualizar total y 
            self.mostrarTotalProductos(self.eliminarProducto) #tambien al de mostrar total de productos

    def actualizarBusquedaProducto(self):#actualiza la busqueda de productos
        try:
            productos = base_de_datos.buscarProductoVenta(self.interfaz_punto_de_venta.LineBuscarProductoPuntoDeVenta.text())#obtenemos de la base de datos el producto que se asemeje al line de buscar producto
            self.interfaz_punto_de_venta.TablaConsultarProducto.setRowCount(len(productos))#asignamos el tamaño de filas cuantos productos obtengamos de la base de datos
            for fila_iterador in range(len(productos)):#iteramos por todas las filas de la tabla
                for columna_iterador in range(len(productos[0])):#iteramos por todas las columnas de la tabla
                    if columna_iterador == 2:#si la columna es igual a dos (precio)
                        self.interfaz_punto_de_venta.TablaConsultarProducto.setItem(fila_iterador,columna_iterador,QtWidgets.QTableWidgetItem("$"+productos[fila_iterador][columna_iterador]))#se asigna el valor de la base de datos con un $
                    else:
                        self.interfaz_punto_de_venta.TablaConsultarProducto.setItem(fila_iterador,columna_iterador,QtWidgets.QTableWidgetItem(productos[fila_iterador][columna_iterador]))#se asigna el valor de la base de datos
        
        except Error as msj:#Alguna excepcion leantara un Error de base de datos
            QtWidgets.QMessageBox.information(self,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ")
            
    def realizarPago(self,event): #Realiza el pago
        if self.interfaz_punto_de_venta.TablaDeVentas.rowCount() > 0: #Si se tiene productos en la tabla de vbentas
            self.mostrarTotalCosto(self.realizarPago)
            self.mostrarTotalProductos(self.realizarPago)
            lista_de_producto = []#Guarda todos los productos
            ticket = f"        PUNTO DE VENTA\n        Fecha | {fecha}\n        Atendio | {self.user}\n" #Generador de ticket venta
            ticket += "| Codigo | Nombre | C/U | Total |\n" #Concatena el texto
            ticket += "---------------------------------\n" #Concatena el texto
            productos = str() 
            try:
                total_productos = self.interfaz_punto_de_venta.TablaDeVentas.rowCount() #Asigna el numero de filas
                for fila_iterador in range(total_productos): #Itera por por filas
                    codigo = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,0).text() #Asigna el texto de la primera columna de la fila iterada
                    nombre = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,1).text() #Asigna el texto de la segunda columna de la fila iterada
                    unidades = int(self.interfaz_punto_de_venta.TablaDeVentas.cellWidget(fila_iterador,3).value()) #Asigna el valor de la cuarta columna de la fila iterada
                    unidadesTotales = int(base_de_datos.validarCantidad(codigo)) #Guarda las cantidades
                    assert unidadesTotales >= unidades , "No existe esa cantidad de productos" #Compara que existan las unidades en inventario para venderlas
                    unidadesTotales = int(unidadesTotales) - int(unidades) #Resta las unidades existentes a las vendidas
                    assert base_de_datos.actualizarCantidadProducto(codigo,unidadesTotales),"Error al actualizar la Cantidad de productos" #ACtualiza  en la base de datos el valor de las unidades restantes existen
                    total_producto = self.interfaz_punto_de_venta.TablaDeVentas.item(fila_iterador,4).text() #Asigna el texto de la quinta columna de la fila iterada
                    ticket += f"{codigo} | {nombre} | {unidades}| {total_producto} |\n" #Contatena los datos de los productos vendidos
                    lista_de_producto.append((codigo,nombre,unidades,total_producto)) #Agrega a la lista los datos de los productos vendidos
                    productos += f"| {nombre} |" #Concatena el nombre del producto
                cantida_productos = self.interfaz_punto_de_venta.LabelUnidadProductos.text().replace("Unidades","") #Remplaza el texto especificado
                totalVenta = self.interfaz_punto_de_venta.LabelCostoTotal.text().replace("$","") #Remplaza el texto especificado
                folio = int(base_de_datos.getUltimoFolio()) #Se genera el folio con el ultimo en la base de datos
                if folio == 0: #Si no hay ninguno se genera el primero
                    folio = 10000001
                else: #Si no se agrega a un nuevo folio
                    folio+=1
                assert base_de_datos.generarTicket(folio,productos,cantida_productos,totalVenta),"No se pudo registar el Ticket" #Registra el ticket en la base de datods
                ticket += f"Total de productos: {cantida_productos}| ${totalVenta}\n " #Concatena el texto con los datos
                ticket += f"Folio | {folio}" #Concatena el texto con los datos
                doc = open(f"Tickets/{folio}","w") #Genera un archivo de texto que permite escribir en el
                doc.write(ticket) #Escribir las informacion del ticket en el archivo de texto
                doc.close() #Cierra el archivo
                opcion = QtWidgets.QMessageBox.question(self, " ", "¿Esta seguro que desea generar la venta?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) #Para confirmar si desea realizar la venta
                if opcion == QtWidgets.QMessageBox.Yes:
                    QtWidgets.QMessageBox.information(self,"VENTA EXITOSA","Venta generada de forma exitosa")
                    self.inicializar_interfaz_punto_de_venta() #Inicializa nuevamente la interfaz
                    self.interfaz_punto_de_venta.TablaDeVentas.setRowCount(0)#Esto es para que al entrar en el punto de venta se borre los datos anteriores
                    self.interfaz_punto_de_venta.TablaConsultarProducto.setRowCount(0)#Elimina todas las filas
                    self.interfaz_punto_de_venta.TablaDeVentas.removeRow(0)#Esto es para que al entrar en el punto de venta se borre los datos anteriores
                    self.interfaz_punto_de_venta.TablaConsultarProducto.removeRow(0)#Elimina todas las filas
                    self.mostrarTotalCosto(self.realizarPago) #Muestra el total de costos
                    self.mostrarTotalProductos(self.realizarPago) #Muestra el total de producto
            except AssertionError as msj: #En caso de haber un error, mostrara el mensaje
                QtWidgets.QMessageBox.information(self,"ERROR",f"{msj}")
   
    def  _agregar_producto_(self,event): #Despliega la ventana de registro de producto
        ventana_registro_producto.show()
        
    # PUNTO DE VENTA

    # INVENTARIO  
    def limpiarLabelBusquedaInventario(self,event):#limpiar line de buscar
        self.interfaz_punto_de_venta.LineBuscarProductoInventario.setText("")

    #Consultas a base de datos

    def actualizarBusquedaInventario(self):#actualizar busqueda de inventario
        try:
            productos = base_de_datos.buscarProductoInventario(self.interfaz_punto_de_venta.LineBuscarProductoInventario.text()) #Busca dentro de la base de datos con lo que ingreso en usuario
            self.interfaz_punto_de_venta.TablaDeInventario.setRowCount(len(productos))
            for fila_iterador in range(len(productos)): #Itera por las filas de la tabla
                for columna_iterador in range(len(productos[0])): #Itera por las columnas de la tabla
                    if columna_iterador ==3: #Concatena el simbolo de $ para la columna de precios de cada fila
                        self.interfaz_punto_de_venta.TablaDeInventario.setItem(fila_iterador,columna_iterador,QtWidgets.QTableWidgetItem("$"+productos[fila_iterador][columna_iterador]))
                    elif columna_iterador == 0: #Actualiza el item en la casilla seleccionada
                        self.interfaz_punto_de_venta.TablaDeInventario.setItem(fila_iterador,columna_iterador,QtWidgets.QTableWidgetItem(productos[fila_iterador][columna_iterador]))
                        self.interfaz_punto_de_venta.TablaDeInventario.item(fila_iterador,columna_iterador).setFlags(PyQt5.QtCore.Qt.ItemIsEditable)
                    else: #Actualiza el item en la casilla seleccionada
                        self.interfaz_punto_de_venta.TablaDeInventario.setItem(fila_iterador,columna_iterador,QtWidgets.QTableWidgetItem(productos[fila_iterador][columna_iterador]))
        except Error as msj:#AGREGAR ICONO
            QtWidgets.QMessageBox.information(self,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ")

    def modificarInventario(self,event): #El inventario cambia por una modificación del usuario
        try:                
            if event.key() == 16777220 and self.interfaz_punto_de_venta.TablaDeInventario.currentRow() != -1 and self.interfaz_punto_de_venta.TablaDeInventario.currentColumn() != -1: #Evento de la tecla Enter en la couman seleccionada
                fila = self.interfaz_punto_de_venta.TablaDeInventario.currentRow() #Fila actual
                columna = self.interfaz_punto_de_venta.TablaDeInventario.currentColumn() #columna actual
                producto_modificar= self.interfaz_punto_de_venta.TablaDeInventario.cellWidget(fila,columna).text()#Modifica el texo actual escrito
                default = self.interfaz_punto_de_venta.TablaDeInventario.item(fila,columna).text() #Deja por defecto el texto
                codigo = self.interfaz_punto_de_venta.TablaDeInventario.item(fila,0).text() #codigo del producto de la fila seleccionada
                if columna ==4: #Modifica la cantidad del producto
                    tipo = "Cantidad"
                    for i in producto_modificar: #Itera por el dato que ingreso el usuario
                        assert i not in caracteres_especiales[::] ,"El producto contiene valores/caracteres invalidos"
                        assert i not in letras[::],"La cantidad no puede contener letras"
                    assert len(producto_modificar) <= 4,"Tamaño de cantidad exedido"
                    assert len(producto_modificar) > 0, f"valor de {tipo} invalio "
                    assert base_de_datos.actualizarProductoInventario(producto_modificar,tipo,codigo), f"Error al actualizar {tipo}"
                elif columna ==3 : #Modifica el precio del producto
                    tipo = "Precio"
                    
                    for i in producto_modificar: #Itera por el dato que ingreso el usuario
                        if i != ".":
                            assert i not in caracteres_especiales[::] ,"El producto contiene valores/caracteres invalidos"
                        assert i not in letras[::],"El precio no puede contener letras"
                    assert len(producto_modificar) <= 30,"Rango de precio exedido"
                    assert len(producto_modificar) > 0, f"valor de {tipo} invalio "
                    assert base_de_datos.actualizarProductoInventario(producto_modificar,tipo,codigo), f"Error al actualizar {tipo}"
                elif columna == 2 : #Modifica la categoria del producto
                    tipo = "Categoria"
                    for i in producto_modificar: #Itera por el dato que ingreso el usuario
                        assert i not in caracteres_especiales[::] ,"El producto contiene valores/caracteres invalidos"
                    assert len(producto_modificar) <= 30,"El nombre de la categoria es demaciado grande"
                    assert len(producto_modificar) > 0, f"valor de {tipo} invalio "
                    assert base_de_datos.actualizarProductoInventario(producto_modificar,tipo,codigo), f"Error al actualizar {tipo}"
                elif columna == 1 : #Modifica el nombre del producto
                    tipo = "Nombre"
                    for i in producto_modificar: #Itera por el dato que ingreso el usuario
                        assert i not in caracteres_especiales[::] ,"El producto contiene valores/caracteres invalidos"
                    assert len(producto_modificar) < 100,"El tamaño de nombre es demaciado grande"
                    assert len(producto_modificar) > 0, f"valor de {tipo} invalio "
                    assert base_de_datos.validarNombre(producto_modificar) ,"Este nombre ya esta ocupado por otro producto."
                    assert base_de_datos.actualizarProductoInventario(producto_modificar,tipo,codigo), f"Error al actualizar {tipo}"

                self.interfaz_punto_de_venta.TablaDeInventario.setItem(fila,columna,QtWidgets.QTableWidgetItem(producto_modificar))
                self.actualizarBusquedaInventario()
            elif event.key() == 16777223 and self.interfaz_punto_de_venta.TablaDeInventario.currentRow() != -1:#suprimir
                try:
                    fila_borrar = self.interfaz_punto_de_venta.TablaDeInventario.currentRow()#fila actual
                    producto_borrar = self.interfaz_punto_de_venta.TablaDeInventario.item(fila_borrar,0).text()#codigo del producto
                    assert base_de_datos.eliminarProductoInventario(producto_borrar),"No se pudo eliminar el producto"#eliminar de la base de datos
                    self.actualizarBusquedaInventario()
                except AssertionError as msj:
                    QtWidgets.QMessageBox.information(self,"ERROR",f"{msj}")
        except AssertionError as msj:
            QtWidgets.QMessageBox.information(self,"ERROR",f"{msj}")
            self.interfaz_punto_de_venta.TablaDeInventario.item(fila,columna).setText(default)
        except Error as msj:#AGREGAR ICONO
            QtWidgets.QMessageBox.information(app,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ")
      
    # INVENTARIO 
    # TICKTES
    def actualizarBusquedaIickets(self): #Actuliza la busqueda en la tabla de tickets
        tickets = base_de_datos.buscarTicket(self.interfaz_punto_de_venta.LineBuscarTickets.text()) #Busca dentro de la base de datos con lo que ingreso en usuario
        self.interfaz_punto_de_venta.TablaDeTickets.setRowCount(len(tickets))
        for fila_iterador in range(len(tickets)): #Itera dentro de las filas de la tabla
            for columna_iterador in range(len(tickets[0])+1): #Itera dentro de las columnas de la tabla
                if columna_iterador == 3: #Concatena el simbolo de $ para la columna de precios de cada fila
                    txt = "$"+ str(tickets[fila_iterador][columna_iterador])
                    self.interfaz_punto_de_venta.TablaDeTickets.setItem(fila_iterador, columna_iterador, QtWidgets.QTableWidgetItem(txt))
                    #self.interfaz_punto_de_venta.TablaDeTickets.item(fila_iterador,columna_iterador).setText(txt)
                if columna_iterador == 4: #Agrega el boton de Mostrar Ticket en la cuarta columna de todas las filas de la tabla
                    self.interfaz_punto_de_venta.TablaDeTickets.setCellWidget(fila_iterador, columna_iterador, QtWidgets.QPushButton("Mostrar ticket"))
                    #self.interfaz_punto_de_venta.TablaDeTickets.CellWidget(fila_iterador, columna_iterador)
                else:
                    self.interfaz_punto_de_venta.TablaDeTickets.setItem(fila_iterador, columna_iterador, QtWidgets.QTableWidgetItem(tickets[fila_iterador][columna_iterador]))
    
    def limpiarLabelBusquedaTickets(self, event): #Limpia todos los datos anteriores que el usuario haya ingresado
        self.interfaz_punto_de_venta.LineBuscarTickets.setText("")

    def mostrarTicket(self,event): #Muestra el ticket escogido
        try:
            if self.interfaz_punto_de_venta.TablaDeTickets.currentRow() > -1:#verifica que hay tickets en la base de datos
                folio = self.interfaz_punto_de_venta.TablaDeTickets.item(self.interfaz_punto_de_venta.TablaDeTickets.currentRow(),0).text()#se toma el folio del ticket
                with open(f"Tickets/{folio}") as doc:#se abre el archivo que guarda como nombre el folio de ese ticket para obtener toda su información
                    QtWidgets.QMessageBox.information(self,"TICKET",f"{doc.read()}")#se muestra el ticket
        except FileNotFoundError:#alguna excepcion a la hora de abrir el ticket mostrara una alerta
            QtWidgets.QMessageBox.information(self,"ERROR","Archivo de ticket eliminado/modificado")
                
@singleton
class VentanaAgregarProducto(QtWidgets.QMainWindow):
    def __init__(self): #Constructor de la clase
        super().__init__() #
        self.interfaz_agregar_producto = Ui_VentanaAgregarProducto() #
        self.interfaz_agregar_producto.setupUi(self) #
        self.setStyleSheet(registro_producto) #Se determina el estilo de la ventana
        self.setWindowTitle("Agregar Producto") #Se agrega titulo a la ventana
        self.inicializar_interfaz_agregar_producto() #Se inicializa la interfaz
        self.interfaz_agregar_producto.BotonAgregarAgregarProducto.setEnabled(False) #Deshabilitamos el boton

    def inicializar_interfaz_agregar_producto(self): #Inicializa la interfaz de la ventana agregar producto
        self.agregado = False
        self.interfaz_agregar_producto.Codigo.setText("Ingrese el código del producto") #La casilla muestra el texto
        self.interfaz_agregar_producto.Nombre.setText("Ingrese el nombre del producto") #La casilla muestra el texto
        self.interfaz_agregar_producto.Categoria.setText("Ingrese la categóría del prodcuto") #La casilla muestra el texto
        self.interfaz_agregar_producto.Precio.setText("Ingrese el precio del producto") #La casilla muestra el texto
        self.interfaz_agregar_producto.Unidades.setText("Ingrese las unidades del producto") #La casilla muestra el texto
        self.interfaz_agregar_producto.Codigo.mouseDoubleClickEvent = self.limpiarLabelCodigoAgregarProducto #Al evento del doble click en la casilla, limpia el texto en ella
        self.interfaz_agregar_producto.Nombre.mouseDoubleClickEvent = self.limpiarLabelNombreAgregarProducto #Al evento del doble click en la casilla, limpia el texto en ella
        self.interfaz_agregar_producto.Categoria.mouseDoubleClickEvent = self.limpiarLabelCategoriaAgregarProducto #Al evento del doble click en la casilla, limpia el texto en ella
        self.interfaz_agregar_producto.Precio.mouseDoubleClickEvent = self.limpiarLabelPrecioAgregarProducto #Al evento del doble click en la casilla, limpia el texto en ella
        self.interfaz_agregar_producto.Unidades.mouseDoubleClickEvent = self.limpiarLabelUnidadesAgregarProducto #Al evento del doble click en la casilla, limpia el texto en ella
        self.interfaz_agregar_producto.Codigo.textChanged.connect(self.estadoBotonAgregarAgregarProducto) #Al cambiar el texto de la casilla, comprueba el estado del boton
        self.interfaz_agregar_producto.Nombre.textChanged.connect(self.estadoBotonAgregarAgregarProducto) #Al cambiar el texto de la casilla, comprueba el estado del boton
        self.interfaz_agregar_producto.Categoria.textChanged.connect(self.estadoBotonAgregarAgregarProducto) #Al cambiar el texto de la casilla, comprueba el estado del boton
        self.interfaz_agregar_producto.Precio.textChanged.connect(self.estadoBotonAgregarAgregarProducto) #Al cambiar el texto de la casilla, comprueba el estado del boton
        self.interfaz_agregar_producto.Unidades.textChanged.connect(self.estadoBotonAgregarAgregarProducto) #Al cambiar el texto de la casilla, comprueba el estado del boton
        self.interfaz_agregar_producto.BotonAgregarAgregarProducto.mousePressEvent = self.agregar_producto #Al cambiar el texto de la casilla, comprueba el estado del boton

    def agregar_producto(self,event): #Agrega el producto ingresado por el usuario a la tabla de productos
        try:
            for i in self.interfaz_agregar_producto.Codigo.text(): #Comprueba que los datos ingresados por el usuario no contega caracteres especiales o caracteres alfabeticos
                assert i not in caracteres_especiales[::], "El código del producto no debe contener caracteres especiales"
                assert i not in letras[::] , "El código del producto no debe contener letras"
            assert len(self.interfaz_agregar_producto.Codigo.text()) == 8, "El código del producto debe ser de 8 carecteres numericos"
            assert base_de_datos.validarCodigo(self.interfaz_agregar_producto.Codigo.text()) , "Ya existe un producto con ese código"
            for i in self.interfaz_agregar_producto.Nombre.text(): #Comprueba que los datos ingresados por el usuario no contega caracteres especiales
                assert i not in caracteres_especiales[::], "El nombre del producto no debe contener caracteres especiales"
            assert len(self.interfaz_agregar_producto.Nombre.text()) <= 100, "El tamaño del nombre es demasiado grande"
            assert base_de_datos.validarNombre(self.interfaz_agregar_producto.Nombre.text()) , "Ya existe un producto con ese nombre"
            for i in self.interfaz_agregar_producto.Categoria.text(): #Comprueba que los datos ingresados por el usuario no contega caracteres especiales
                assert i not in caracteres_especiales[::], "La categoria del producto no debe contener caracteres especiales"
            assert len(self.interfaz_agregar_producto.Categoria.text()) <= 50, "El tamaño del categoría es demasiado larga"
            for i in self.interfaz_agregar_producto.Precio.text(): #Comprueba que los datos ingresados por el usuario no contega caracteres especiales o caracteres alfabeticos
                if i != ".":
                    assert i not in caracteres_especiales[::], "El precio del producto no debe contener caracteres especiales"
                assert i not in letras[::] , "El precio del producto no debe contener letras"
            assert len(self.interfaz_agregar_producto.Precio.text()) <= 30, "El tamaño del precio es demasiado grande"
            for i in self.interfaz_agregar_producto.Unidades.text(): #Comprueba que los datos ingresados por el usuario no contega caracteres especiales o caracteres alfabeticos
                assert i not in caracteres_especiales[::], "Las unidades del producto no debe contener caracteres especiales"
                assert i not in letras[::] , "Las unidades del producto no debe contener letras"
            assert len(self.interfaz_agregar_producto.Unidades.text()) <= 6, "El tamaño de unidades es demasiado grande"
            assert base_de_datos.registrarProducto(str(self.interfaz_agregar_producto.Codigo.text()), str(self.interfaz_agregar_producto.Nombre.text()), str(self.interfaz_agregar_producto.Categoria.text()), str(self.interfaz_agregar_producto.Precio.text()), str(self.interfaz_agregar_producto.Unidades.text())), "No se pudo registrar el producto"
            QtWidgets.QMessageBox.information(self, " ", "Registro de producto exitoso")#si se pudo completar el registro retorna una ventana de confirmacion
            ventana_punto_de_venta.actualizarBusquedaInventario()# se llama ala funcion de actualizar inventario
            self.agregado = True #Hacemos que la variable agregado se vuelva verdadera
        except AssertionError as msj:
            QtWidgets.QMessageBox.information(self,"Error de Registro",f"{msj}")

    def limpiarLabelCodigoAgregarProducto(self, event):#Limpia todos los datos anteriores que el usuario haya ingresado
        self.interfaz_agregar_producto.Codigo.setText("")

    def limpiarLabelNombreAgregarProducto(self, event):#Limpiatodos los datos anteriores que el usuario haya ingresado
        self.interfaz_agregar_producto.Nombre.setText("")

    def limpiarLabelCategoriaAgregarProducto(self, event):#Limpia todos los datos anteriores que el usuario haya ingresado
        self.interfaz_agregar_producto.Categoria.setText("")

    def limpiarLabelPrecioAgregarProducto(self, event):#Limpia todos los datos anteriores que el usuario haya ingresado
        self.interfaz_agregar_producto.Precio.setText("")

    def limpiarLabelUnidadesAgregarProducto(self, event): #Limpiatodos los datos anteriores que el usuario haya ingresado
        self.interfaz_agregar_producto.Unidades.setText("")

    def estadoBotonAgregarAgregarProducto(self): #Comprueba el estado del boton de agregar, y lo habilita si el usuario ingresa todos los datos correctamente
        if len(self.interfaz_agregar_producto.Codigo.text()) != 0 and len(self.interfaz_agregar_producto.Nombre.text()) != 0 and len(self.interfaz_agregar_producto.Categoria.text()) != 0 and len(self.interfaz_agregar_producto.Precio.text()) != 0 and len(self.interfaz_agregar_producto.Unidades.text()) != 0:
            self.interfaz_agregar_producto.BotonAgregarAgregarProducto.setEnabled(True)
        else:
            self.interfaz_agregar_producto.BotonAgregarAgregarProducto.setEnabled(False)
    
    def closeEvent(self, event): #Al ejecutarse el evento de cerrar, despliega un mensaje para confirmar el cierre
        if not self.agregado:
            opcion = QtWidgets.QMessageBox.question(self, " ", "¿Estás seguro que quieres cancelar el registro de productos?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if opcion == QtWidgets.QMessageBox.Yes:#AGREGAR ICONO
                ventana_registro_producto.close()
            else:
                event.ignore()
    

def suppress_qt_warnings():#Esto es para que no muestre warnings ala hora de iniciar el codigo; Es la unica solucion que encontre
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == '__main__':
    try:
        hoy = datetime.now()#Obtenemos la fecha actual
        fecha = f"{hoy.day}/{hoy.month}/{hoy.year}"#obtenemos el formato de la fecha
        base_de_datos = BaseDeDatos() #Se crea la instancia del objeto de la clase BaseDeDatos
        suppress_qt_warnings() #Se llama a la función para evitar que muestre warnings en el código
        app = QtWidgets.QApplication([]) #Se crea la iaplicación de escritorio
        ventana_login = VentanaLogin() #Se crea la instancia del objeto de la clase VentanaLogin
        ventana_registro_usuario = VentanaRegistroUsuario() #Se crea la instancia del objeto de la clase VentanaRegistroUsuario
        ventana_punto_de_venta = VentanaPuntoDeVenta() #Se crea la instancia del objeto de la clase VentanaPuntoDeVenta
        ventana_registro_producto = VentanaAgregarProducto() #Se crea la instancia del objeto de la clase VentanaAgregarProducto
        ventana_login.show() #Despliega la ventana de login
        sys.exit(app.exec()) #Cierra el sistema de la aplicación
    except Error as msj:#AGREGAR ICONO
        QtWidgets.QMessageBox.information(app,"ERROR",f"Ah ocurrio un error con la base de datos: {msj} ") #Muestra un mensaje de error en caso de  error con la base de datos
    finally:
        base_de_datos.conexion.close() #Se cierra la conexión con la base de datos

        #cambiar padres
        #todos los frames .setGeometry(QtCore.QRect(20, 60, 1131, 511))
        #setFixedSize(width, height)