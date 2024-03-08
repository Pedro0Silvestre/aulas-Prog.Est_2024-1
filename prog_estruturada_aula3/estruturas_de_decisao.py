"""
 Programação Estruturada
 2024.1
 08/03/2024

 Estruturas de decisão:
- if/elif/else
- match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno == ("T"): #elif = else + if na mesma linha 
        print("Boa tarde!")
    elif turno == ("N"):
        print("Boa noite!")
    else:
        print("Dado inválido!")
        
# Return encerra a execução da função por isso nos casos de RETURN n precisamos usar o else apenas uma seuqencia de if 
def saudacao2(turno):
     if turno == "M":
        return"Bom dia!"
     if turno == ("T"): #elif = else + if na mesma linha 
        return("Boa tarde!")
     if turno == "N":
        return"Boa noite!"
        
     return"Dado inválido!" #caso nehuma condição atendida ele retorna o caso padrão automaticamente
    
    

saudacao("N")
saudacao("M")
saudacao("T")
saudacao("A")

def le_nome():
    nome = input("Informe o seu nome:")
    #if nome == "" (string vazia = FALSE)
    if not nome:
        print("Erro! Entrada inválida!")
    
    return nome

#Ternário
def e_par(num):
    if num % 2:
        return "é ímpar"
    return "é par"

#Ternário é para sre usado para uma unica instrução não para varios casos de elif 
def e_par2(num):
    return "é ímpar" if num % 2 else "é par" #estrutura do ternário (inica com o comando return e dps as condições )
print(e_par2(16))

#MATCH CASE ( Famoso switch case)
#use o match com interfaces por linhas de comando, para cmparações imediatas e limitadas

def saudacao3 (turno):
    match turno:
        case "M":
            print("Bom dia !")
        case "T":
            print("Boa tarde")
        case "N":
            print("Boa noite!")
        case _: # O underscore (_) é o caso padrão para dados diferentes das respostas refernciadas no match 
            print("Caso inválido")

def aprovado (conceito):
    match conceito:
        case "Bom"|"Ótimo"|"Excelente": #O pip é usado como MATCH (Exclusivamente) ele serve para reduzir códigos muito redundantes vc encgloba varias respostas num case só
            return "Aprovado"
        case _:
            return "Reprovado"


"""
Exercício

implemente um programa que receba(use parâmetros) dois numeros e retorne o maior deles

"""

def maior(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    return "Números iguais!"

print(maior(9,9))

"""
Faça um programa que verifique se uma letra é vogal ou consoante

"""
#O match burla o efeito do python de numa opração logica com OU sempre RETORNAR O SEGUNDO 
def e_vogal(letra):
    match letra:
        case "a"|"e"|"i"|"o"|"u":
            return "É vogal"
    return "É consoante"
        
print(e_vogal("k"))

"""
exercicio 06

Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.

"""
#O MATCH não funciona para casos de comparação nesse caso devemos usar o if
# Python entende intervalos no if ( ex: if 7 <= media < 10)
def situacao_final (nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    if media == 10:
            print("Aprovado com distinção")
    elif media>= 7:
            print("Aprovado")
    elif media < 7 :
            print("Reprovado")
    else:
        print("Nota inválida!")

situacao_final(10,10,10)





