
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import sys
import clsVentanaAgregarProducto as venAgPr
import clsVentanaModificarProducto as venMoPr
import clsVentanaEliminarProducto as venElPr
import clsVentanaAgregarCategoria as venAgCa
import clsCrudProductos as crudProductos


class clsVentanaInventario(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaInventario, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaInventario.ui',self)
		self.crudProd = crudProductos.clsCrudProductos()
		self.tabla = self.crudProd.getTabla()
		self.setupUi()
	
	def setupUi(self):
		self.btnAgregarProducto.clicked.connect(self.agregarProducto)
		self.btnModificarProducto.clicked.connect(self.modificarProducto)
		self.btnEliminarProducto.clicked.connect(self.eliminarProducto)
		self.btnAgregarCategoria.clicked.connect(self.agregarCategoria)
		self.btnBuscar.clicked.connect(self.buscarProducto)
		self.loadTabla()
	
	def agregarProducto(self):
		self.agP = venAgPr.clsVentanaAgregarProducto()
		self.agP.show()
	
	def modificarProducto(self):
		self.mp = venMoPr.clsVentanaModificarProducto()
		self.mp.show()
	
	def eliminarProducto(self):
		self.elim = venElPr.clsVentanaEliminarProducto()
		self.elim.show()
	
	def agregarCategoria(self):
		self.agC = venAgCa.clsVentanaAgregarCategoria()
		self.agC.show()
	
	def buscarProducto(self):
		cod = self.lineBuscarProducto.text()
		fil = self.crudProd.getProducto(cod)
		if(fil != None):
			self.loadFila(fil)
		else:
			self.loadTabla()
	
	def insertarProductoEnTabla(self):
		try:
			codigo = self.lineCodigoProd.text()
			fila = self.crudProductos.getProducto(codigo)
			desc = fila[0][3]
			prc = float(fila[0][4])
			prl = float(fila[0][5])
			stock = int(fila[0][6])
			cant = int(self.lineCantidad.text())
			if(fila != None):
				if(cant <= stock):
					self.crudCarrito.insertarProductoCarrito(codigo, desc, prc, prl, cant)
					self.reiniciarLine()
					self.table = self.crudProductos.getTabla()
					self.loadTabla()
					self.hide()
					self.show()
				else:
					self.venSt = clsVenInSt.clsVentanaInsuficienteStock()
					self.venSt.show()
			else:
				self.venEr = clsVenProdInex.clsVentanaErrorEliminar()
				self.venEr.show()
        
		except Exception as e:
			print('Error en la insercion ' + str(e))
	
	def loadTabla(self):
		try:
			result = self.crudProd.getTabla()
			self.listaInventario.setRowCount(0)
			self.listaInventario.setColumnCount(5)
			self.listaInventario.setHorizontalHeaderLabels(["codigo", "descripcion", "precio Contado", "precio Lista", "stock"])
			for elem in result:
				rows = self.listaInventario.rowCount()
				self.listaInventario.setRowCount(rows + 1)
				self.listaInventario.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
				self.listaInventario.setItem(rows, 1, QTableWidgetItem(str(elem[2])))
				self.listaInventario.setItem(rows, 2, QTableWidgetItem(str(elem[3])))
				self.listaInventario.setItem(rows, 3, QTableWidgetItem(str(elem[4])))
				self.listaInventario.setItem(rows, 4, QTableWidgetItem(str(elem[5])))
			self.listaInventario.resizeColumnsToContents()
		except Exception as e:
			print('Error al cargar datos en la grilla ' + str(e))
	
	def loadFila(self, fil):
		try:
			# result = self.crudProd.getTabla()
			self.listaInventario.setRowCount(0)
			self.listaInventario.setColumnCount(5)
			self.listaInventario.setHorizontalHeaderLabels(["codigo", "descripcion", "precio Contado", "precio Lista", "stock"])
			for elem in fil:
				rows = self.listaInventario.rowCount()
				self.listaInventario.setRowCount(rows + 1)
				self.listaInventario.setItem(rows, 0, QTableWidgetItem(str(elem[1])))
				self.listaInventario.setItem(rows, 1, QTableWidgetItem(str(elem[3])))
				self.listaInventario.setItem(rows, 2, QTableWidgetItem(str(elem[4])))
				self.listaInventario.setItem(rows, 3, QTableWidgetItem(str(elem[5])))
				self.listaInventario.setItem(rows, 4, QTableWidgetItem(str(elem[6])))
			self.listaInventario.resizeColumnsToContents()
		except Exception as e:
			print('Error al mostrar la fila' + str(e))
	
	def tablaVacia(self):
		rowI = 0
		self.listaInventario.setRowCount(rowI+1)
		if rowI == 0:
			columns = 5
			self.listaInventario.setColumnCount(columns)
			self.listaInventario.setHorizontalHeaderLabels(["codigo", "descripcion", "precio Contado", "precio Lista", "stock"])
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaInventario()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
