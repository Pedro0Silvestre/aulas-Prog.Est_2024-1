"""
Programação estruturada 2024.1
25/03/2024
listas (aula extra)

"""
"Listas são uma estrutura de dados composta que armazena vários valores dentro de colchetes"

lsita_compras = ['banana','maçã','laranja']
print(lsita_compras)

"""apartir da posição do elemento dentro da lista vc pode acessa-lo especificamente (indice começa no zero)"""
print(lsita_compras[1])

"em listas podemos usar indices negativos"
print(lsita_compras[-1]) #imprimi laranja pois esse é o termo anterior ao zero 

"ADICIONANDO ELEMENTOS EM LISTAS"
#APPEND: Método append adiciona elementos no final de uma lista
lsita_compras.append('beterraba')
print(lsita_compras)

#INSERT: Recebe dois argumentos o indice onde o elemento deve ser inserido e o valor a ser inserido. o insert não remove o valor que anteriormente ocupava aquele posição ele insire o novo e desloca os demais uma posição a frente 
lsita_compras.insert(0,'chocolate') #insere chocolate na posição 0
print(lsita_compras)

"APAGANDO ELEMENTOS"
#DEL: A função DEL recebe um array e um índice e elimina o valor que ocupava essa posição
del lsita_compras[4]
print(lsita_compras)

#REMOVE: Esse método recebe o VALOR que vc deseja remover da lista 
lsita_compras.remove('chocolate')
print(lsita_compras)

lsita_compras.append('Carro')
print(lsita_compras)

"PASSANDO ELEMENTOS DE UMA LISTA PARA OUTRA"
#Lista vazia
lista_sonhos = []
#armazenando valor removido numa variavel
sonho = lsita_compras.pop(-1) #método pop recebe um indice e remove o elemento desse indice do array(faz ele saltar do array)
print(sonho)

#Adicionando elemento em sonhos
lista_sonhos.append(sonho)
print(lista_sonhos)

"EXERCITANDO LISTAS"
#Inserindo valor de um usuário
tarefas = []
"usando o FOR"
# for i in range(4):
#     tarefa = input("Insira uma tarefa:")
#     tarefas.append(tarefa)

# print(tarefas)

"usando while"
# tarefa = " "
# while tarefa != "" :
#     tarefa = input("Insira uma Tarefa:")
#     tarefas.append(tarefa)

print(tarefas[1:3]) #Printa elementos nesse intervalo de 1 até 3 tirando o 3

"SORT: Método que ordena arrays em ordem crescente por padrão"

lojas=['Rio de Janeiro','São Paulo','Curitiba']
faturamento=[10000, 20000, 50000]

# .sort(reverse=True) #Ordena em ordem contrario decrescente
faturamento.sort() 
print(faturamento)

"TUPLAS: estruturas de dados representadas por parenteses que associam dois valores. Podemos usar tuplas para associar o estado ao seu respectivo faturamento"

resultados = []

for i in range(3):
    tupla = (lojas[i-1],faturamento[i-1])
    resultados.append(tupla)

print(resultados)
print(resultados[1][1]) #ao se passar dois indicies vc primeiro acessa o indice do array e dps o da tupla 





