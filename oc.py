from sys import argv
from cadena import Cadena

script, expresion, expresion2 = argv

nueva_cadena = Cadena(expresion)
nueva_cadena1 = Cadena(expresion2)
nueva_cadena.validar_expresion(nueva_cadena.expresion)
nueva_cadena1.validar_expresion(nueva_cadena1.expresion)