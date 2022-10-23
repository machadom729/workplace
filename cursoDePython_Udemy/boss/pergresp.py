print()

# texto explicativo

print('Este é um jogo de perguntas e respostas.\n'
      'A cada perguntas responda a questão entre alternativas "a", "b", "c", "d" e "e"\n'
      'Te desejo boa sorte :D')

# dicionario dentro de dicionario contendo as perguntas e respostas e alternativa correct

perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue? ',
        'respostas': {
            'a': 'Tem entre 2 a 4 litros. São retirados 450 mililitros',
            'b': 'Tem entre 4 a 6 litros. São retirados 450 mililitros',
            'c': 'Tem 10 litros. São retirados 2 litros',
            'd': 'Tem 7 litros. São retirados 1,5 litros',
            'e': 'Tem 0,5 litros. São retirados 0,5 litros',

        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'Pergunta': 'De quem é a famosa frase “Penso, logo existo”? ',
        'respostas': {
            'a': 'Platão',
            'b': 'Galileu Galilei',
            'c': 'Descartes',
            'd': 'Sócrates',
            'e': 'Francis Bacon',

        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'Pergunta': 'De onde é a invenção do chuveiro elétrico? ',
        'respostas': {
            'a': 'França',
            'b': 'Inglaterra',
            'c': 'Brasil',
            'd': 'Austrália',
            'e': 'Itália',

        },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'Pergunta': 'Quais o menor e o maior país do mundo?  ',
        'respostas': {
            'a': 'Vaticano e Rússia',
            'b': 'Nauru e China',
            'c': 'Mônaco e canadá',
            'd': 'Malta e Estados Unidos',
            'e': 'São marino e India',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'Pergunta': 'Qual o nome do presidente do Brasil que ficou conhecido com Jango?  ',
        'respostas': {
            'a': 'Jânio Quadros',
            'b': 'Jacinto Anjos',
            'c': 'Getúlio Vargas',
            'd': 'João Figueiredo',
            'e': 'João Goulart',
        },
        'resposta_certa': 'e',
    },
    'Pergunta 6': {
        'Pergunta': 'Qual o grupo em que todas as palavras foram escritas corretamente?  ',
        'respostas': {
            'a': 'Asterístico, beneficiente, meteorologia, entertido',
            'b': 'Asterisco, beneficente, meteorologia, entretido',
            'c': 'Asterisco, beneficente, metereologia, entretido',
            'd': 'Asterístico, beneficiente, metereologia, entretido',
            'e': 'Asterisco, beneficiente, metereologia, entretido',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 7': {
        'Pergunta': 'Qual o livro mais vendido no mundo a seguir à Bíblia?  ',
        'respostas': {
            'a': 'O Senhor dos Anéis',
            'b': 'Dom Quixote',
            'c': 'O Pequeno Príncipe',
            'd': 'Ela, a Feiticeira',
            'e': 'Um Conto de Duas Cidades',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 8': {
        'Pergunta': 'Quais os países que têm a maior e a menor expectativa de vida do mundo?  ',
        'respostas': {
            'a': 'Japão e Serra Leoa',
            'b': 'Austrália e Afeganistão',
            'c': 'Itália e Chade',
            'd': 'Brasil e Congo',
            'e': 'Estados Unidos e Angola',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 9': {
        'Pergunta': 'Quantas casas decimais tem o número pi?  ',
        'respostas': {
            'a': 'Duas',
            'b': 'Centenas',
            'c': 'Infinitas',
            'd': 'Vinte',
            'e': 'Milhares',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 10': {
        'Pergunta': 'Atualmente, quantos elementos químicos a tabela periódica possui?  ',
        'respostas': {
            'a': '113',
            'b': '109',
            'c': '108',
            'd': '118',
            'e': '92',
        },
        'resposta_certa': 'd',
    },
}

print()

# variavel para contar as respostas certas

respostas_certas = 0

# laço de repetição para percorrer todo o dicionario

for pk, pv in perguntas.items():

    print(f'{pk}: {pv["Pergunta"]}')   #percorre as perguntas e as imprimi

    print('Resposta: ')
    print()

    # percorre as alternativa e imprimi depois da pergunta

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    # pede a resposta do usúario

    resposta_usuario = input('Sua resposta é: ')

    # verifica se a resposta esta certa ou errada e imprimi uma mensagem correspondente

    if resposta_usuario == pv['resposta_certa']:
        print('Acertou miseravii!!')
        respostas_certas += 1
    else:
        print('Errouuu!!!')

    print()

# variaveis para realizar o calculo da porcetagem

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

#imprimi na tela depois que todas as questoes estao respondidas quantas foram acertadas e a porcentagem

print(f'Você acerto {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
