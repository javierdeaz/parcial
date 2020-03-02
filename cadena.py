from sys import argv
class Cadena:
    def __init__(self, expresion):
        self.expresion = expresion

    def validar_expresion(self, expresion):
        if expresion.find('{')==0 and expresion.rfind('}')==len(expresion)-1 and expresion.count(",,") == 0 and expresion.find(',')!=1:
            print('Expresion correcta\n')
        else:
            print('Error')