l1 = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]

l2 = [variavel for variavel in l1]

ex2 = [v *2 for v in l1]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l3 = ['luiz', 'mauro', 'maria']

ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(x,y) for x,y in tupla]

l4 = list(range(100))

ex6 = [v for v in l3 if v % 3 == 0 if v % 8 ==0]

ex7 = [v if v % 3 == 0 else 'Não é' for v in l4]

print(l2)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex6)
print(ex7)

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i: i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)

d1 = {x: y.upper() for x, y in tupla}
print(d1)

