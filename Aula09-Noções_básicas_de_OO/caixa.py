from funcionario import Funcionario

class Caixa(Funcionario): #herança: classe caixa herda os atributos da classe funcionario
    def __init__(self,nome,matricula,email) -> None:
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.horario = ""

    def definir_horarios(self, horario):
        self.horario = horario
        