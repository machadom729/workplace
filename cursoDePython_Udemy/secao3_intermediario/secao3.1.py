# #exercicio fizzbuzz
# def fizzbuzz(n1):
#     if n1 % 3 == 0 and n1 % 5 == 0:
#         return 'fizzbuzz'
#     if n1 % 3 == 0:
#         return 'fizz'
#     if n1 % 5 == 0:
#         return 'buzz'
#     return n1
#
# n1 = int(input('Insira um numero: '))
# print(fizzbuzz(n1))

# execicio 2
#
# def mestre(funcao, *args, **kwargs):
#     return funcao(*args, **kwargs)
#
#
# def fala_oi(nome):
#     return f'Oi {nome}'
#
#
# def saudacao(nome, saudacao):
#     return f'{saudacao} {nome}'
#
#
# executando = mestre(fala_oi, 'Luiz')
# executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
# print(executando)
# print(executando2)
#
# #funçao lambda
#
# a = lambda x, y: x * y
# print(a(2,2))
#
# lista = [
#     ['P1', 12],
#     ['P2', 142],
#     ['P3', 5]
# ]
# print(sorted(lista, key=lambda i: i[1]))

# tuplas ficando entra () são imutaveis e somente para leitura tem como concatenar com outra tupla para modifica-la
# temos que transforma-la em lista atraves do comando 'list' e para retorma para tupla 'tuple'
# tup = [1, 2, 3, 4]

#dicionario fica entre {} opde ser criado com o comando 'dict' consiste em uma chave e um valor


# #d1 = {1: 'valor1}

#sets
# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^(elementos que estão nos dois sets, mas não em ambos)
# s1 = set(), set.update ...
# set não aceita elemento duplicado e não respeita ordem
