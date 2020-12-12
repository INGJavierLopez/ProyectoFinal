import sqlite3
from sqlite3 import Error


class BaseDeDatos():

    def __init__(self):
            self.conexion = sqlite3.connect("PuntoDeVenta.db")#se crea/abre la base de datos y se inicializa la conexion
            self.cursor = self.conexion.cursor()#se crea un cursor
            self.cursor.execute(#se crea la talba de usuarios en caso de no existir
                "CREATE TABLE IF NOT EXISTS Usuarios(Usuario varchar(30),password varchar(30));")
            self.cursor.execute(#se crea la talba de productos en caso de no existir
                "CREATE TABLE IF NOT EXISTS Productos(Codigo varchar(8),Nombre varchar(100),Categoria varchar(50),Precio varchar(30),Cantidad varchar(6));"
            )
            self.cursor.execute(#se crea la talba de tickets en caso de no existir
                "CREATE TABLE IF NOT EXISTS Tickets(Folio varchar(8),Productos text,CantidadProductos varchar(6),Total varchar(30));"
            )
            self.conexion.commit()
    #login
    def loginUser(self, user, password):#funcion para loguearte
        try:
            self.cursor.execute(#se selecciona todo cuando el usuario y contraseña coincidan
                f"select * from Usuarios where Usuario = '{user}' and password  = '{password}';  ")
            if not self.cursor.fetchone() is None:#si selecciona un elemento retorna true
                return True
            else:
                return False #si no selecciono nada retorna
        except Error:
            return False

    def registrarUser(self, user, password):#funcion registrar usuario
        try:
            self.cursor.execute(#comprueba que no existe ningun usuario con ese nombre de usuario
                f"SELECT Usuario FROM Usuarios WHERE Usuario = '{user}';")
            if self.cursor.fetchone() is None:#si no existe ningun usuario procede a agregarlo a la base de datos
                self.cursor.execute(
                    f"INSERT INTO Usuarios VALUES('{user}','{password}');")
                self.conexion.commit()#se guardan los cambios en la base de datos
                return True#retorna true si se completo el registro
            else:
                return False
        except Error:
            return False
    def comoprobarUser(self,user):#se comprueba que no existe un usuario para poder iniciar sesion
        try:
            self.cursor.execute(#se comprueba si que hay un usuario registrado con ese user
                f"SELECT Usuario FROM Usuarios WHERE Usuario = '{user}';")
            if self.cursor.fetchone() is None:
                return True #si no existe ningun usuario con ese nombre retorna true
            else:
                return False #si exite un usuario retorna false
        except Error:
            return False
    #login
    #venta
    def buscarProductoVenta(self,producto):#selecciona los productos que se buscan
        try:
            self.cursor.execute(#busca si hay alguna coincidencia en el codigo,nombre o categoria
                f"SELECT Codigo,Nombre,Precio,Cantidad FROM Productos WHERE Codigo LIKE '{producto+'%'}' OR Nombre LIKE '{producto+'%'}' OR Categoria LIKE '{producto+'%'}' ORDER BY Nombre;")
            return self.cursor.fetchall()#retorna todas las coincidencias
        except Error:
            return False

    def cargarProductos(self): #obtenemos todos los productos de la base de datos
        try:
            self.cursor.execute(
                f"SELECT * FROM Productos;") #selecciona todo sobre los productos registrados
            return self.cursor.fetchall() #retorna todos los productos
        except Error:
            return False
            
    def getProducto(self,producto): #obtenemos los datos del producto con el codigo ingresado
        try:
            self.cursor.execute(#ejecutamos la busqueda del producto
                f"SELECT Codigo,Nombre,Precio FROM Productos WHERE Codigo LIKE '{producto+'%'}';")
            return self.cursor.fetchall()#retornamos el producto encontrado
        except Error:
            return False 
    
    def validarCantidad(self,codigo):#validamos que la cantidad solicitada este en la base de datos
        try:
            self.cursor.execute( #seleccionamos la cantidad del producto que tiene el codigo ingresado
                f"SELECT Cantidad FROM Productos WHERE Codigo LIKE '{codigo}';")
            return self.cursor.fetchone()[0] #retorna la cantidad de dicho producto
        except Error:
            return False 

    def actualizarCantidadProducto(self,codigo,cantidad):#actualizamos la cantidad de un producto despues de realizar la venta
        try:
            self.cursor.execute( #actualizmos la columna de productos del producto con el codigo ingresado y le asignamos la cantidad nueva
                f"UPDATE Productos SET Cantidad ='{cantidad}' WHERE Codigo = '{codigo}';")
            self.conexion.commit() #se guardan los cambios en la base de datos
            return True #retorna verdadero si no hay ninguna excepccion
        except Error:
            return False

    #venta
    #inventario
    def buscarProductoInventario(self,producto):#Obtenemos los productos que se buscan en el line de buscar producto
        try:
            self.cursor.execute(#realiza una consulta a la base de datos llevando como parametro el texto del line
                f"SELECT * FROM Productos WHERE Codigo LIKE '{producto+'%'}' OR Nombre LIKE '{producto+'%'}' OR Categoria LIKE '{producto+'%'}' ORDER BY Nombre;")
            return self.cursor.fetchall() #retorna todas las coincidencias del cursor
        except Error:
            return False

    def eliminarProductoInventario(self,producto):#Eliminamos el producto seleccionado de la base de datos
        try:
            self.cursor.execute(#Se elimina el producto con el codigo proporcionado
                f"DELETE FROM Productos WHERE Codigo = '{producto}';")
            self.conexion.commit()#se guardan los cambios
            self.cursor.execute(#para comprobar que se elimino se hace una consulta para comprobar que ya no existe el producto
                f"SELECT Codigo FROM Productos WHERE Codigo = '{producto}';")
            if self.cursor.fetchone() is None: #si el cursor devuelve none quiere decir que se elimino de forma correcta
                return True
            else:
                return False
        except Error:
            return False

    def actualizarProductoInventario(self,valor,producto,codigo):#actualizamos algun atributo del producto excepto el codigo
        try:
            self.cursor.execute(#tomamos como parametro el nuevo valor como valor, producto como el atributo y codigo para saber que producto se va a modificar
                f"UPDATE Productos SET {producto}='{valor}' WHERE Codigo = '{codigo}';")
            self.conexion.commit()#guardamos los cambios en la base de datos
            return True
        except Error:
            return False
        
    def validarNombre(self,nombre):#Si se desea cambiar el nombre de un producto se debe validar que no exista en la base de datos
        try:
            self.cursor.execute(#se busca en la base de datos el nombre ingreasado
                f"SELECT Nombre FROM Productos WHERE Nombre = '{nombre}';")
            if self.cursor.fetchone() is None:#si el cursor retorna none quiere decir que no hay ningun producto registrado con ese nombre
                return True #retornamos true para validar la modificacion
            else:
                return False #retornamos false para cancelar la validacion
        except Error:
            return False
    
    def validarCodigo(self,codigo):#validar que el codigo ingresado para el nuevo producto no esta en la base de datos
        try:
            self.cursor.execute( #se busca en la base de datos alguna coincidenca con el codigo ingresado
                f"SELECT Codigo FROM Productos WHERE Codigo = '{codigo}';")
            if self.cursor.fetchone() is None:#si no hay coincidencias retorna verdadero
                return True
            else:
                return False
        except Error:
            return False
    
    def registrarProducto(self, codigo, nombre, categoria, precio, unidades):#funcion para registrar producto
        try:
            self.cursor.execute(
                f"INSERT INTO Productos VALUES('{codigo}', '{nombre}', '{categoria}', '{precio}', '{unidades}')")
            self.conexion.commit()
            return True
        except Error:
            return False

    #inventario
    #tickets
    def buscarTicket(self, ticket):#Retorna todas las coincidencias del texto ingresado en el line
        try:
            self.cursor.execute(#el texto contiene el numero de folio y lo que hace la funcion es devolver todos los que tienen esa coincidencia
                f"SELECT * FROM Tickets WHERE Folio LIKE '{'%'+ticket+'%'}' ORDER BY Folio;")
            return self.cursor.fetchall()
        except Error:
            return False

    def getUltimoFolio(self):#obtenemos el ultimo folio registrado
        try:
            self.cursor.execute(#seleccionamos todos los tickets ordenandolos de mayor a menor
                f"SELECT Folio FROM Tickets ORDER BY Folio DESC;")
            folio = self.cursor.fetchone()#asignamos el folio a una variable
            if folio is None: #si el folio es none entonces no tenemos ningun folio por lo cual retornamos 0
                return 0
            else:
                return folio[0] #si no, retornamos el ultimo folio
        except Error:
            return False

    def generarTicket(self,folio,productos,cantida_productos,totalVenta):#se genera el ticket de compra
        try:
            self.cursor.execute(
                f"INSERT INTO Tickets VALUES('{folio}','{productos}','{cantida_productos}','{totalVenta}');")
            self.conexion.commit()
            return True
        except Error:
            return False



    #tickets
# https://www.digitalocean.com/community/tutorials/crear-un-nuevo-Usuario-y-otorgarle-permisos-en-mysql-es
# https://www.digitalocean.com/community/tutorials/how-to-create-and-manage-databases-in-mysql-and-mariadb-on-a-cloud-server
# https://pynative.com/python-mysql-database-connection/
