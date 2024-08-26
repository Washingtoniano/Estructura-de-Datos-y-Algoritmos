class nodo():
	__dato:object
	__sig:object
	def __init__(self,dato):
		self.__dato=dato
		self.__sig=None
	def setSiguiente(self,sig):
		self.__sig=sig
	def getDato(self):
		return self.__dato
	def getSig(self):
		return self.__sig