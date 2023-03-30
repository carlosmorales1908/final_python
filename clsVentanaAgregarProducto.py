from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys
import clsCrudProductos as clsCrudProd
import clsConexion as conexion
import clsVentanaProductoAgregadoExito as clsVenPrAgEx
import clsVentanaExisteProducto as clsVenExPr
import clsVentanaInventario as venInv
class clsVentanaAgregarProducto(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaAgregarProducto, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaAgregarProducto.ui',self)
		self.setupUi()
		self.bd = conexion.clsConexion()
		self.crudProd = clsCrudProd.clsCrudProductos()
		self.ven = venInv.clsVentanaInventario()
	
	def setupUi(self):
		self.btnGuardar.clicked.connect(self.insertarProducto)
		
	def reiniciarVentana(self):
		self.lineEditCodigo.clear()
		self.lineEditSerie.clear()
		self.lineEditDescripcion.clear()
		self.lineEditPrecioContado.clear()
		self.lineEditPrecioLista.clear()
		self.lineEditStock.clear()
		self.lineEditCategoria.clear()
	
	def insertarProducto(self):
		try:
			cod = self.lineEditCodigo.text()
			ser = self.lineEditSerie.text()
			desc = self.lineEditDescripcion.text()
			prc = float(self.lineEditPrecioContado.text())
			prl = float(self.lineEditPrecioLista.text())
			st = int(self.lineEditStock.text())
			cat = int(self.lineEditCategoria.text())
			if(self.crudProd.existe(cod) == 0):
				self.crudProd.insertarProductoEnTabla(cod, ser, desc, prc, prl, st, cat)
				self.reiniciarVentana()
				self.venAgE = clsVenPrAgEx.clsVentanaProductoAgregadoExito()
				self.venAgE.show()
			else:
				self.venFail = clsVenExPr.clsVentanaExisteProducto()
				self.venFail.show()
		except Exception as e:
			print('Error en la insercion ' + str(e))

def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaAgregarProducto()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
