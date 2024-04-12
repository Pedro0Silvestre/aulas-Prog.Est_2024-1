#exercicio even
# even = 0
# for i in range(5):
#     if int(input()) % 2 == 0:
#         even += 1

# print(even, 'valores pares')

"soma dos não divisiveis por 13"
# sum = 0
# x = int(input())
# y = int(input())
# temp = x

# if x > y:
#     x = y
#     y = temp


# for i in range(x,y+1):
#     if i % 13 != 0 :
#         sum += i

# print(sum)

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


    

    

