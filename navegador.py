class Navegador(object):
	def __init__ (nombre,version):	
		self.version=version
		self.nombre=nombre
		self.tabs=[]
		self.nombre=[]
	def crear_tab(URL,nombre,URL):
		self.tabs.append(URL)
		self.nombres.append(nombre)
	def cam_URl(self, tab_numero,nombre,URL):
		self.tabs[tab_numero]=URL
		self.nombre[tab_numero]=nombre
	def cerrar_t (self,tab_numero):
		self.tabs.pop[tab_numero]
		self.tabs.pop[tab_numero]
	def cerrar_todos(self)
		self.tabs=[]
		self.nombre=[]
