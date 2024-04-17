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
len()
list.append()
list.insert()
list.extend()
list.pop()
list.remove()
list.index()
list.count()
min()
max()
sum()
list.sort()
sorted()
