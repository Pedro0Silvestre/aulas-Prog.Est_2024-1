"""
Programação estruturada
2024.1
01/03/2024

EXERCÍCIOS
"""

"""
Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre a média.
A média é calculada de acordo com a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
# def media ():
#     ap1= float(input("Insira o valor da nota AP1:"))
#     ap2= float(input("Insira o valor da nota AP2:"))
#     ac= float(input("Insira o valor da nota AC:"))
#     print("A média é", (ap1 + ap2) * 0.4 + ac * 0.2)

"""
Faça um programa que receba as três notas da disciplina (AP1, AP2 e AC) e retorne a média.
A média é calculada de acordo com a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""

def media_escolar(ap1,ap2,ac):
    return ((ap1 + ap2) * 0.4 + ac * 0.2)

#MAIN = Função criada para testar valores e outras funções

def main():
    print(media_escolar(7,8,9.2))
    print(media_escolar(7.7,6.5,7.3))

main()

