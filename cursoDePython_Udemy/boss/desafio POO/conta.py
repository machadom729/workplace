from abc import ABC, abstractmethod
import random as rd


class Conta(ABC):
    def __init__(self, agencia, saldo):
        self._agencia = agencia
        self._conta = rd.randint(100, 999)
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo deve ser numerico')

        self._saldo = valor

    def detalhes(self):
        print(f'Sua agência é {self.agencia} ')
        print(f'Sua conta é {self.conta} ')
        print(f'Seu saldo é {self.saldo}')
        print()

    @abstractmethod
    def saque(self, sacar): pass

    def depositar(self, deposito):
        if not isinstance(deposito, (int, float)):
            raise ValueError('Deposito deve ser numerico')

        self._saldo += deposito
        print(f'O valor depositado foi {deposito}')
        self.detalhes()


class ContaCorrente(Conta):
    permissao = False

    def __init__(self, agencia, saldo, limite):
        super().__init__(agencia, saldo)
        self._limite = limite

    @ property
    def limite(self):
        return self._limite

    def saque(self, sacar):
        if (self.saldo + self.limite) < sacar or not self.permissao:
            print('Saque inválido')
            return

        self.saldo -= sacar
        print(f'O valor saquado foi {sacar}')
        self.detalhes()


class ContaPoupanca(Conta):
    permissao = False

    def saque(self, sacar):
        if self.saldo < sacar or not self.permissao:
            print('Saque inválido')
            return

        self.saldo -= sacar
        print(f'O valor saquado foi {sacar}')
        self.detalhes()
