"""
Programação estruturada 
       
    Dicionários(Aula extra)

        25/03/2024
"""

"DICIONÁRIOS: Estruturas de dados compostas, semelhantes a listas e tuplas mas que conseguem guardar elçementos em posições personalizadas contendo indices textuais ao invez de numéricos. Identificados com Chaves{}"

dados = dict()
dados = {'nome':'Pedro','idade':20} #Com isso a posição 0 passa a se chamar nome e guarda o elemento Pedro enquanto a posição 1 vira idade e guarda o valor 20
#Declarar elementos se usa chavas para acessalos se usa colchetes

"Acessando elementos"
print(dados['nome'])
print(dados['idade'])

"ADICIONANDO ELEMENTOS"
dados['sexo'] = 'M'
print(dados['sexo'])

'REMOVENDO ELEMENTOS'
del dados['idade']  #Comando del elimina não só o valor ams tbm o indice o elemento como um todo
print(dados)

"ADICIONANDO VÁRIOS ELEMENTOS"
filme = {
    'titulo':'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}
print(filme)

"ACESSANDO AS PARTES"
print(filme.values()) #Retorna todos os valores contidos no dict
print(filme.keys()) #Retorna as classes dos elementos os indices
print(filme.items()) #Retorna values e keys juntos o indice junto do elemento no formato de tupla

"INTEGRANDO COM LOOP"
#K e V são variaveis que representam as keys e os itens, usadas como parametro no for elas percorrem todo os items do dict 
for k,v in filme.items():
    print(f'O {k} é {v}')

"ALTERANDO ELEMENTOS"
dados['nome'] = 'Leandro'
print(dados)



"INTEGRANDO DICIONARIOS E LISTAS"
def integracao():
    brasil = []

    estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
    estado2 = {'uf':'São Paulo','sigla':'SP'}

    brasil.append(estado1)
    brasil.append(estado2)

    print(brasil)
    print(brasil[0])
    print(brasil[1])
    print(brasil[0]['uf']) #acessando mulriplos elementos
    print(brasil[1]['uf']) #acessando mulriplos elementos

"INTEGRANDO COM FOR"

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input("Unidade Federativa:")
    estado['sigla'] = input("Sigla do Estado: ")
    brasil.append(estado.copy())#Método copy cria cópias do dicionário repartindo seus dados para na hora de serem inseridos inserir cada parte separadamente

for e in brasil:#loop para a lista
    for v in e.values():#loop para acessar elementos do dicionario dentro da lista
        print(v, end=' ')
    print()#pula de linha

"""FAZER EXERCÍCIOS DO GUANABARA DE TODOS OS CONTEÚDOS"""



