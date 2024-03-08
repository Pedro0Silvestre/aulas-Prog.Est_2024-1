"""
Programação Estruturada
2024.1
08/03/2024

AC4

Desenvolva uma versão inicial de CLI (command-line interface) para analisar se um aluno foi ou não aprovado em uma disciplina. A aplicação deve atender aos seguintes requisitos:

A CLI deve perguntar ao usuário o seu nome. Caso a resposta do usuário seja um texto vazio, o programa deve ser encerrado;
Em seguida, o programa deve calcular a média do usuário. Para isso, o programa deve ler as notas de AP1, AP2, AS e AC. Em seguida, deve exibir na tela a média final do aluno. Considere que a média é calculada como (AP1 + AP2) * 0.4 + AC * 0.2, sendo que a AS pode substituir a AP1 ou a AP2 (a menor dentre as duas);
Por fim, a aplicação deve exibir na tela se o aluno foi aprovado ou reprovado, baseado na sua média. A média para aprovação é 7.0.
Organize o seu código em funções com responsabilidades distintas (uma para o cálculo de nota, uma para exibição de informações, uma para leitura de dados, etc.). Caso as notas passadas sejam inválidas (menores que 0 ou maiores que 10), o programa não deve calcular nada e deve ser encerrado.

"""

def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    ap1 = float(input("Insira a nota da AP1:"))
    ap2 = float(input("Insira a nota da AP2:"))
    asub = float(input("Insira a nota da AS:"))
    ac = float(input("Insira a nota da AC:"))
    return ap1,ap2,asub,ac
     

def analisar_subst(ap1, ap2, asub):
    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """
    if asub > ap1 :
        ap1 = asub
        return ap1,ap2
    elif asub > ap2:
        ap2 = asub
        return ap1,ap2
    return ap1,ap2

def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""
    return 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10 

    

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()

# TESTES:
# print(analisar_subst(0,7,6))
# print(calcular_media(7,7,7,7)) 
# print(aluno_foi_aprovado(6))
# print(notas_sao_validas(2,2,2,2))