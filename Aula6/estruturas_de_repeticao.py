"""
Programação estruturada 
2024.1
15/03/2024

Estruturas de repetição
- while
- for
"""

"estruturas de repetição são blocos de código que são executados mais de uma vez com base num determinado teste lógico"

"loop infinito"
def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1  #decremento

contagem_regressiva(5) #teste verdadeiro
contagem_regressiva(-5) #teste falso

"""quando usar o while? quando não saberemos quantas vezes o loop deverá se repetir"""

"""FOR: Usada para quando há um numero de repetições limitado ou quando vc já souber quantas vezes ele irá se repetir. Ou para coleções de dados """

"RANGE: Estrutura de dados mais básica do python, essa estrutura retorna uma sequenia de numeros inteiros continuos(em ordem)"
"range(10): passando um oparametro apenas para o range o parametro será o final de sua sequencia e se iniciará do zero"
"range(1,10): passando dois parametros o primeiro é o start o segundo será o stop ( STOP SEMPRE EXCLUSIVE ELE N É INCLUSO o STAR INCLUSIVE)"
"range(1,10,2): Passando três parâmetros o primeiro é o start o segundo o stop e o terceiro é o step(de (incremento do contador)"
"caso o interavel n permita que a sequencia seja executada o loop não será rodado"

print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))

"""Usando o FOR: primeiro vc define uma varivel de contador e usa o range para representar o número de vezes que será executado"""
def regreessiva_2(num):
    for cont in range(num,-1,-1):
        print(cont)

regreessiva_2(5)
"No caso de variaveis inutéis que nãos etão sendo acessadas vc usa o underscore(_) como caractere coringa subistituindo a variavel que vc deseja eliminar (atentar as variaveiz cinza is not acessed)"
def ola_varias_vezes(num_vezes):
    for _ in range(num_vezes):
        print("olá")
ola_varias_vezes(3)

def pula_mult_3(max):
    for num in range(1,max + 1):
        if num % 3 == 0 :
            continue #Continue interrompe o loop uma sequeência ele pula o elemento atual e vai para o prox
        print(num)

pula_mult_3(15)

"break, sai da estrutura de repetição pula ela"
def para_antes_de_10(max):
    for num in range(1,max + 1):
        print(num)
        if num == 9:
            break

para_antes_de_10(20)

"""o else no for apenas é executado caso o break n seja executado n tenha entrado no break"""

def e_primo (num):
    for div in range(2,num):
        if num % div == 0:
            print("não é primo")
            break
    else:
        print("é primo")

e_primo(7)

"""
EXERCÍCIO RESOLVIDO 1
Elaborar uma função conta_pares(min, max) para exibir todos os valores entre min e max, com um incremento de 2, 
separando-os com um hífen. Ex.: 2 – 4 – 6 – 8 – 10 – 12 – 14.

"""

def conta_pares(min,max):
    if min % 2 == 1:
        for cont in range(min + 1,max+1,+2):
            print(cont,end="-")
    else:
        for cont in range(min,max+1,+2):
            print(cont,end="-")  #end : parametro do print que define oque virá no final do q será printado


# conta_pares(2,10)
# conta_pares(1,10)

"""
EXERCÍCIO 3
Faça um programa que calcule o fatorial de um número inteiro positivo fornecido pelo usuário. Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
"""
def fatorial(num):
    fat = 1
    for i in range(1,num + 1 ):
        fat = fat * i 
    print(fat)

fatorial(5)










