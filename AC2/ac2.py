# Exercício 1: revisite a AC1
# Desenvolva duas funções em Python:
# eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes sempre reais;
# bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
def eq_seg_grau (a,b,c):
    delta = (b ** 2) -4 * a *c
    raiz_1 = (-b + (delta)**1/2)/(2*a)
    raiz_2 = (-b - (delta)**1/2)/(2*a)
    return(raiz_1,raiz_2)
print(eq_seg_grau(1,4,3))

def bissexto(ano):
    resto_por_4 = int(ano)%4
    resto_por_100 = int(ano)%100
    resto_por_400 = int(ano)%400
    divisivel_por_400= (resto_por_400 == 0)
    divisivel_por_4 = (resto_por_4 == 0)
    return(divisivel_por_400) or (resto_por_100 != 0 and divisivel_por_4)

print(bissexto(2000))


# Exercício 2: salário
# Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais, valor_hora e num_horas, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente. Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275. A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.
def calcula_salario(valor_hora,num_horas,irpf=0.275):
    salario_liquido = valor_hora * num_horas * (1.0 - float(irpf))
    return salario_liquido
print(calcula_salario(200,240))