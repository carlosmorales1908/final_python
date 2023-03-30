import clsConexion as conexion

class clsCrudProductos():
	def __init__(self):
		self.bd = conexion.clsConexion()
	
	def getTabla(self):
		query = "SELECT producto.codigo, producto.serie, producto.descripcion, producto.precioContado, producto.precioLista, producto.stock, producto.idCategoria FROM producto"
		resultado = self.bd.run_query(query)
		if(len(resultado) == 0):
			return None
		else:
			return resultado
	
	def getProducto(self, cod):
		query = f"SELECT * FROM producto WHERE producto.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def getPrecioLista(self, cod):
		query = f"SELECT producto.precioContado FROM producto WHERE producto.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def getPrecioContado(self, cod):
		query = f"SELECT producto.precioLista FROM producto WHERE producto.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado)==0):
			return None
		else:
			return resultado
	
	def insertarProductoEnTabla(self, cod, ser, desc, prc, prl, st, cat):
		query = "INSERT INTO producto (codigo, serie, descripcion, precioContado, precioLista, stock, idCategoria) VALUES ('%s','%s','%s','%f','%f','%d','%d');"%(cod, ser, desc, prc, prl, st, cat)
		self.bd.run_query(query)
	
	def delete(self, cod):
		query = f"DELETE FROM producto WHERE producto.codigo = '{cod}' ;"
		self.bd.run_query(query)
	
	def existe(self, cod):
		query = f"SELECT * FROM producto WHERE producto.codigo = '{cod}'"
		resultado = self.bd.run_query(query)
		if(len(resultado) != 0):
			return 1
		else:
			return 0
	
	def update(self, cod, ser, desc, prc, prl, st, cat):
		query = "UPDATE producto SET codigo ='%s', serie='%s', descripcion='%s',precioContado='%f', precioLista='%f', stock = '%d', categoria = '%s', WHERE codigo = '%d';"%(cod, ser, desc, prc, prl, st, cat)
		self.bd.run_query(query)
	
	def updateStock(self, cod, cant):
		query = "UPDATE producto SET stock = '%d' WHERE codigo = '%d';"%(cod, cant)
		self.bd.run_query(query)
		
def main():
    return 0

if __name__ == '__main__':
    main()
