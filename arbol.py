from nodo import nodo
class arbol:
    def __init__(self):
        self.raiz = None
        self.bInorden = ""
        self.bOrden = ""
        
    
    def __añadirRecursivo(self,nodo1,n):
        if nodo1.dato > n:
            if nodo1.izq is None:
                nodo1.izq = nodo(n)
            else:
                self.__añadirRecursivo(nodo.izq,n)
        else:
            if nodo1.der is None:
                nodo1.der = nodo(n)
            else:
                self.__añadirRecursivo(nodo1.der,n)
            
       
    def añadir(self,dato):
        if self.raiz is None:
            self.raiz = nodo(dato)
        else:
            self.__añadirRecursivo(self.raiz,dato)
    def mostrar(self):
        print(self.bInorden)
    
    
    def __inorden(self,nodo1):
        if nodo1 is not None:
            self.__inorden(nodo1.izq)
            print(nodo1.dato)
            if self.bInorden is "":
                self.bInorden = f"{nodo1.dato}"
            else:
                self.bInorden = f"{self.bInorden}  {nodo1.dato}"
                
            self.__inorden(nodo1.der)
            
    
    
    def buscarInorden(self):
        self.__inorden(self.raiz)
    
            
arbol1 = arbol()
arbol1.añadir(5)
arbol1.añadir(2)
arbol1.añadir(34)
arbol1.añadir(70)
arbol1.buscarInorden()
arbol1.mostrar()
                
        

    
        
