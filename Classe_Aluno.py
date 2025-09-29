class Aluno:
    def __init__(self,nome,mensalidade,idade):
        self.nome = nome
        self.idade = idade
        self.mensalidade = mensalidade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Mensalidade: R$ {self.mensalidade}"

    def set_nome(self,novo_nome):
        self.nome = novo_nome

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_mensalidade(self):
        return self.mensalidade



    def main(valor):
        print(valor)

    def set_nome(self,novo_nome):
        self.nome = novo_nome


    def set_mensalidade(self,nova_mensalidade):
        self.mensalidade = nova_mensalidade

    def set_idade(self,nova_idade):
        self.idade = nova_idade




if __name__ == '__main__':
    objeto1 = Aluno("Dan",1000,20)

    print(f"Nome antigo = {objeto1.get_nome()}")
    objeto1.set_nome("Roberto")
    print(f"Novo nome = {objeto1.get_nome()}")
    objeto1.set_mensalidade(2000)
    print(f"A nova mensalidade é {objeto1.get_mensalidade()} ")
    objeto1.set_idade(30)
    print(f"A nova idade é {objeto1.get_idade()}")
