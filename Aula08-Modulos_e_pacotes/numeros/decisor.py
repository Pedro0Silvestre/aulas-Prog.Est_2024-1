"""
Seleciona ual operação será realizada conforme o input do usuário
"""
from numeros.operacoes import arit,exp   #pacotes dentro de pacotes 
# usamos ref relativas quando lido com módulos dentro de um mesmo pacote
from.operacoes import exp #usando referência relativa dois pontos levam para a raiz

def chama_calculadora(n1, operacao, n2):
    match operacao:
        case "+":
            return arit.soma(n1,n2)#chama função de soma
        case "-":
            return arit.subtracao(n1,n2)
            #chama função de subtração
        case "*":
            return arit.multiplicacao(n1,n2)
            #chama a função de multiplicação
        case "/":
            return arit.divisao(n1,n2)
            #chama a operação de multiplicação
        case "**":
            return exp.potencia(n1,n2)
        case "^":
            return exp.raiz(n1,n2)
        case _:
            return "OPERAÇÃO INVÁLIDA"
        

#ctrl : substitiui varios elementos por uma palavra
