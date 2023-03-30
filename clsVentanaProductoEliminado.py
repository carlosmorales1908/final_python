from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaProductoEliminado(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaProductoEliminado, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaProductoEliminado.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnAceptar.clicked.connect(self.aceptar)
	
	def aceptar(self):
		self.hide()
	
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaProductoEliminado()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
