from conta import Conta
from agencia import Agencia
from gerente import Gerente

ag1 = Agencia(1,"Barra","Zé")
ag2 = Agencia(2,"Recreio","Maria")
gerente = Gerente("Zé",1,"zé@banco.com",ag1)

c1 = Conta(ag1)
c2 = Conta(ag2)

print(c1) #Retorna o objeto e seu endereço de memória 
print(c2)

c1.depositar(50)
print(c1.ver_saldo()) #muda o slado de c1 pelo (self)
print(c2.ver_saldo()) # Pela POO nós devemos uar apenas meódos até para verificar valores ou exibir coisas 

c3 = Conta(ag2)
print(c3)

print(c2 == c3)

c2.depositar(10)
print(c2.ver_saldo())
print(c3.ver_saldo())
print(c2 == c3)