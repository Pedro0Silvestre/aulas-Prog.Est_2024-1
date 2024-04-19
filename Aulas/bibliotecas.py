"""Programação estruturada  AULA 08

Bibliotecas e pacotes MAIS USADOS

19/04/2024"""


import random as rnd #Forma de criar uma sigle menor para chamar a função
from random import randint # Importar apenas uma função e não a biblioteca toda 
import time
import pygame 

"re (regular expressions)"
#cria regras para validar strings 9(Validar cpfs, emails etc.)

"datetime & calendar "
#gera anos e datas de um calendário 
# consegue ler datas transformando datas inseridas num usuário para strings com os dias da semana

"enum(enumerate)"
# enumera itens
# defindindo conjuntos de dados em categorias

"math"
# armazena formulas matemáticas
# arrdondamento,raiz quadrada, exponencial,log, constantes matématicas(pi, num euller etc..)

"random"
#gera valores aleatorios
# choices (escolhe elemento qualquer de uma lista)
#choices (mais de uma escolha)
# shuffle: altera a ordenação de uma lista (embaralhamento)

"pathlib/glob/os. path"
# usado par lidar com caminhos de diretorios em diferentes sistemas operacionais
# usado para acessar dietorios de seu sistemas (pathlib ou os.path)
#glob: identifica padrões em caminos de arquivos

"shutil"
# operações complexas de arquivos
# movimenta diretorios, deleta diretorias, alterna uso de discos

"sqlite3"
# usado em banco de dados, SQL

"csv"
#pacote de manipulação de arquivo csv(separados por vírgula)

"JSON"
# Manipula arquivos web
#compromete a segurança

"time"
#tmie.time() registra um tempo em segundos desde o inicío dos computadores(1 jan de 1970 ; 00:00)
# time.time() analiza diferenças de tempo
#usada para anlisar o tempo de execução de uma função
def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat *= i
    return fat

inicio   = time.time()
fatorial(1000000)
print(f"Tempo decorrido: {time.time() - inicio:.2f} segundos.") #calcula o tempo decorrido da função fatorial, mede tempos de respostas etc.
#marque time.time antes de inciar a função e dps assim vendo a diferença

time.sleep(3) #Aguarda x segundos para rodar o resto do código

"Logging"
#ajuda no rastreamento de bugs registrando o passo a passo na execução que elvo a um bug

"tkinter"
# Trabalha com graficos e outros dados visuais como caixa de dialogo etc

"typing"
#typing.rint: ajuda na melhor seleção e uso de variaveis mostrando otipode dados que elas originalmente foram armazenadas

"unittest"
#trestes unitários

"syst"
# lida com osistema que esta esxucutandoo codigo como pythoin, terminal etc.

"Bibliotecas externas"
# Verifique o historico da biblioteca antes de usar, se há manutenção, documentação , pagina, referencias (wuanto mais infirmações melhor)
# ver se está dentro de um repositorio publico (github) ver avaliação, num de commits
# verifique o pypy = registro de pacotes usados no python
# com usar?
# entre no terminal do vscode pyhton e use o comando pip install (nome da biblioteca)
#automaticamente busca no pypy a biblioteca que vc digitou e instala no pc
# 