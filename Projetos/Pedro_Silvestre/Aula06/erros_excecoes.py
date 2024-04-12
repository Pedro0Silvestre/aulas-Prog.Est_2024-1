"""
Programação Estruturada
2024.1
12/04/2024

Tratamento de erros e exceções
try / except

QUANDO USAR:
- Usar quando não souber qual exceção pode subir
- OU quando sei qual exceção pode subir, mas não sei como o código chega lá
"""
#Quando falamos de erros de sintaxe em python falamos de erros de sintaxe.
# erros de sintaxe são quando o código foi escrito erroneamente, nesses erros o computador nem roda o cdigo nem começa a ler

#Exceções: interrompem a execução do programa diferente dos erros o código é lido até o momento que há a exceção. Erros de tipo, erros de divisão etc.
# print(5 /0) # zero division
# print("1" + 2) # inteiro + string 

#Como identificar exceções ?
#Devemos evitar usar try /except pois eles quebram o fluxo do código, para erros identificaveis devmos concertar de maneira manual, try serve para erros não identificaveis


"COMO USAR?"
def divisao(a,b):
    try: #Cada try deve estar ligado a pelo menos um except, caso não haverá um erro de sintaxe
        print(a/b)
    except ZeroDivisionError: # alinhamos o except ao try e escrevemos o tipo do erro esperado e a mensagem de erro
        print("Erro! O DIVISOR NÃO PODE SER ZERO")
    except TypeError:
        print("ERRO! ambos os parâmetros precisam ser numéricos")

# Podemos usar except sem indicar o erro que esperamos, entratanto isso não é recomendado caso vc já saiba o tipo do erro
divisao(10,2)
divisao(10,0)
divisao("abc",2)

# O except deve ser usado no menor trecho possível e sempre deixando dentro do try apenas os trechos do código que possam conter erros 
def terceira_letra():
    try:
        nome = input("Informe seu nome:")#devemos tira o input de dentro do try pois ele n pode dar erro
        print(f"A terceira letra do seu nome é {nome(2)}.")
    except Exception as err: # nesse caso vc n sabe qual erro vai ocorrer, então vc cria uma exceção e passa o erro que ocorreu na variavel err, e depois printar justamento o tipo de erro que ocorreu com type
        print(f"Erro desconhecido. Erro: {err}") #SEMPRE USADO 
        print(type(err))
    else: # O else num try só roda caso seu código n caia em nenhuma exceção nenhum except acima
        print("Leitura dos dados bem sucedidos")
    finally: # O finally sempre é executado independente de ocorrer erro ou não 
        print("Fim da função")

""" 
Num programa de erros vc sempre começa pelo try, obrigatoriamente vc terá um except genérico(não ideal)
você pod eter inumeros excepts, o else será lido caso n haja erro e o finally roda sempre independente de ocorrer erro ou não
"""

#Criando um erro:
class TamanhoExcedidoError(Exception):
    pass
#Nesse caso você está criando um erro personalizado que n existia

def exibe_num(numero):
    if numero > 10: # O RAISE sobe um erro (cria) uma exceção customizada nesse caso caso o valor for maior que 10 vc passa um erro para algo q n daria erro
        raise ValueError #RAISE é muito comum 
    
    print(numero)

exibe_num(15)

def func1():
    raise NotImplementedError
def func2():
    raise NotImplementedError
# essa forma de passar o not implemented error é comum em projetos grandes onde alguém vai executar uma função que não foi implementada ainda






