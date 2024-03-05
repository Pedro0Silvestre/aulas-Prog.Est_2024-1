# 1-Faça um procedimento soma que recebe dois números e retorne a soma deles.
def soma() :
    a = 2
    b = 3
    return a + b
print(soma())

# 2-Faça um procedimento média que recebe três notas e retorne a média aritmética simples.
def media(a,b,c):
    return (a+b+c)/3
print(media(2,3,7))

# 3-Faça um procedimento nota que recebe três notas, chame o procedimento média do exercício anterior e informe se o aluno está aprovado ou reprovado. Considere aprovado um aluno que tenha obtido média superior ou igual a 7.0.

def aprovado(a,b,c):
    return (media(a,b,c) >= 6)
print(aprovado(6,6,5))

# 4- Faça um procedimento pares que recebe um número maximo e exibe todos os números pares, de zero a maximo.

def pares (max):
    for i in range(0,max+2,2):
     print(i)
pares(12)

# 5- Faça um procedimento valida_nota que recebe uma nota e retorna VERDADEIRO se a nota for válida (maior ou igual a zero, e menor ou igual a 10), ou retorna FALSO caso contrário.

def valida_nota (nota):
   return nota>=0 and nota<=10
print(valida_nota(-1.0))

# 6- Faça um procedimento fibo que recebe um número n (assumindo inteiro e positivo) e exibe na tela o n-ésimo elemento na sequência de Fibonacci, que é formada pelos valores 1, 1, 2, 3, 5, 8, 13, 21, 34, … Ou seja, um valor na posição i é igual à soma dos valores nas posições i - 1 e i - 2. Considere que os dois primeiros elementos são iguais a 1.

def fibo(n):
   a = 0
   b = 1
   c = 0
   for i in range (0,n):
      c = a + b
      if i == n-1:
         print(c-a)
      a = b
      b = c
      
    
fibo(9), fibo(1) 




      
    
      


    
   








