from sys import argv
from cadena import Cadena
from operaciones import Operaciones

script, expresion, expresion2 = argv


nueva_cadena = Cadena(expresion)
nueva_cadena1 = Cadena(expresion2)
op=Operaciones(expresion,expresion2)
nueva_cadena.validar_expresion(nueva_cadena.expresion)
nueva_cadena1.validar_expresion(nueva_cadena1.expresion)
op.op_conjuntos(expresion,expresion2)
