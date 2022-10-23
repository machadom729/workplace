
# loop infinito
while True:
    nome = 'Matheus'
    print(f'Olá {nome}')
    break
print('não será executada')

# contar até 100
x = 0
while x < 100:
    print(x)
    x = x + 1
print('Acabou')

# uso do 'continue' para pular uma condição e 'break' para parar sair do loop
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x += 1
print('Acabou')
x = 0
while x < 10:
    if x == 3:
        x += 1  # x = x + 1
        break
    print(x)
    x = x + 1
print('Acabou')

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

# laço for in
for n in range(10):
    print(n)
print('Acabou')
for n in range(0, 11, 3):  # conta até 10 pulando de 3 em 3
    print(n)
print('Acabou')

"""
Split, Join, Enumerate em python
*Split - dividir um string
*Join - Juntar uma lista
* - Enumerar elementos da lista
"""
lista = frase.split(' ')
print(lista)
for valor in lista:
    print(valor)
    print(f'A palavra "{valor}" apareceu {lista.count(valor)}x vezes.')

frase2 =  ' '.join(lista)
print(frase2)

for indice, valor in enumerate(lista):
    print(indice, valor)

# desempacotamento de lista
n1, n2 ,n3, *outra_lista, ultimo_valor = lista
print(n1, n2, n3, outra_lista, ultimo_valor)

# inversao de variavel
x = 25
y = 'Matheus'
z = 'Machado'
w = 'anos'
x, y, z, w = y, z, x, w
print(x, y, z, w)

# operador ternário

logged_user = False
msg = 'Usuário logado.' if (logged_user) else 'Usuário precisar logar.'
print(msg)

# desafio contadores
x = 0
y = 10
while x <= 10 and y >= 0:
    print(x, y)
    x += 1
    y -= 1

#soluçao do professor
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)