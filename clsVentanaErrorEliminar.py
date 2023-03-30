from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaErrorEliminar(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaErrorEliminar, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaErrorEliminar.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnAceptar.clicked.connect(self.aceptar)
	
	def aceptar(self):
		self.hide()
	
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaErrorEliminar()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
