from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaCobro(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaCobro, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaCobro.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnCobrarEfectivo.clicked.connect(self.cobrarEfectivo)
		self.btnCobrarTarjeta.clicked.connect(self.cobrarTarjeta)
	
	def cobrarEfectivo(self):
		return None
	
	def cobrarTarjeta(self):
		return None
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaCobro()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
