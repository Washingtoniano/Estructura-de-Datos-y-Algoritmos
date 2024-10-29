import numpy as np
class trabajo():
    __arreglo:np.ndarray
    __op:int
    __cant:int
    def __init__(self,cant=4):
        self.__cant=cant
        self.__arreglo=np.empty(self.__cant,dtype=object)
        self.__cant=0
    