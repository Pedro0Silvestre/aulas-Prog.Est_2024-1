"""
Ponto de entrada do programa.

Realiza uma operação de calculadora.
"""

from cli import calculadora 
#Referência absoluta, utilizada para arquivos na raiz, assim podendo buscar as diferenes pastas também na raiz 

print(__name__) #indica modulo que deu o start do programa oque vc importou 

def main():
    calculadora.iniciar()

if __name__ == "__main__": # evita que o modulo seja sempre executado, apenas se quem ele estiver chamando for a main
    main()
# usaado para criar um comportamento que so vai acontecer se esse for o ponto de partida do programa VER OBSERVAÇÃO DEPOIS EM CASA DE COMO USAR ISSO 
