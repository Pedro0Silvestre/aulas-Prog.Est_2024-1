"""
Exercício 1: equações de segundo grau
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.

Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.

"""

def bhaskara ():
    a = float(input("Insira o valor de A:"))
    b = float(input("Insira o valor de B:"))
    c = float(input("Insira o valor de C:"))
    delta = b ** 2 -4 * a *c
    raiz_1 = (-b + (delta)**1/2)/2*a
    raiz_2 = (-b - (delta)**1/2)/2*a
    print("X1=",raiz_1," X2=",raiz_2)

bhaskara()

"""
Exercício 2: anos bissextos
Elabore um programa em Python que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

O programa deve utilizar apenas as funções print(), input() e int(), além dos operadores lógicos and, or ou not e de operadores aritméticos ou de comparação necessários.

"""
def is_bissexto():
    ano = int(input("Informe o ano:"))
    resto_por_4 = ano%4
    resto_por_100 = ano%100
    resto_por_400 = ano%400
    divisivel_por_400= (resto_por_400 == 0)
    divisivel_por_4 = (resto_por_4 == 0)
    print((divisivel_por_400) or (resto_por_100 != 0 and divisivel_por_4))

is_bissexto()








