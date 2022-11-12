from nodo import nodo
class arbol:
    def __init__(self):
        self.raiz = None
        self.bInorden = ""
        self.bInorden1 = []
        self.bOrden = ""
        self.nivel = -1
        
    
    def __añadirRecursivo(self,nodo1,n):
        if nodo1.dato > n:
            if nodo1.izq is None:
                nodo1.izq = nodo(n)
            else:
                self.__añadirRecursivo(nodo1.izq,n)
        else:
            if nodo1.der is None:
                nodo1.der = nodo(n)
            else:
                self.__añadirRecursivo(nodo1.der,n)
            
       
    def añadir(self,dato):
        if self.raiz is None:
            self.raiz = nodo(dato) # raiz       
            
        else:
            self.__añadirRecursivo(self.raiz,dato)
    def mostrar(self):
        return self.bInorden1
    
    def __inorden(self,nodo1):
        if nodo1 is not None: 
            self.__inorden(nodo1.izq)
            self.bInorden1.append(nodo1.dato)
            self.__inorden(nodo1.der)
            
            
        else:
            self.nivel +=1  # Cuenta la cantidad de nodos
    
    
    def buscarInorden(self):
        self.__inorden(self.raiz)
    
    
    def __borraNodo (self,nodo1,dato):
        if nodo1.dato == dato:
            nodo1.dato = None
            nodo1.izq = None
            nodo1.der = None
            self.bInorden1 = []
            return True
        #else: False
        
        else:
            if nodo1.dato > dato:
                if self.__borraNodo(nodo1.izq,dato): 
                    nodo1.izq = None
                    self.__inorden(self.raiz)
            else:
                if self.__borraNodo(nodo1.der,dato):
                    nodo1.der = None
                    self.__inorden(self.raiz)

    def borrarNodo (self,dato):
        self.__borraNodo(self.raiz,dato)
        
        
    
            
arbol1 = arbol()
arbol1.añadir(5)
arbol1.añadir(2)
arbol1.añadir(34)
arbol1.añadir(70)
arbol1.añadir(70)
arbol1.añadir(80)
arbol1.añadir(80)
arbol1.añadir(80)
arbol1.añadir(7)
arbol1.buscarInorden()
print(arbol1.mostrar())
print(arbol1.raiz)

arbol1.borrarNodo(70)
print(arbol1.mostrar())             
        

    
        
