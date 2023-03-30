import clsConexion as conexion

class clsCrudCarrito():
	def __init__(self):
		self.bd = conexion.clsConexion()
	
	def getTabla(self):
		query = "SELECT carrito.codigo, carrito.descripcion, carrito.precioContado, carrito.PrecioLista, carrito.cantidad FROM carrito"
		resultado = self.bd.run_query(query)
		if(len(resultado) == 0):
			return None
		else:
			return resultado
	
	def getCantidad(self, cod):
		query = f"SELECT carrito.cantidad FROM carrito WHERE codigo = {cod}"
		resultado = self.bd.run_query(query)
		if(len(resultado) == 0):
			return None
		else:
			return resultado
	
	def getProductoCarrito(self, cod):
		query = f"SELECT * FROM carrito WHERE carrito.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def getPrecioLista(self, cod):
		query = f"SELECT carrito.precioLista FROM carrito WHERE carrito.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def getPrecioContado(self, cod):
		query = f"SELECT carrito.precioContado FROM carrito WHERE carrito.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def insertarProductoCarrito(self, cod, desc, prc, prl, cant):
		query = "INSERT INTO carrito (codigo, descripcion, precioContado, precioLista, cantidad) VALUES ('%s','%s','%f','%f','%d');"%(cod, desc, prc, prl, cant)
		self.bd.run_query(query)
	
	def delete(self, cod):
		query = f"DELETE FROM carrito WHERE carrito.codigo = '{cod}' ;"
		self.bd.run_query(query)
	
	def existe(self, cod):
		query = f"SELECT * FROM carrito WHERE carrito.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado) != 0):
			return 1
		else:
			return 0
	
	def update(self, cod, desc, prc, prl, cant):
		query = "UPDATE carrito SET codigo ='%s', descripcion='%s',precioContado='%f', precioLista='%f', cantidad = '%d', WHERE codigo = '%d';"%(cod, desc, prc, prl, cant)
		self.bd.run_query(query)
	
	def updateCant(self, cant, cod):
		query = "UPDATE carrito SET cantidad = '%d', WHERE codigo = '%s';"%(cant, cod)
		self.bd.run_query(query)
	
	def borrarDatos(self):
		query = "TRUNCATE TABLE carrito"
		self.bd.run_query(query)
	
	
	
def main():
    return 0

if __name__ == '__main__':
    main()
