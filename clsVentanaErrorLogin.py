from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

class clsVentanaErrorLogin(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsVentanaErrorLogin, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/ventanaErrorLogin.ui',self)
		self.setupUi()
	
	def setupUi(self):
		self.btnAceptar.clicked.connect(self.aceptar)
	
	def aceptar(self):
		self.hide()
	
	
def main():
	app = QApplication(sys.argv)
	objeto = clsVentanaErrorLogin()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()

        
