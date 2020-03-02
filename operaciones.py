from sys import argv
from cadena import Cadena

class Operaciones(Cadena):
    def __init__(self,expresion,expresion2):
        Cadena.__init__(self, expresion)
        self.expresion2 = expresion2

    def op_conjuntos(self, expresion, expresion2):
        j = expresion.replace('{', '').replace('}', '')
        k = expresion2.replace('{', '').replace('}', '')

        x = j[1:len(j)]
        a = k[1:len(k)]

        lista1 = x.split()
        lista2 = a.split()

        primera  = set(lista1)
        segunda = set(lista2)

        print(f'Union')
        print(primera.union(segunda))
        print(f'Intercepcion')
        print(primera.intersection(segunda))