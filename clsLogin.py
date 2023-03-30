from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys
import clsCrudUsuarios as crudUsuarios
import clsVentanaPrincipal as venPpal
import clsVentanaErrorLogin as venError

class clsLogin(QtWidgets.QMainWindow):
	
	def __init__(self):
		super(clsLogin, self).__init__()
		uic.loadUi('E:/Unsa/Python/2021/TP FINAL/correcto/login.ui',self)
		self.bd = crudUsuarios.clsCrudUsuarios()
		self.setupUi()
	
	def setupUi(self):
		self.btnIngresar.clicked.connect(self.ingresar)
	
	def ingresar(self):
		usuarioIngresado = self.lineUsuario.text()
		contraseniaIngresada = self.lineContrasenia.text()
		cuenta = self.bd.getCuenta(usuarioIngresado)
		if cuenta != None:
			if contraseniaIngresada == cuenta[0][1]:
				self.ven = venPpal.clsVentanaPrincipal()
				self.ven.show()
				self.hide()
			else:
				self.error = venError.clsVentanaErrorLogin()
				self.error.show()
		else:
			self.error = venError.clsVentanaErrorLogin()
			self.error.show()
	
	
def main():
	app = QApplication(sys.argv)
	objeto = clsLogin()
	objeto.show()
	app.exec_()

if __name__ == '__main__':
	main()
