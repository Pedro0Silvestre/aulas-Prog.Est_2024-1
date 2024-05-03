from funcionario import Funcionario

class Gerente(Funcionario): #gernte herda a super classe funcionario
    """
    nome
    matrivula
    cpf
    email
    horário
    data_nascimenteo
    """

    def __init__(self,nome,matricula,email,horario) -> None:
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.horario = ""
    
    def definir_horario(self,horario):
        self.horario = horario

    def trocar_email(self,novo_email):
        self.email = novo_email
    
    def cadastrar_novo_cliente(self,nome,email):
        nova_conta = Conta(self.agencia)
        novo_cliente = Titular
        