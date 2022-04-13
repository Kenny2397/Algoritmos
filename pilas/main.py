from Pila import Pila
from Nodo import Nodo

pila = Pila()

persona1 = Nodo("Alex", "Mtz", 1)
persona2 = Nodo("Ben", "Frank", 2)
persona3 = Nodo("Carlos", "Hdz", 3)
persona4 = Nodo("Diana", "Montoya", 4)

pila.push(persona1)
# pila.push(persona2)
# pila.push(persona3)
# pila.push(persona4)
print('-----')
pila.imprimePila()