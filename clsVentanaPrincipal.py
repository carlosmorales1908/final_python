
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import sys
import clsVentanaInventario as venInv
import clsVentanaCobro as venCob
import clsCrudProductos as clsCrudProd
import clsCrudCarrito as clsCrudCarr
import clsVentanaErrorEliminar as clsVenProdInex
import clsVentanaInsuficienteStock as clsVenInSt
import clsVentanaCantidadCero as venCantCer

class clsVentanaPrincipal(QtWidgets.QMainWindow):
	
	def __init__(self):
		super(clsVentanaPrincipal, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaPrincipal.ui',self)
		self.crudProductos = clsCrudProd.clsCrudProductos()
		self.crudCarrito = clsCrudCarr.clsCrudCarrito()
		self.table = self.crudCarrito.getTabla()
		self.f=-1
		self.c=-1
		self.setupUi()
		self.loadTable()
	
	def setupUi(self):
		self.loadTable()
		self.btnInventario.clicked.connect(self.abrirInventario)
		self.btnCancelarVenta.clicked.connect(self.cancelarVenta)
		self.btnCancelarProducto.clicked.connect(self.cancelarProducto)
		self.btnCobrar.clicked.connect(self.cobrar)
		self.btnAgregarProducto.clicked.connect(self.agregarProductoCarrito)
		self.qTableCarrito.cellClicked.connect(self.cell_was_clicked)
		self.cartelPrecioEfectivo.setText(str(0))
		self.cartelPrecioTarjeta.setText(str(0))
	
	def insertarProductoEnCarrito(self):
		try:
			codigo = self.lineCodigoProd.text()
			fila = self.crudProductos.getProducto(codigo)
			print(fila)
			print("pasa 1")
			desc = fila[0][3]
			print("pasa 2")
			prc = float(fila[0][4])
			prl = float(fila[0][5])
			stock = int(fila[0][6])
			cant = int(self.lineCantidad.text())
			self.loadTable()
			if(fila != None):
				idProd = self.crudCarrito.existe(codigo)
				if(cant > 0):
					if(idProd == 1):
						if(cant <= stock):
							self.crudCarrito.updateCant(cant, codigo)
							# self.actualizaPrecioEfectivoExistente(cod, cant)
							# self.actualizaPrecioListaExistente(cod, cant)
							self.reiniciarLine()
							self.table = self.crudCarrito.getTabla()
							self.loadTable()
						else:
							self.venSt = clsVenInSt.clsVentanaInsuficienteStock()
							self.venSt.show()
							self.loadTable()
					else:
						self.crudCarrito.insertarProductoCarrito(codigo, desc, prc, prl, cant)
						self.reiniciarLine()
						# self.actualizaPrecioEfectivo(codigo, cant)
						# self.actualizaPrecioListaExistente(codigo, cant)
						self.table = self.crudCarrito.getTabla()
						self.loadTable()
				else:
					self.venCant = venCantCer.clsVentanaCantidadCero()
					self.venCant.show()
			else:
				self.venEr = clsVenProdInex.clsVentanaErrorEliminar()
				self.venEr.show()
        
			self.loadTable()
		except Exception as e:
			print('Error en la insercion ' + str(e))
			self.loadTable()
	
	def loadTable(self):
		if self.table != None:
			try:
				result = self.crudCarrito.getTabla()
				self.qTableCarrito.setRowCount(0)
				self.qTableCarrito.setColumnCount(5)
				self.qTableCarrito.setHorizontalHeaderLabels(["codigo", "descripcion", "precio Contado", "precio Lista", "cantidad"])
				for elem in result:
					rows = self.qTableCarrito.rowCount()
					self.qTableCarrito.setRowCount(rows + 1)
					self.qTableCarrito.setItem(rows, 0, QTableWidgetItem(str(elem[0])))
					self.qTableCarrito.setItem(rows, 1, QTableWidgetItem(str(elem[1])))
					self.qTableCarrito.setItem(rows, 2, QTableWidgetItem(str(elem[2])))
					self.qTableCarrito.setItem(rows, 3, QTableWidgetItem(str(elem[3])))
					self.qTableCarrito.setItem(rows, 4, QTableWidgetItem(str(elem[4])))
				self.qTableCarrito.resizeColumnsToContents()
			except Exception as e:
				print('Error al cargar datos en la grilla ' + str(e))
		else:
			self.tablaVacia()
	
	def modificarStock(self):
		result = self.crudCarrito.getTabla()
		for elem in result:
			rows = self.qTableCarrito.rowCount()
			
	
	def tablaVacia(self):
		rowI = 0
		print(self.table)
		self.qTableCarrito.setRowCount(rowI+1)
		if rowI == 0:
			columns = 5
			self.qTableCarrito.setColumnCount(columns)
			self.qTableCarrito.setHorizontalHeaderLabels(["codigo", "descripcion", "precioContado", "precioLista", "cantidad"])
			
	
	def abrirInventario(self):
		self.inv = venInv.clsVentanaInventario()
		self.inv.show()	
	def abrirInventario(self):
		self.inv = venInv.clsVentanaInventario()
		self.inv.show()
	
	def cancelarVenta(self):
		self.crudCarrito.borrarDatos()
		self.table = self.crudCarrito.getTabla()
		self.loadTable()
		# self.tablaVacia()
		# self.loadTable()
	
	def cell_was_clicked(self, row, column):
		self.f=row
		self.c=column
	
	def cancelarProducto(self):
		if self.f>-1 and self.c>-1:
			cod = self.qTableCarrito.item(self.f, 0).text()
			try:
				self.crudCarrito.delete(cod)
				print ("Exito. Eliminacion correcta del carrito, codigo= " + str(cod))
				self.qTableCarrito.removeRow(self.f)
			except Exception as e:
				print('Error en la eliminacion ' + str(e))
		else:
			print ("Error. No seleccionó fila")
	
	def cobrar(self):
		self.cob = venCob.clsVentanaCobro()
		self.cob.show()
		self.cancelarVenta()
	
	def agregarProductoCarrito(self):
		self.insertarProductoEnCarrito()
	
	def reiniciarLine(self):
		self.lineCodigoProd.clear()
		self.lineCantidad.clear()
	
	def actualizaPrecioEfectivo(cod, cant):
		pa = int(self.cartelPrecioEfectivo.getText())
		np = pa + (self.crudProductos.getPrecioContado(cod) * cant)
		self.cartelPrecioEfectivo.setText(str(np))
	
	def actualizaPrecioLista(cod, cant):
		pa = int(self.cartelPrecioTarjeta.getText())
		np = pa + (self.crudProductos.getPrecioContado(cod) * cant)
		self.cartelPrecioEfectivo.setText(str(np))
	
	def actualizaPrecioEfectivoExistente(cod, cant):
		existe = self.carrito.getCantidad(cod)
		dif = cant - existe
		pa = int(self.cartelPrecioEfectivo.getText())
		np = pa + (self.crudProductos.getPrecioContado(cod) * dif)
		self.cartelPrecioEfectivo.setText(str(np))
	
	def actualizaPrecioListaExistente(cod, cant):
		existe = self.carrito.getCantidad(cod)
		dif = cant - existe
		pa = int(self.cartelPrecioTarjeta.getText())
		np = pa + (self.crudProductos.getPrecioContado(cod) * dif)
		self.cartelPrecioEfectivo.setText(str(np))
	
	
	# def loadTable(self):
		
		# print(self.table)
		# if self.table != None:
			# for row in self.table:
				# rowI = 0
				# self.qTableCarrito.setRowCount(rowI+1)
				# self.qTableCarrito.setHorizontalHeaderLabels(["codigo", "descripcion", "precioContado", "precioLista", "cantidad"])
				# if rowI == 0:
					# columns = len(row)
					# self.qTableCarrito.setColumnCount(columns)
				# columns = len(row)
				# for columnJ in range(columns):
					# myValue = row[columnJ]
					# cell = QTableWidgetItem(str(myValue))
					# self.qTableCarrito.setItem(rowI, columnJ, cell)
	
				# rowI = rowI + 1
		# else:
			# print("si")
			# self.tablaVacia()
	
def main():
    app = QApplication(sys.argv)
    objeto = clsVentanaPrincipal()
    objeto.show()
    app.exec_()

if __name__ == '__main__':
    main()
