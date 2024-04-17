"LISTAS"
alunos = ["João","Alessandra","Felipe","Bianca"]
#uma das principais estruturas de dados para conter variaos elementos 
"ACESSANDO ELEMENTOS"
print(alunos[0])#Acessando elementos
print(alunos[-1])#Índices negativos podem ser acessados 
print(alunos[1:3])#SLICING: Metodo de acessar sublistas, selecionando um intervalo, o primeiro é o indice do primeiro elemento e o segundo é exclusive
print(alunos[1:4:2])#STEP: Podemos adicionar no slicing um terceiro elemento contendo o tamanho do passo
# omitir o primeiro número faz com que devolva desde o início da lista
print(alunos[:3]) 
# omitir o segundo número faz com que vá até o final da lista
print(alunos[6:])

"OPERAÇÕES COM LISTAS"
#Verifica se um determinado valor é igual a um dos elementos de uma lista 
if "Bianca" in alunos:
    print("Aluno localizado")
#Percorre todos os elementos de uma lista 
for aluno in alunos:
    print(aluno)
#percorre os índices e os valores dos elementos de uma lista, simultaneamente, retornando primeiro o indice e edpois o elemento
for indice, aluno in enumerate(alunos):
    print(indice + 1, aluno, sep="-")
# junta duas listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista = lista1 + lista2  # [1, 2, 3, 4, 5, 6]
# repete uma dada lista um número determinado de vezes
lista = 3 * lista1  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

"MÉTODOS E EFUNÇÕES DE LISTAS"
# len()
# list.append()
# list.insert()
# list.extend()
# list.pop()
# list.remove()
# list.index()
# list.count()
# min()
# max()
# sum()
# list.sort()
# sorted()

"TUPLAS"
#Listas em que não podemos alterar seus elementos ou seu tamanho. IMUTÁVEIS
tupla = (1,2,3)
print(tupla[1]) # 2
print(tupla[:2]) # (1, 2)
# tupla.append(4) -> vai subir uma exceção!
# O uso mais comum de tuplas é quando queremos que uma função retorne informações associadas entre si, que não devem ser modificadas por quem chamou a função.

"CONJUNTOS"
#Conjuntos são outro caso particular de listas. Eles são coleções desordenadas de elementos, e não possuem elementos repetidos. Para representar conjuntos, utilizamos chaves ou a função set():
frutas = {"laranja", "pera", "mamão", "abacaxi", "mamão", "laranja"}
print(frutas) # {"laranja", "pera", "mamão", "abacaxi"}

"DICIONÁRIO"
aluno = {
    "nome": "123 de oliveira 4",
    "matrícula": 12345,
    "data de nascimento": "11/11/2000",
    "notas": {
        "ap1": 6.7,
        "ap2": 7.7,
        "ac": 4.5
    }
}
# kEYS(), VALUES(), ITENS(). Acessar elementos num dicionário
pauta = {
    # chave: valor
    "a": 4.0,
    "b": 5.5,
    "c": 9.2,
    "d": 8.7,
    "e": 6.6
}

print(pauta)
print(pauta.keys())
print(pauta.values())

if "h" in pauta:
    print(pauta["h"])

# iterar pelas chaves -> o uso do .keys() é dispensável
for aluno in pauta:
    print(aluno)

# iterar pelos valores
for nota in pauta.values():
    print(nota)

# iterar pelo dicionário inteiro
for aluno, nota in pauta.items():
    print(aluno, nota)
    