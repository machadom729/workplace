while True:

    cpf = input('Digite seu cpf: ')
    qtdnum = len(cpf)
    x = 8
    y = 9
    z = 0
    mult1 = list(range(2, 12,))
    result = []
    result2 = []

    # estruturas para realizar as operações para definir
    # os dois ultimos digitos do novo_cpf

    while x >= 0 and z <= 8:
        r = int(cpf[z]) * int(mult1[x])
        result.append(r)
        x -= 1
        z += 1

    r1 = 11 - (sum(result) % 11)
    z = 0

    while y >= 0 and z <= 9:
        r = int(cpf[z]) * int(mult1[y])
        result2.append(r)
        y -= 1
        z += 1

    r2 = 11 - (sum(result2) % 11)

    # estrutura para definir os dois ultimos digitos do cpf

    if r1 > 9:
        d1 = '0'
    elif r1 <= 9:
        d1 = cpf[9]
    if r2 > 9:
        d2 = '0'
    elif r2 <= 9:
        d2 = cpf[10]

    # criando o novo cpf para comparar com o original e validar

    novo_cpf = cpf[0:9] + d1 + d2
    sequencia = novo_cpf == str(novo_cpf[0]) * qtdnum

    if cpf == novo_cpf:
        print('Este CPF é válido!!!')
    else:
        print('Este CPF não é válido')

        """
        calcula para formato do cpf
        CPF = 168.995.350-09
        ------------------------------------------------
        1 * 10 = 10           #    1 * 11 = 11 <-
        6 * 9  = 54           #    6 * 10 = 60
        8 * 8  = 64           #    8 *  9 = 72
        9 * 7  = 63           #    9 *  8 = 72
        9 * 6  = 54           #    9 *  7 = 63
        5 * 5  = 25           #    5 *  6 = 30
        3 * 4  = 12           #    3 *  5 = 15
        5 * 3  = 15           #    5 *  4 = 20
        0 * 2  = 0            #    0 *  3 = 0
                              # -> 0 *  2 = 0
                 297          #             343
        11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
        11 > 9 = 0            #
        Digito 1 = 0          #   Digito 2 = 9
        """
