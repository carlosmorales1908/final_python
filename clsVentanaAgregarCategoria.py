from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaAgregarCategoria(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaAgregarCategoria, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaAgregarCategoria.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnAgregar.clicked.connect(self.agregarCategoria)
	
	def agregarCategoria(self):
		return None
	
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaAgregarCategoria()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
