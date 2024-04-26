"""
Interface por linha de comando (cli)
Calculadora
Apresenta as opções da calculadora e as operações disponiveis.
Chama as operações de calculo, conforme a seleção do usuário.
"""

#Referência absoluta - diferentes pacotes dentros de um mesmo projeto 
from numeros import decisor

def exibe_opcoes_disponiveis():
    print("""Bem-Vindo a calculadora!
          Insira um número e pressione ENTER, em seguida digite uma operação(*,-,+,/) e pressione ENTER.
          Por fim, insira outro número e pressione ENTER mais ma vez. O resultado será exibido em seguida.""")
    
def iniciar():
    exibe_opcoes_disponiveis()
    n1 = float(input)
    operacao = input()
    n2 = float(input())
    print(decisor.chama_calculadora(n1, operacao, n2))





iniciar()