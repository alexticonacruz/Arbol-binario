from nodo import nodo
class arbol:
    def __init__(self):
        self.raiz = None
        #self.bInorden = ""
        self.bInorden1 = []
        #self.bOrden = ""
        self.nivel = -1
        self.bPreOrden1 = []
        self.bPosOrden1 = []
        
    #   ---------- Añadir un nodo   ----------------------
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
        
    #   --------   Devuelve el resultado del bInorden Guardado  ---------
    def mostrar(self):
        return self.bInorden1
    
    #   -------- Acomoda y registra la busque
    def __inorden(self,nodo1):
        if nodo1 is not None: 
            self.__inorden(nodo1.izq)
            self.bInorden1.append(nodo1.dato)
            self.__inorden(nodo1.der)
            
            
        else:
            self.nivel +=1  # Cuenta la cantidad de nodos
    
    
    def buscarInorden(self):
        self.bInorden1 = []
        self.__inorden(self.raiz)
        
    #   -----   Borra Un nodo especifico    ------------------
    
    def __borraNodo (self,nodo1,dato):
        if nodo1.dato == dato:
            nodo1.dato = None
            nodo1.izq = None
            nodo1.der = None
            self.bInorden1 = []
            return True
        
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
        
        if self.raiz.dato == dato:
            self.raiz = None
            self.bInorden1 = []
            
        else:
            self.__borraNodo(self.raiz,dato)
    
            
    #   ---------------------------------------------------------------------------------    
            
    # Ordenado Preorden 1. imprime  => Raiz, izq, der.
    
    def __preOrden(self,nodo1):
        if nodo1 is not None:
            self.bPreOrden1.append(nodo1.dato)
            self.__preOrden(nodo1.izq)
            self.__preOrden(nodo1.der)
            
    
    def preorden(self):
        self.__preOrden(self.raiz)
        
    #   ------- Ordenado PosOrden  imprime => izq , der, Raiz  --->   izq = 5, der = 15,  raiz = 10,      ---
    def __posOrden(self,nodo1):
        if nodo1 is not None:
            self.__posOrden(nodo1.izq)
            #self.bPosOrden1.append(nodo1.dato)  # imprime => 5 , 10 , 15
            self.__posOrden(nodo1.der)
            self.bPosOrden1.append(nodo1.dato)  # imprime => 5 , 10 , 15
            
        
    
    def posorden(self):
        self.__posOrden(self.raiz)
arbol1 = arbol()
arbol1.añadir(45)
arbol1.añadir(23)
arbol1.añadir(65)
arbol1.añadir(2)
arbol1.añadir(38)
arbol1.añadir(7)
arbol1.añadir(52)
arbol1.añadir(96)
arbol1.añadir(48)
# arbol1.añadir(25)
# arbol1.añadir(19)

# arbol1.añadir(10)
# arbol1.añadir(5)
# arbol1.añadir(15)
# arbol1.añadir(3)
# arbol1.añadir(7)
# arbol1.añadir(2)
arbol1.posorden()
print(arbol1.bPosOrden1)
# arbol1.añadir(5)
# arbol1.añadir(2)
# arbol1.añadir(34)
# arbol1.añadir(70)
# arbol1.añadir(70)
# arbol1.añadir(80)
# arbol1.añadir(80)
# arbol1.añadir(80)
# arbol1.añadir(7)
# arbol1.buscarInorden()
# print(arbol1.mostrar())
# print(arbol1.raiz)

# arbol1.borrarNodo(5)
# print(arbol1.mostrar())             
        
# a = arbol1
# print("dañino")
# print(a)
# a = None
# print(a)
    
        
