from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys
import clsCrudProductos as clsCrudProd
import clsConexion as conexion
import clsVentanaProductoEliminado as venPrElim
import clsVentanaErrorEliminar as venErrorElim
import MySQLdb
class clsVentanaEliminarProducto(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaEliminarProducto, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaEliminarProducto.ui',self)
		self.setupUi()
		self.crudPro = clsCrudProd.clsCrudProductos()
	
	def setupUi(self):
		self.btnEliminar.clicked.connect(self.eliminarProducto)
		
	
	
	def eliminarProducto(self):
		try:
			cod = self.lineEditCodigo.text()
			if(self.crudPro.existe(cod) == 1):
				self.crudPro.delete(cod)
				self.venPr = venPrElim.clsVentanaProductoEliminado()
				self.venPr.show()
			else:
				self.venEr = venErrorElim.clsVentanaErrorEliminar()
				self.venEr.show()
		except Exception as e:
			print('Error en eliminacion ' + str(e))
		
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaEliminarProducto()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
