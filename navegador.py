class navegador(object):
	def __init__ (nombre,version):	
		self.version=version
		self.nombre=nombre
		self.tabs=[]
		self.cerrar=False
	def abrir(URL,nombre):
		tab=(URL,snombre)
		tabs.append(tab)
	def cerrar(self, i):
		self.tabs.pop(i)
	def cerrar_t (self,tab):
		self.cerrar=True
	def mostrar_tab(self,tabs):
		return 
	def guardar(self,tabs):
