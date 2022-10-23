

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, idade, conta):
        super().__init__(nome, sobrenome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta


class Banco:
    agencia = 2215

    def valida(self, cliente):
        if cliente.conta.agencia != self.agencia:
            print("Esta conta não pertence a este banco")

        cliente.conta.permissao = True
