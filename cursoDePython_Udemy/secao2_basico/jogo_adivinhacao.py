#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
while True:
    import random
    palavra_secretas = [
        'brasil', 'padre', 'gruta', 'primo', 'predileto', 'protocolo',
        'trato', 'dragao', 'medrosos', 'madrugada', 'fraco', 'prova',
        'primavera', 'prego', 'trilha', 'refrigerante', 'bruxa', 'micro',
        'tristeza', 'novembro', 'fruta', 'trabalho', 'granito', 'frete',
        'edredon', 'depressa', 'trigo', 'prata', ' promocao', 'capricho',
        'imprimir', 'grito', 'grilo', 'negro', 'alegria', 'gravata'
    ]
    secreto = random.choice(palavra_secretas)
    digitadas = []
    chances = 5

    while True:
        if chances <= 0:
            print('PERDEUUU KKKKKK TENTA DENOVO HEHEHEHE!!!')
            break

        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Ahhh isso não vale, digite apenas uma letra.')
            continue

        digitadas.append(letra)

        if letra in secreto:
            print(
                f'Acertou miseravi, a letra "{letra}" existe na palavra secreta.')
        else:
            print(
                f'Errouuuu: a letra "{letra}" NÃO EXISTE na palavra secreta.')
            digitadas.pop()

        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

        if secreto_temporario == secreto:
            print(
                f'GANHOU AAAEEEWWW :D!!! A palavra era {secreto_temporario}.')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print(' ')
