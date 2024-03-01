"""
Programação estruturada
2024.1
01/03/2024

Funções
- encapsulamento de informações
- Isolar o comportamento para facilitar o uso
- Organizar o código
"""
#CONSTANTES SÃO DECLARADAS NO NICIO DO CÓDIGO, VALORES QUE NÃO SERÃO ALTERADOS NO DECORRES DO CÓDIGO



def traco(sep,tamanho):
    print(sep * tamanho)

# " : " dois pontos em python representam um bloco de código

#Como declarar função em python def(define) + nome da funcao + parenteses() + dois pontos : qq indica o bloco de código
def cabecalho(titulo,sep="-",tamanho=30): #Definindo varios parametros
    traco(sep , tamanho)
    print(titulo)   #Em python a identação é vital para o código caso uma função esteja com identação errada sem identar ou com espaços diferentes o código dará erro
    traco(sep , tamanho)

#PARAMETRO CHAVE: def cabecalho(sep= - , tamanho= 30) É um padrão pré definido, caso vc execute a função e n passe o valor desse parametro ele assumirá o valor padrão
#- Pode mudar a ordem em que o parametro é atribuido ao invez de definir sep dps tamanho pode passar tamanho = x e dps sep = y
# Parâmetro posicional sempre antes do parametro chave

# PARÂMETROS: Nesse caso titulo é um parametro que pode ser passado ao se chamar a função
    #Ao se por titulo como parametro será criado uma VARIAVEL TITULO de escopo local


# Chamando uma função
cabecalho("Relatório de despesas","-", 30)
cabecalho("Folha de pagamento",tamanho =25, sep=".") # Caso vc passe o nome do parametro seguido do valor a ordem do parametro n irá influenciar

#Não colocar parenteses significa que estou falando da função e não chamando
print(cabecalho)
print(cabecalho("olá","+", 30))
x=2

# Por padrão uma função retorna o valor none
def soma(a,b):
    return a + b #O return sempre é usado para retornar o valor então ao invez de na função vc usar o print para exibir vc primeiro retorna o valor e dps pede para imprimir

print(soma(2,5) + soma(4,9))

def e_par (num):
    return num % 2 == 0

print(e_par(8))
print(e_par(55))

def troca_valores(a,b) :
    return b,a #esse retorno é uma tupla

print(troca_valores(8,0))

#Pode usar parametros multiplos para atribuir multiplas variaveis


# Escopo de variáveis
def func1():
    a = 10
    print(a) # escopo local ( só acessado dentro dessa função)
    print(x) # escopo global (acessado em qualquer lugar do código , pois foi declarado fora de uma função)

print("-" * 30)
func1()

def func2(x):
    x = 999
    print(x) # escopo local tem precedência
#AO se declarar uma variavel local com mesmo nome de uma global ele irá criar na memoria uma nova variavel local com o mesmo nome da global
# pode ter varias variaveis de mesmo nome

func2(100)
print(x)

def func3():
    global x # NÃO UYSAR!!! a plavra reservada global é usada para numa função local alterar ou acessar uma varivel global
            #IMPORTANTE Não usar variveis globais é uma má prática use LOCAIS>GLOBAL
    x = 0
    print(x)

func3()
print(x) # 0 pois alteramos o x global

