from Nodo import Nodo

class Pila:
    
    def __init__(self):
        self.top = None
        
    def push(self, nodo):
        aux = self.top
        # if top==None:
        #     top = nodo
        # else:
        #     nodo.next = top
        #     top = nodo
        if aux != None:
            nodo.next = aux
        self.top = nodo   ## aqui indico que mi top es el nuevo nodo, si le pongo aux = nodo no funciona.
    
    
    def pop(self):
        top = self.top
        if top == None:
            return 'No hay nodos'
        else:
            self.top = top.next
            top.next = None
            
        # if top != None:
        #     self.top = top.next
        #     top.next = None
        
    def imprimePila(self):
        aux = self.top
        while aux != None:
            print(aux.nombre)
            aux = aux.next