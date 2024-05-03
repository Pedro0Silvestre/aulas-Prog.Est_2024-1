# CamelCase
class Conta:
    """
    saldo
    numero
    agencia
    """
    #Método construtor
    def __init__(self,numero, agencia):
        self.agencia = agencia
        self.numero = self.agencia.abrir_conta()
        self.saldo = 0

    def depositar(self,valor):
        self.saldo += valor

    def ver_saldo(self):
        return self.saldo

    # sobrescrita ( sobrescrever métodos já usados)
    def __str__(self):
        return f"Conta {self.conta}, {self.agencia} - saldo R$ {self.saldo:.2f}"
    #comparação entre objetos
    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.agencia == __value.agencia and self.numero == __value.numero #comparação de agencia e numero    


        