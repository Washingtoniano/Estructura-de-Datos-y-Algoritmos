#2^n-1 n=cantfichas
from nodo import nodo
class pila():
	__tope:None
	__cant:int

	def __init__(self):
		self.__tope=None
		self.__cant=0
	
	def insertar(self,dato):
		unnodo=nodo(dato)
		unnodo.setSiguiente(self.__tope)
		self.__tope=unnodo
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
		aux=self.__tope
		while aux!=None:
			print(aux.getDato())
			aux=aux.getSig()
		
	