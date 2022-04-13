from Pila import Pila
from Nodo import Nodo

# pila = Pila()

# persona1 = Nodo("Alex", "Mtz", 1)
# persona2 = Nodo("Ben", "Frank", 2)
# persona3 = Nodo("Carlos", "Hdz", 3)
# persona4 = Nodo("Diana", "Montoya", 4)

# pila.push(persona1)
# # pila.push(persona2)
# # pila.push(persona3)
# # pila.push(persona4)
# print('-----')
# pila.imprimePila()

expresion ="(2+3+4)-{3+4}+[6*7]"

pila=Pila()

parentesis = Nodo('(')
corchete = Nodo('[')
llaves = Nodo('{')

def validaExpresion(expresion):
    for c in expresion:
        if c =='(':
            pila.push(parentesis)
        if c == '[':
            pila.push(corchete)
        if c == '{':
            pila.push(llaves)
