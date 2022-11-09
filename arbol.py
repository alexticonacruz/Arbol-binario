from nodo import nodo
global a1
class arbol:
    def __init__(self):
        self.raiz = None
        
    
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
            print("if")
        else:
            print("else")
            self.__añadirRecursivo(self.raiz,dato)
    def mostrar(self):
        print(self.raiz)
    
    
    def __inorden(self,nodo1,cadena):
        if nodo1 is not None:
            self.__inorden(nodo1.izq)
            print(nodo1.dato)
            cadena = cadena + nodo1.dato
            self.__inorden(nodo1.der)
            return a1
    
    
    def buscarInorden(self,cadena):
        self.__inorden(self.raiz,cadena)
    
            
arbol1 = arbol()
arbol1.añadir(5)
arbol1.añadir(2)
arbol1.añadir(34)
arbol1.añadir(70)
arbol1.mostrar("")
print(arbol1.buscarInorden())
                
        

    
        
