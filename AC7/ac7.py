"exercicio even"
even = 0
for i in range(5):
    if int(input()) % 2 == 0:
        even += 1

print(even, 'valores pares')

"soma dos não divisiveis por 13"
sum = 0
x = int(input())
y = int(input())
temp = x

if x > y:
    x = y
    y = temp


for i in range(x,y+1):
    if i % 13 != 0 :
        sum += i
print(sum)

"""QUESTÃO SALARY RISE """
salario = float(input())
if salario <= 400.00:
    percentual = 0.15
    reajuste_ganho = salario*percentual
    novo_salario = salario + reajuste_ganho

elif salario <= 800.00:
    percentual = 0.12
    reajuste_ganho = salario*percentual
    novo_salario = salario + reajuste_ganho

elif salario <= 1200.00:
    percentual = 0.10
    reajuste_ganho = salario*percentual
    novo_salario = salario + reajuste_ganho

elif salario <= 2000.00:
    percentual = 0.07
    reajuste_ganho = salario*percentual
    novo_salario = salario + reajuste_ganho

else:
    percentual = 0.04
    reajuste_ganho = salario*percentual
    novo_salario = salario + reajuste_ganho

print("Novo salario: %.2f" %novo_salario)
print("Reajuste ganho: %.2f"%reajuste_ganho)
print("Em percentual:",int(percentual*100),"%")

"""array fill"""

v = int(input())
n = []
if v < 50:
    n.append(v)
    for i in range(0,10):
        v = 2*v
        n.append(v)
        print(f"N[{i}] = {n[i]}")

"LOWEST NUMBER AND POSITION"

n = int(input())
if 1 < n and n < 1000:
    menor_valor = 1000
    x = input().split(" ")
    for i in range(n):
            if int(x[i]) < menor_valor:
                menor_valor = int(x[i])
                index = i
    print(f"Menor valor: {menor_valor}")
    print(f"Posicao: {index}")

"SORT BY LENGTH"
temp = ""
a = input().split()
for palavra in a:
    if len(palavra) > len(temp):
        temp = palavra
        
        print(temp)
print(a)

"COLUMN IN ARRAY"
c = int(input())
if c >= 0 and c <= 11:
    soma = 0
    t = input()
    if t == "S":
        for x in range(0,12):
            for y in range(0,12):
                num = float(input())
                if y == c:
                    soma += num
        print(round(soma),1) 
    else:
        for x in range(0,12):
            for y in range(0,12):
                num = float((input()))
                if y == c:
                    soma += num
        print(round(soma/12,1))

"SORT BY LENGTH"
frases = []
n = int(input())
for i in range(n):
    frases.append(input())
for frase in frases:
    palavras = frase.split()
    palavras_ordenadas = [] 
    if len(palavras) >= 1 and len(palavras) <= 50:
        for palavra in palavras:
            if len(palavra) >=1 and len(palavra) <= 50:
                palavras_ordenadas.append(len(palavra))
        palavras_ordenadas.sort(reverse=True)
        for i in range(0,len(palavras)):
            for palavra in palavras:
                if palavras_ordenadas[i] == len(palavra):
                    palavras_ordenadas[i] = palavra
                    palavras.remove(palavra)
        print(" ".join(palavras_ordenadas))

    

    

