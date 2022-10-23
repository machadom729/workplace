
#  sep é como vai separar os argumentos invés do espaço padrão
#  end é como vai terminar a linha invés de quebrar a linha como padrão
print('824', '176', '070', sep='.', end='-')
print('18')


#  formatação de string

nome = 'Matheus Machado'
idade = 25
altura = 1.85
e_maior = idade >= 18
peso = 62
imc = peso / altura ** 2
print(nome, 'tem', idade, 'anos de idade e seu imcé', imc)
# fstring é para formatar da mesma forma que .format
print(f'{nome} tem {idade} anos de de idade e seu {imc:.2f}')  # ":.2f" para exibir duas casas decimais


#  desafio pratico

ano_atual = 2021
nascimento = ano_atual - idade
print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}')


# desafio dois
#1
num1 = input('insira um numero inteiro: ')
try:
    num2 = int(num1)
    if num2%2 == 0:
        print('este numero é par')
    else:
        print('este numero é impar')
except:
    print('este não é um numero inteiro')


#2
hora = input('digite as horas: ')
try:
    hora = int(hora)
    if 0 < hora <= 11:
        print('bom dia')
    elif 11 < hora <= 18:
        print('boa tardes')
    elif 18 < hora <= 23:
        print('boa noite')
    else:
        print('um dia so tem 24 horas')
except:
    print('isso nao e um numero')


name = input('Escreva seu nome: ')
if len(name) <= 4:
    print(f'{name} é curto')
elif 4 < len(name) < 7:
    print(f'{name} é normal')
elif len(name) > 6:
    print(f'{name} é muito grande')
else:
    print('digite um nome')
"""
Formatando valores com modificadores
:s - string
:d - int
:f - float
:.(nº)f - quantidade de casas decimais
:(caractere)(> or < or ^)(quantidade)(tipo s, d, f) - para adicionar caractere
> para add a esquerda
< para add a direita
^ para deixar no centro
"""
num1 = 123123.123123
nome = 'abcdefghijkmn'
print(f'{num1:.3f}')
print(f'{nome:#^10}')

#  fatiamento de string

print(nome[0:6])  # ler as letras 0 a 6
print(nome[-1])  # ler a ultima letra
print(nome[0::2])  # ler todas as letras mas pulando de 2 em 2
