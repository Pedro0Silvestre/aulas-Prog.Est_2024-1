"""
RUN AND DEBUG
parte do vscode feita para debuggar códigos, com essa ferramenta vc concegue ir analizando o código passo a passo
de inicio vc define um breakpoin (pontinho vermelho) seu ponto de inicío
e vai passando passo a passo da função analizando cada parte do código separadamente
"""
def func1(n):
    print(11)

def func2(x):
    x = int(input("Informe um número:"))
    func1(10)

def func3():
    nomes = input("Informe os nomes, separados por espaço: ")
    nomes = nomes.split(" ") 
    func2(nomes)

def main():
    func3()

main()


