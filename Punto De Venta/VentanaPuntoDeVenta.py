# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPuntoDeVenta.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPuntoDeVenta(object):
    def setupUi(self, VentanaPuntoDeVenta):
        VentanaPuntoDeVenta.setObjectName("VentanaPuntoDeVenta")
        VentanaPuntoDeVenta.setFixedSize(1171, 602)
        self.centralwidget = QtWidgets.QWidget(VentanaPuntoDeVenta)
        self.centralwidget.setObjectName("centralwidget")
        self.FrameInventario = QtWidgets.QFrame(self.centralwidget)
        self.FrameInventario.setGeometry(QtCore.QRect(20, 60, 1131, 511))
        self.FrameInventario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameInventario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameInventario.setObjectName("FrameInventario")
        self.BotonAgregarProducto = QtWidgets.QPushButton(self.FrameInventario)
        self.BotonAgregarProducto.setGeometry(QtCore.QRect(890, 10, 151, 31))
        self.BotonAgregarProducto.setObjectName("BotonAgregarProducto")
        self.LabelBuscarProductoInventario = QtWidgets.QLabel(self.FrameInventario)
        self.LabelBuscarProductoInventario.setGeometry(QtCore.QRect(25, 10, 111, 21))
        self.LabelBuscarProductoInventario.setObjectName("LabelBuscarProductoInventario")
        self.TablaDeInventario = QtWidgets.QTableWidget(self.FrameInventario)
        self.TablaDeInventario.setGeometry(QtCore.QRect(10, 50, 1111, 451))
        self.TablaDeInventario.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.TablaDeInventario.setAlternatingRowColors(True)
        self.TablaDeInventario.setObjectName("TablaDeInventario")
        self.TablaDeInventario.setColumnCount(5)
        self.TablaDeInventario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeInventario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeInventario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeInventario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeInventario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeInventario.setHorizontalHeaderItem(4, item)
        self.LineBuscarProductoInventario = QtWidgets.QLineEdit(self.FrameInventario)
        self.LineBuscarProductoInventario.setGeometry(QtCore.QRect(139, 10, 231, 21))
        self.LineBuscarProductoInventario.setObjectName("LineBuscarProductoInventario")
        self.FrameTickets = QtWidgets.QFrame(self.centralwidget)
        self.FrameTickets.setGeometry(QtCore.QRect(20, 60, 1131, 511))
        self.FrameTickets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameTickets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameTickets.setObjectName("FrameTickets")
        self.TablaDeTickets = QtWidgets.QTableWidget(self.FrameTickets)
        self.TablaDeTickets.setGeometry(QtCore.QRect(10, 50, 1111, 451))
        self.TablaDeTickets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TablaDeTickets.setAlternatingRowColors(True)
        self.TablaDeTickets.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TablaDeTickets.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TablaDeTickets.setObjectName("TablaDeTickets")
        self.TablaDeTickets.setColumnCount(5)
        self.TablaDeTickets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeTickets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeTickets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeTickets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeTickets.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeTickets.setHorizontalHeaderItem(4, item)
        self.LineBuscarTickets = QtWidgets.QLineEdit(self.FrameTickets)
        self.LineBuscarTickets.setGeometry(QtCore.QRect(139, 10, 231, 21))
        self.LineBuscarTickets.setText("")
        self.LineBuscarTickets.setObjectName("LineBuscarTickets")
        self.LabelBuscarProductoTickets = QtWidgets.QLabel(self.FrameTickets)
        self.LabelBuscarProductoTickets.setGeometry(QtCore.QRect(25, 10, 111, 21))
        self.LabelBuscarProductoTickets.setObjectName("LabelBuscarProductoTickets")
        self.FramePuntoDeVenta = QtWidgets.QFrame(self.centralwidget)
        self.FramePuntoDeVenta.setGeometry(QtCore.QRect(20, 60, 1131, 511))
        self.FramePuntoDeVenta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramePuntoDeVenta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramePuntoDeVenta.setObjectName("FramePuntoDeVenta")
        self.BotonRealizarPago = QtWidgets.QPushButton(self.FramePuntoDeVenta)
        self.BotonRealizarPago.setGeometry(QtCore.QRect(730, 420, 351, 41))
        self.BotonRealizarPago.setObjectName("BotonRealizarPago")
        self.TablaConsultarProducto = QtWidgets.QTableWidget(self.FramePuntoDeVenta)
        self.TablaConsultarProducto.setGeometry(QtCore.QRect(690, 50, 431, 251))
        self.TablaConsultarProducto.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TablaConsultarProducto.setAlternatingRowColors(True)
        self.TablaConsultarProducto.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TablaConsultarProducto.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TablaConsultarProducto.setObjectName("TablaConsultarProducto")
        self.TablaConsultarProducto.setColumnCount(4)
        self.TablaConsultarProducto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConsultarProducto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConsultarProducto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConsultarProducto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConsultarProducto.setHorizontalHeaderItem(3, item)
        self.LineBuscarProductoPuntoDeVenta = QtWidgets.QLineEdit(self.FramePuntoDeVenta)
        self.LineBuscarProductoPuntoDeVenta.setGeometry(QtCore.QRect(800, 20, 311, 21))
        self.LineBuscarProductoPuntoDeVenta.setObjectName("LineBuscarProductoPuntoDeVenta")
        self.LabelBuscarProductoPuntoDeVenta = QtWidgets.QLabel(self.FramePuntoDeVenta)
        self.LabelBuscarProductoPuntoDeVenta.setGeometry(QtCore.QRect(680, 20, 106, 21))
        self.LabelBuscarProductoPuntoDeVenta.setObjectName("LabelBuscarProductoPuntoDeVenta")
        self.layoutWidget = QtWidgets.QWidget(self.FramePuntoDeVenta)
        self.layoutWidget.setGeometry(QtCore.QRect(750, 310, 311, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LabelCantidadProductos = QtWidgets.QLabel(self.layoutWidget)
        self.LabelCantidadProductos.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelCantidadProductos.setObjectName("LabelCantidadProductos")
        self.gridLayout.addWidget(self.LabelCantidadProductos, 0, 0, 1, 1)
        self.LabelUnidadProductos = QtWidgets.QLabel(self.layoutWidget)
        self.LabelUnidadProductos.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelUnidadProductos.setObjectName("LabelUnidadProductos")
        self.gridLayout.addWidget(self.LabelUnidadProductos, 0, 1, 1, 1)
        self.LabelTotalProductos = QtWidgets.QLabel(self.layoutWidget)
        self.LabelTotalProductos.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTotalProductos.setObjectName("LabelTotalProductos")
        self.gridLayout.addWidget(self.LabelTotalProductos, 1, 0, 1, 1)
        self.LabelCostoTotal = QtWidgets.QLabel(self.layoutWidget)
        self.LabelCostoTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelCostoTotal.setObjectName("LabelCostoTotal")
        self.gridLayout.addWidget(self.LabelCostoTotal, 1, 1, 1, 1)
        self.TablaDeVentas = QtWidgets.QTableWidget(self.FramePuntoDeVenta)
        self.TablaDeVentas.setGeometry(QtCore.QRect(10, 20, 651, 481))
        self.TablaDeVentas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TablaDeVentas.setAlternatingRowColors(True)
        self.TablaDeVentas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TablaDeVentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TablaDeVentas.setObjectName("TablaDeVentas")
        self.TablaDeVentas.setColumnCount(5)
        self.TablaDeVentas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeVentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeVentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeVentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeVentas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaDeVentas.setHorizontalHeaderItem(4, item)
        self.layoutWidget.raise_()
        self.BotonRealizarPago.raise_()
        self.TablaConsultarProducto.raise_()
        self.LineBuscarProductoPuntoDeVenta.raise_()
        self.LabelBuscarProductoPuntoDeVenta.raise_()
        self.TablaDeVentas.raise_()
        self.LayoutNombreDeUsuario = QtWidgets.QLabel(self.centralwidget)
        self.LayoutNombreDeUsuario.setGeometry(QtCore.QRect(910, 10, 141, 41))
        self.LayoutNombreDeUsuario.setObjectName("LayoutNombreDeUsuario")
        self.BotonCerrarSesion = QtWidgets.QPushButton(self.centralwidget)
        self.BotonCerrarSesion.setGeometry(QtCore.QRect(1031, 10, 121, 41))
        self.BotonCerrarSesion.setObjectName("BotonCerrarSesion")
        VentanaPuntoDeVenta.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaPuntoDeVenta)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 21))
        self.menubar.setObjectName("menubar")
        self.menuPunto_de_venta = QtWidgets.QMenu(self.menubar)
        self.menuPunto_de_venta.setObjectName("menuPunto_de_venta")
        self.menuInventario = QtWidgets.QMenu(self.menubar)
        self.menuInventario.setObjectName("menuInventario")
        self.menuTickets = QtWidgets.QMenu(self.menubar)
        self.menuTickets.setObjectName("menuTickets")
        VentanaPuntoDeVenta.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuPunto_de_venta.menuAction())
        self.menubar.addAction(self.menuInventario.menuAction())
        self.menubar.addAction(self.menuTickets.menuAction())

        self.retranslateUi(VentanaPuntoDeVenta)
        QtCore.QMetaObject.connectSlotsByName(VentanaPuntoDeVenta)

    def retranslateUi(self, VentanaPuntoDeVenta):
        _translate = QtCore.QCoreApplication.translate
        VentanaPuntoDeVenta.setWindowTitle(_translate("VentanaPuntoDeVenta", "MainWindow"))
        self.BotonAgregarProducto.setText(_translate("VentanaPuntoDeVenta", "Agregar Producto"))
        self.LabelBuscarProductoInventario.setText(_translate("VentanaPuntoDeVenta", "Buscar Producto: "))
        item = self.TablaDeInventario.horizontalHeaderItem(0)
        item.setText(_translate("VentanaPuntoDeVenta", "Codigo"))
        item = self.TablaDeInventario.horizontalHeaderItem(1)
        item.setText(_translate("VentanaPuntoDeVenta", "Nombre"))
        item = self.TablaDeInventario.horizontalHeaderItem(2)
        item.setText(_translate("VentanaPuntoDeVenta", "Categoria"))
        item = self.TablaDeInventario.horizontalHeaderItem(3)
        item.setText(_translate("VentanaPuntoDeVenta", "Precio"))
        item = self.TablaDeInventario.horizontalHeaderItem(4)
        item.setText(_translate("VentanaPuntoDeVenta", "Unidades"))
        item = self.TablaDeTickets.horizontalHeaderItem(0)
        item.setText(_translate("VentanaPuntoDeVenta", "Folio"))
        item = self.TablaDeTickets.horizontalHeaderItem(1)
        item.setText(_translate("VentanaPuntoDeVenta", "Productos"))
        item = self.TablaDeTickets.horizontalHeaderItem(2)
        item.setText(_translate("VentanaPuntoDeVenta", "Cantidad Productos"))
        item = self.TablaDeTickets.horizontalHeaderItem(3)
        item.setText(_translate("VentanaPuntoDeVenta", "Total"))
        item = self.TablaDeTickets.horizontalHeaderItem(4)
        item.setText(_translate("VentanaPuntoDeVenta", "Ticket"))
        self.LabelBuscarProductoTickets.setText(_translate("VentanaPuntoDeVenta", "Busca Ticket: "))
        self.BotonRealizarPago.setText(_translate("VentanaPuntoDeVenta", "Realizar Pago"))
        item = self.TablaConsultarProducto.horizontalHeaderItem(0)
        item.setText(_translate("VentanaPuntoDeVenta", "Codigo"))
        item = self.TablaConsultarProducto.horizontalHeaderItem(1)
        item.setText(_translate("VentanaPuntoDeVenta", "Nombre"))
        item = self.TablaConsultarProducto.horizontalHeaderItem(2)
        item.setText(_translate("VentanaPuntoDeVenta", "Precio"))
        item = self.TablaConsultarProducto.horizontalHeaderItem(3)
        item.setText(_translate("VentanaPuntoDeVenta", "Unidades"))
        self.LabelBuscarProductoPuntoDeVenta.setText(_translate("VentanaPuntoDeVenta", "Buscar Producto: "))
        self.LabelCantidadProductos.setText(_translate("VentanaPuntoDeVenta", "Productos: "))
        self.LabelUnidadProductos.setText(_translate("VentanaPuntoDeVenta", "Unidades: "))
        self.LabelTotalProductos.setText(_translate("VentanaPuntoDeVenta", "Total: "))
        self.LabelCostoTotal.setText(_translate("VentanaPuntoDeVenta", "Costo: "))
        item = self.TablaDeVentas.horizontalHeaderItem(0)
        item.setText(_translate("VentanaPuntoDeVenta", "Codigo"))
        item = self.TablaDeVentas.horizontalHeaderItem(1)
        item.setText(_translate("VentanaPuntoDeVenta", "Nombre"))
        item = self.TablaDeVentas.horizontalHeaderItem(2)
        item.setText(_translate("VentanaPuntoDeVenta", "Precio"))
        item = self.TablaDeVentas.horizontalHeaderItem(3)
        item.setText(_translate("VentanaPuntoDeVenta", "Unidades"))
        item = self.TablaDeVentas.horizontalHeaderItem(4)
        item.setText(_translate("VentanaPuntoDeVenta", "Total"))
        self.LayoutNombreDeUsuario.setText(_translate("VentanaPuntoDeVenta", "Usuario en cuestion:"))
        self.BotonCerrarSesion.setText(_translate("VentanaPuntoDeVenta", "Cerar sesion"))
        self.menuPunto_de_venta.setTitle(_translate("VentanaPuntoDeVenta", "Punto de venta"))
        self.menuInventario.setTitle(_translate("VentanaPuntoDeVenta", "Inventario"))
        self.menuTickets.setTitle(_translate("VentanaPuntoDeVenta", "Tickets"))
