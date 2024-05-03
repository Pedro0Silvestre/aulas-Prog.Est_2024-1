import random

class Aventureiro:
    def __init__(self) -> None:
        self.vida = random.randint(100,120)
        self.forca = random.randint(10,18)
        self.defes = random.randint(10,18)
        self.posicao = [0,0]





    # Operações do aventureiro
    def andar(self, direcao):
        """
        Altera o valor da posição do aventureiro conforme a direção informada pelo
        usuário. Direções válidas:
        - W: cima
        - A: esquerda
        - S: baixo
        - D: direita

        Se o aventureiro estiver nos limites do mapa, não faz nenhum movimento.

        Considerar que o mapa é um sistema cartesiano, com o eixo x aumentando
        da esquerda para a direita, e o eixo y aumentando de cima para baixo.
        Portanto, as coordenadas (0, 0) estão no canto superior esquerdo do mapa,
        enquanto que as coordenadas (9, 9) estão no canto inferior direito.

        Retorna True caso o aventureiro tenha andado, e False caso contrário.
        """
        match direcao:
            case "W":
                if self.posicao[1] > 0:
                    self.posicao[1] -= 1
                    return True
            case "S":
                if self.posicao[1] < 9:
                    self.posicao[1] += 1
                    return True
            case "A":
                if self.posicao[0] > 0:
                    self.posicao[0] -= 1
                    return True
            case "D":
                if self.posicao[0] < 9:
                    self.posicao[0] += 1
                    return True

        return False

    def atacar(aventureiro):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return aventureiro["forca"] + random.randint(1, 6)

    def aventureiro_defender(aventureiro, dano):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        dano_levado = dano - aventureiro["defesa"]
        if dano_levado > 0:
            aventureiro["vida"] -= dano_levado

    def ver_atributos_aventureiro(aventureiro):
        """
        Exibe na tela os atributos do aventureiro (nome, vida, força, defesa).
        """
        print("Informações de ", aventureiro["nome"], ":", sep="")
        print("Vida:", aventureiro["vida"])
        print("Força:", aventureiro["forca"])
        print("Defesa:", aventureiro["defesa"])

    def aventureiro_esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0