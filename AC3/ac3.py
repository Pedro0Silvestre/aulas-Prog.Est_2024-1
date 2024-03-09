""" Exercício 1: triângulos
 Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string,
  "Escaleno", "Isósceles" ou "Equilátero", conforme o tipo do triângulo. 
  A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo. 
  Use a função abaixo como teste:
"""
def existencia_triangulo(lado1,lado2,lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

def Equilatero (lado1,lado2,lado3):
    return lado1 == lado2 and lado2 == lado3

def Isosceles(lado1,lado2,lado3):
    return lado1 == lado2 or lado2 == lado3 or lado1 == lado3

#Tentando fazer do jeito top-down mas falhando miseravelmente

def determina_tipo_triangulo(lado1,lado2,lado3):
    if existencia_triangulo(lado1,lado2,lado3):
        if Equilatero (lado1,lado2,lado3):
            print("Triangulo equilátero")
        elif Isosceles(lado1,lado2,lado3):
            print("Triangulo isóceles")
        else:
            print("Triangulo escaleno")
    else:
        print("Triangulo inexistente")

determina_tipo_triangulo(3,5,3)

"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma string indicando o dia da semana equivalente,
 considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. 
A função deve retornar uma string vazia caso o número seja inválido. Use a função abaixo como teste:
"""

def dia_semana(dia):
    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Dia invalido")

for i in range(1,9):
    dia_semana(i)
        

"""          
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao, que recebem dois números cada uma e retornam 
o resultado da operação indicada. Em seguida, crie uma função que elabora uma interface por linha de comando (CLI)
, que lê dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação inválida" se o usuário 
inserir uma mensagem diferente das quatro operações.
"""
def le_conta():
    #lê os números e o tipo de operação 
    num1 = float(input("Informe um número:"))
    num2 = float(input("Informe outro número:"))
    operador = input("Informe a operação: ")
    return num1,num2,operador

def operacao_valida(operador):
    #retorna true ou false caso o operador seja válido
    match operador:
        case "soma" | "subtração" | "multiplicação" | "divisão":
            return True
    print("OPERAÇÃO INVÁLIDA!")

def soma(num1,num2):
    #Realiza a soma
    return num1 + num2
def subtracao(num1,num2):
    #Realiza a subtração
    return num1 - num2
def multiplicacao(num1,num2):
    #Realiza a multiplicação
    return num1 * num2
def divisao(num1,num2):
    #Realiza a divisão
    return num1 / num2
def realiza_operacao(num1,num2,operador):
    #Reconhece o operador e realiza a operação
    match operador:
    
        case "soma":
            return soma(num1,num2)
        case "subtração":
            return subtracao(num1,num2)
        case "multiplicação":
            return multiplicacao(num1,num2)
        case "divisão":
            return divisao(num1,num2)



def main():
    num1,num2,operador= le_conta()
    if operacao_valida(operador):
        return print(realiza_operacao(num1,num2,operador))

main()




    
