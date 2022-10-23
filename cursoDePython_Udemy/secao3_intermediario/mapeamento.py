import functools
from dados import produtos, pessoas, lista

uso da funcao map
nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)
for preco in novos_produtos:
    print(preco)

for pessoa in pessoas:
    print(pessoa)

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)


def aumenta_idade(p):
    p['idade'] = round(p['idade'] * 1.25)
    return p


nomee = map(aumenta_idade, pessoas)
for idade in nomee:
    print(idade)

uso do filter
nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

print()

nova_lista = filter(lambda p: p['preco'] > 10, produtos)
for produto in nova_lista:
    print(produto)

print()

nova_lista = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista:
    print(produto)


# funcao reduce - acumuladora
# como ela funciona
acumula = 0
for item in lista:
    acumula += item

print(acumula)

soma_lista = functools.reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = functools.reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
