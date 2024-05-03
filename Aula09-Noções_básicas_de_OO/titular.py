from pessoa import Pessoa

class Titular(Pessoa):
    """
    nome
    cpf
    endereço
    email
    telefone
    conta
    """

    def __init__(self,nome,email,conta) -> None:
        self.nome = nome
        self.email = email
        self.conta = conta

    def trocar_email(self,novo_email):
        self.email = novo_email