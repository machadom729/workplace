import conta as c
import pessoa as p


banco = p.Banco()
conta1 = c.ContaCorrente(agencia=2215, saldo=1000, limite=500)
cliente1 = p.Cliente(nome='Matheus', sobrenome='Machado',
                     idade=25, conta=conta1)
banco.valida(cliente1)
conta1.saque(sacar=1250)
conta1.depositar(deposito=2909)

banco2 = p.Banco()
conta2 = c.ContaPoupanca(agencia=2215, saldo=160)
cliente2 = p.Cliente(nome='Maria', sobrenome='Barreto',
                     idade=65, conta=conta2)
banco2.valida(cliente2)
conta2.saque(sacar=145)
conta2.depositar(deposito=290)
