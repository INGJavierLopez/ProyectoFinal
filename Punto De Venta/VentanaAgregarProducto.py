# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAgregarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaAgregarProducto(object):
    def setupUi(self, VentanaAgregarProducto):
        VentanaAgregarProducto.setObjectName("VentanaAgregarProducto")
        VentanaAgregarProducto.setFixedSize(382, 421)
        self.centralwidget = QtWidgets.QWidget(VentanaAgregarProducto)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 381, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FrameCodigo = QtWidgets.QFrame(self.frame)
        self.FrameCodigo.setGeometry(QtCore.QRect(10, 60, 361, 51))
        self.FrameCodigo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCodigo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCodigo.setObjectName("FrameCodigo")
        self.Codigo = QtWidgets.QLineEdit(self.FrameCodigo)
        self.Codigo.setGeometry(QtCore.QRect(80, 9, 271, 31))
        self.Codigo.setObjectName("Codigo")
        self.LabelCodigoAgregarProducto = QtWidgets.QLabel(self.FrameCodigo)
        self.LabelCodigoAgregarProducto.setGeometry(QtCore.QRect(10, 10, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCodigoAgregarProducto.setFont(font)
        self.LabelCodigoAgregarProducto.setObjectName("LabelCodigoAgregarProducto")
        self.BotonAgregarAgregarProducto = QtWidgets.QPushButton(self.frame)
        self.BotonAgregarAgregarProducto.setGeometry(QtCore.QRect(70, 370, 251, 31))
        self.BotonAgregarAgregarProducto.setObjectName("BotonAgregarAgregarProducto")
        self.LabelTitulo = QtWidgets.QLabel(self.frame)
        self.LabelTitulo.setGeometry(QtCore.QRect(80, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LabelTitulo.setFont(font)
        self.LabelTitulo.setObjectName("LabelTitulo")
        self.FrameNombre = QtWidgets.QFrame(self.frame)
        self.FrameNombre.setGeometry(QtCore.QRect(10, 120, 361, 51))
        self.FrameNombre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameNombre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameNombre.setObjectName("FrameNombre")
        self.Nombre = QtWidgets.QLineEdit(self.FrameNombre)
        self.Nombre.setGeometry(QtCore.QRect(80, 9, 271, 31))
        self.Nombre.setObjectName("Nombre")
        self.LabelNombreAgregarProducto = QtWidgets.QLabel(self.FrameNombre)
        self.LabelNombreAgregarProducto.setGeometry(QtCore.QRect(10, 10, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelNombreAgregarProducto.setFont(font)
        self.LabelNombreAgregarProducto.setObjectName("LabelNombreAgregarProducto")
        self.FrameCategoria = QtWidgets.QFrame(self.frame)
        self.FrameCategoria.setGeometry(QtCore.QRect(10, 180, 361, 51))
        self.FrameCategoria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCategoria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCategoria.setObjectName("FrameCategoria")
        self.Categoria = QtWidgets.QLineEdit(self.FrameCategoria)
        self.Categoria.setGeometry(QtCore.QRect(80, 9, 271, 31))
        self.Categoria.setObjectName("Categoria")
        self.LabelCategoriaAgregarProducto = QtWidgets.QLabel(self.FrameCategoria)
        self.LabelCategoriaAgregarProducto.setGeometry(QtCore.QRect(10, 10, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCategoriaAgregarProducto.setFont(font)
        self.LabelCategoriaAgregarProducto.setObjectName("LabelCategoriaAgregarProducto")
        self.FramePrecio = QtWidgets.QFrame(self.frame)
        self.FramePrecio.setGeometry(QtCore.QRect(10, 240, 361, 51))
        self.FramePrecio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramePrecio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramePrecio.setObjectName("FramePrecio")
        self.Precio = QtWidgets.QLineEdit(self.FramePrecio)
        self.Precio.setGeometry(QtCore.QRect(80, 9, 271, 31))
        self.Precio.setObjectName("Precio")
        self.LabelPrecioAgregarProducto = QtWidgets.QLabel(self.FramePrecio)
        self.LabelPrecioAgregarProducto.setGeometry(QtCore.QRect(10, 10, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelPrecioAgregarProducto.setFont(font)
        self.LabelPrecioAgregarProducto.setObjectName("LabelPrecioAgregarProducto")
        self.FrameUnidades = QtWidgets.QFrame(self.frame)
        self.FrameUnidades.setGeometry(QtCore.QRect(10, 300, 361, 51))
        self.FrameUnidades.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameUnidades.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameUnidades.setObjectName("FrameUnidades")
        self.Unidades = QtWidgets.QLineEdit(self.FrameUnidades)
        self.Unidades.setGeometry(QtCore.QRect(80, 9, 271, 31))
        self.Unidades.setObjectName("Unidades")
        self.LabelUnidadesAgregarProducto = QtWidgets.QLabel(self.FrameUnidades)
        self.LabelUnidadesAgregarProducto.setGeometry(QtCore.QRect(10, 10, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelUnidadesAgregarProducto.setFont(font)
        self.LabelUnidadesAgregarProducto.setObjectName("LabelUnidadesAgregarProducto")
        VentanaAgregarProducto.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaAgregarProducto)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarProducto)

    def retranslateUi(self, VentanaAgregarProducto):
        _translate = QtCore.QCoreApplication.translate
        VentanaAgregarProducto.setWindowTitle(_translate("VentanaAgregarProducto", "MainWindow"))
        self.LabelCodigoAgregarProducto.setText(_translate("VentanaAgregarProducto", "Código"))
        self.BotonAgregarAgregarProducto.setText(_translate("VentanaAgregarProducto", "Aregar Prodcuto"))
        self.LabelTitulo.setText(_translate("VentanaAgregarProducto", "Registrar Productos"))
        self.LabelNombreAgregarProducto.setText(_translate("VentanaAgregarProducto", "Nombre"))
        self.LabelCategoriaAgregarProducto.setText(_translate("VentanaAgregarProducto", "Categoria"))
        self.LabelPrecioAgregarProducto.setText(_translate("VentanaAgregarProducto", "Precio"))
        self.LabelUnidadesAgregarProducto.setText(_translate("VentanaAgregarProducto", "Unidades"))
