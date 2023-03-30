import clsConexion as cone

class clsCrudUsuarios:
	def __init__(self):
		self.bd = cone.clsConexion()
	
	def getTabla(self):
		query = "SELECT * FROM usuarios"
		resultado = self.bd.run_query(query)
		if(len(resultado) == 0):
			return None
		else:
			return resultado
	
	def getCuenta(self, usu):
		query = f"SELECT usuarios.usuario, usuarios.contrasenia FROM usuarios WHERE usuarios.usuario='{usu}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
