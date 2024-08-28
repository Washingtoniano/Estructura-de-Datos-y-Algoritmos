#2^n-1 n=cantfichas
from nodo import nodo
class pila():
	__tope:None
	__cant:int
	__indice:int
	__actual:None
	def __iter__(self):
		return self
	def __next__(self):
		if self.__indice==self.__cant:
			self.__actual=self.__tope
			self.__indice=0
			raise StopIteration
		else:
			dato=self.__actual.getDato()
			self.__actual=self.__actual.getSig()
			self.__indice+=1
			return dato
	def __init__(self):
		self.__tope=None
		self.__tope=None
		self.__cant=0
		self.__indice=0
	def insertar(self,dato):
		unnodo=nodo(dato)
		unnodo.setSiguiente(self.__tope)
		self.__tope=unnodo
		self.__actual=unnodo
		self.__cant+=1
	def vacia(self):
		return self.__tope==None
	
	def eliminar(self):
		if(self.vacia()==True):
			print("Lista vacia")
		else:
			aux=self.__tope.getDato()
			self.__tope=self.__tope.getSig()
			self.__cant-=1
			return aux
	def recorrer(self):
		for dato in self:
			print (dato)
		
		
	