import re
import random


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def first_digit(cnpj):
    contador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj1 = []
    for n in cnpj[:12]:
        cnpj1.append(int(n))
    res = sum([x*y for x, y in zip(contador, cnpj1)])
    digit1 = 11 - (res % 11)
    if digit1 > 9:
        return 0
    else:
        return digit1


def second_digit(cnpj):
    contador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj1 = []
    for n in cnpj[:13]:
        cnpj1.append(int(n))
    res = sum([x*y for x, y in zip(contador, cnpj1)])
    digit1 = 11 - (res % 11)
    if digit1 > 9:
        return 0
    else:
        return digit1


def valida(cnpj):
    ncnpj = remover_caracteres(cnpj)
    d1 = first_digit(ncnpj)
    d2 = second_digit(ncnpj)

    novo_cnpj = ncnpj[:12] + str(d1) + str(d2)

    if novo_cnpj == ncnpj:
        print('Este CNPJ é válido. UHUUU')
    else:
        print('Este CNPJ não é válido. ERROUUUU')


def gera():
    f_block = random.randint(10, 99)
    s_block = random.randint(100, 999)
    t_block = random.randint(100, 999)

    inicio_cnpj = f'{f_block}{s_block}{t_block}0001'

    d1 = first_digit(inicio_cnpj)
    d2 = second_digit(inicio_cnpj + str(d1))

    return f'{f_block}.{s_block}.{t_block}/0001-{d1}{d2}'

# comando = input('Você quer gerar ou validar? ')

# if comando.lower() == 'validar':
#     func.valida(input('Digite o seu CNPJ: '))

# if comando.lower() == 'gerar':
#     gerado = func.gera()
#     print(gerado)
