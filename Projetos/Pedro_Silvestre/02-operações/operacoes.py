"""
Programação Estruturada
2024.1
01/03/2024

Operações em python
- Aritimèticas
- Atribuição
- Comparação (ou relacionais)
- Lógicas ( ou booleanas)

"""

# Operações Aritiméticas

# Dois operandos numèricos
x = 10
y = 5

print(x + y) # Soma
print(x - y) # Subtração
print(x * y) # Multiplicação
print(x / y) # Divisão
print(x ** y) # Potência
print(x // y) # Divisão inteira (retorna sempre o quociente, resultado inteiro)
              #em caso de uma divisão inteira com um negativo (ex: -7 // 3) o inteiro mais anterior será resultado
              # -7 // 3 = -2.166... (arrendondando pra BAIXO)= -3
print(x % y) # Módulo (resto de uma divisão)

# round(valor, num_digitos)
print(round(x - y,2)) #Função round arredonda um valor até os digitos determinados nesse exemplo 2

# Um operando é uma string
print("-" + "-") # concatenação de strings
print("-" * 30) # multiplicação de strings (repete a string x vezes)

# Operações de atribuição
x = 10 #atribuição simples
x += 2 # x  = x + 2
x -= 3 # x = x - 3

#Menos comuns
x *= 5 # x = x * 5
x /= 4
x **= 2
x //= 6
x %= 2
print(x)
print(y)

# Operadores de comparação
# Resulta num valor booleano (true ou False)
print(x >y) # maior que
print(x >= y) # maior ou igual a
print(x < y) # menor que
print(x <= y) #menor ou igual a
print(x == y) # Igual a
print(x != y) #diferente de

#Comparação entre strings - Tabela ASCII
#Na comparação de strings o python leva em cosideração o numero do caracter na tabela ASCII então letras minusculas
#são maiores que maiusculas NÃO COMPARE LETRAS MINUSCULAS COM MAIUSCULAS SEMPRE DE IGUAL PRA IGUAÇ
x = "abc"
y = "Abc"
print(x >y) # maior que
print(x >= y) # maior ou igual a
print(x < y) # menor que
print(x <= y) #menor ou igual a
print(x == y) # Igual a
print(x != y) #diferente de

#Operadores lógicos
print("-" * 30)

x = True
y = False
print(x and y) # E ( retorna verdadeiro se ambos forem verdadeiros)
print(x or y) # OU (retorna verdadeiro se pelo menos um dos valores for verdadeiro)
print(not x) # NÃO (inverte valor lógico)

# Type casting (muda o tipo de dado)
x = 9
print(float(x)) #converte x num dado de ponto flutuante
print(int("10"))

# Em python, todo valor diferente de "",0,0.0, é True
print(bool(x))
print(bool(0))

print("abc" and 16)
# o operador and como pelo menos um tem de ser verdadeiro para dar true ele retorna o segundo valor caso primeiro verdadeiro
print(0 and 16)
print(False and 16)
print("" and 16)
#ESTUDE DNV A DIFERENÇA DO AND E DO OR 
print("abc" or 16)
print(10.5 or 16)
print(True or 16)
print("" or 16)
# no or Se o primeiro valor for falso ele retorna o valor do segundo

# Isso sobe uma exceção se o primeiro operando for False
print(6 or int("a"))

# Pythonico (algo q só funciona no python)


"""
Precedência

()
**
* / // %
+ -
> >= < <= == !=
not
and
or
"""

#Divisão é uma operação que sempre retorna valor flutuante(float)
#SELECINAR E BOTAR PARENTESES BOTA PARENTESES EM TUDO
print (6 + 3 * 2 <= 15 - 2.5 // 4 % 3 and 10/2 or not 15 + 2 ** 2 < 2)
# TRUE tem valor númerico de 1 e o FALSE valor númerico de 0




