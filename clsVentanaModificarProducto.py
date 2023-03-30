from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaModificarProducto(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaModificarProducto, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaModificarProducto.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnGuardar.clicked.connect(self.guardarCambios)
		self.btnBuscar.clicked.connect(self.buscarProducto)
	
	def guardarCambios(self):
		return None
	
	def buscarProducto(self):
		return None
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaModificarProducto()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
