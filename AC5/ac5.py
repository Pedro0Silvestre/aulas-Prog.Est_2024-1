"""
Programação Estruturada
2024.1
15/03/2024

AC5
"""
"""randint() função da biblioteca random que gera um numero aleatorio entre os parametros inseridos, break encerra loop"""

import random

# print(random.randint(2,8))

def main():
    #status aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10,20)
    defesa_aventureiro = random.randint(1,5)

    #status monstro
    vida_monstro = random.randint(60,80)
    ataque_monstro = random.randint(20,30)

    #exibir status iniciais
    print("Aventureiro: vida ",vida_aventureiro,"- att", ataque_aventureiro,"- def",defesa_aventureiro)
    print("Monstro: vida ",vida_monstro,"- att ",ataque_monstro)

    #loop das rodadas
    rodadas = 0
    while True :
        rodadas += 1
        print('RODADA: ',rodadas)
        
        #ataque aventureiro
        dano_causado_aventureiro = random.randint(1,ataque_aventureiro)
        #dano na vida do monstro
        vida_monstro = vida_monstro - dano_causado_aventureiro
        #verificar morte do monstro
        if vida_monstro <= 0:
            print("PARABÉNS - Monstro morreu")
            break
        #dano do monstro
        dano_causado_monstro = random.randint(1,ataque_monstro)
        #ver se passou a defesa
        if dano_causado_monstro > defesa_aventureiro:
            vida_aventureiro = vida_aventureiro - (dano_causado_monstro - defesa_aventureiro)
        #verificar morte do aventureiro
        if vida_aventureiro <= 0:
            print("GAME OVER - Aventureiro morreu")
            break
        #exibi atributos atuais
        print("Aventureiro: vida ",vida_aventureiro,"- att", ataque_aventureiro,"- def",defesa_aventureiro)
        print("Monstro: vida ",vida_monstro,"- att ",ataque_monstro)
            
main()


