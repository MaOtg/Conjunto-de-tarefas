# Hora do Show
def mehn(opcao):
    """
    Código em formato de menu, para saber diversas coisas...
    """
    print('-=>' * 24)

    if opcao == 1:
        nnotas = int(input(f'Ok {nome}! Quantas notas irão compor a média? '))
        notas = float(input('\n''Digite uma nota: ')),
        while len(notas) <= nnotas - 1:
            notas += float(input('Digite a outra nota: ')),
        print('-=' * 25)
        notas = sum(notas) / nnotas
        notas = '%.2f' % notas
        print(f'{nome}, a média das suas notas é {notas}')
        print('-=' * 25)
        # Cálculo da média

    elif opcao == 2:
        a = 0
        b = 10
        escolha = int(input(f'Ok {nome}! Escolha um número para saber a tabuada: '))
        print('-=>' * 24)
        while a <= b:
            result = escolha * a
            print(f'{escolha} x {a} = {result}')
            a += 1
        print('-=' * 15)
        # Tabuada

    elif opcao == 3:
        def equacao(a, b, c):
            '''
            Código que realiza equações do Primeiro grau
            '''
            x = ((c - b) / a)
            print('-=' * 11)
            print(f'O valor de X é igual a {x}')
            return ((a * x) + b) == c

        print(f'Ok {nome}! para a equação de 1° grau no modelo (ax + b = c) Digite...')
        equacao(float(input('O valor de a: ')),
                float(input('O valor de b: ')),
                float(input('O resultado c: ')))
        print('-=' * 11)
        # Equacao1°grau

    elif opcao == 4:
        def equa2(a, b, c):
            '''
            Código que realiza equações do Segundo grau
            '''
            raiz = ((b * b) - (4 * a * c)) ** 0.5
            x1 = ((b * -1) + raiz) / (2 * a)
            x2 = ((b * -1) - raiz) / (2 * a)
            print('-=' * 15)
            if ((a * (x1 * x1)) + (b * x1) + (c)) == 0:
                print(f'O valor de X1 é igual a {x1}')
            if ((a * (x2 * x2)) + (b * x2) + (c)) == 0:
                print(f'O valor de X2 é igual a {x2}')
            return

        print(f'Ok {nome}! Para saber o valor das raízes:')
        equa2(float(input('Insira o valor de a: ')),
              float(input('Insira o valor de b: ')),
              float(input('Insira o valor de c: ')))
        print('-=' * 15)
        # Equacao2°grau

    elif opcao == 5:
        def r3(a, b, x):
            '''
            Código para fazer regra de 3 só inserindo os valores
            '''
            y = (x * b) / a
            print('-=' * 15)
            print(f'O valor de Y é igual a {y}')
            return (a * b) == (x * y)

        print(f'Ok {nome}! Para realizarmos a regra de 3:')
        print('Modelo a/b = x/y')
        print('-=' * 3)
        r3(float(input('Digite o valor de a: ')),
           float(input('Digite o valor de b: ')),
           float(input('Digite o valor de x: ')))
        print('-=' * 15)
        # Regrade3

    elif opcao == 6:
        def percent(a, b):
            '''
            Código para calcular qualquer porcentagem de um número
            '''
            b1 = b / 100
            c = b1 * a
            print('-=' * 10)
            print(f'{b}% de {a} é igual a {c}')
            return

        print(f'Ok {nome}! Para saber a % do número digite:')
        percent(float(input('Número: ')),
                float(input('Porcentagem escolhida (sem o %): ')))
        print('-=' * 10)
        # Percentagem

    elif opcao == 7:
        def capit(c, i, t):
            '''
            Código para se calcular o montante de um capital aplicado a juros compostos
            '''
            i = i / 100
            m = c * ((1 + i) ** t)
            r = m - c
            m = '%.2f' % m
            r = '%.2f' % r
            print('-=' * 15)
            print(f'O valor total do montante será de {m} R$')
            print(f'Houve um rendimento de {r} R$')
            return

        print(f'Ok {nome}! Para calcular o montante gerado a partir de um único depósito, digite as informações pedidas:')
        capit(float(input('\n''Valor do capital inicial (sem o cifrão): ')),
              float(input('Taxa de juros mensal  (sem o símbolo %): ')),
              float(input('Tempo em meses aplicado: ')))
        print('-=' * 15)
        # Juroscompostos-montante

    elif opcao == 8:
        def pit(b, c):
            '''
            Código para calcular pitágoras
            '''
            a = float(((b ** 2) + (c ** 2)) ** 0.5)
            print('-=' * 15)
            print(f'O valor da hipotenusa é igual a {a}')
            return (b ** 2) + (c ** 2) == a

        print(f'Ok {nome}! Para descobrir a hipotenusa:')
        pit(float(input('Coloque o valor do cateto oposto: ')),
            float(input('COloque o valor do cateto adjacente: ')))
        print('-=' * 15)
        # Pitágoras

    elif opcao == 9:
        def l(x):
            '''
            Código com operações de logaritmo
            '''
            import math
            print('-=' * 15)
            if x == 1:
                print('-=' * 16)
                escolha = int(input('A soma será entre quantos Log?: '))
                print('-=' * 16)
                print('A seguir insira as informações:')
                print('\n'' Digite as info do Log')
                logs = math.log(float(input('   Log de: ')),
                                float(input('   Na base: '))),
                while len(logs) <= escolha - 1:
                    print('\n'' Info do outro Log')
                    logs += math.log(float(input('   Log de: ')),
                                     float(input('   Na base: '))),
                print('-=' * 14)
                print(f'O resultado da soma é = {sum(logs)}')
            elif x == 2:
                print('-=' * 19)
                esc = int(input('A subtração será entre quantos log?: '))
                print('-=' * 19)
                print('A seguir insira as informações:')
                print('\n'' Digite as info do Log')
                logs = math.log(float(input('  Log de: ')),
                                float(input('  Na base: '))),
                while len(logs) <= esc - 1:
                    print('\n'' Info do outro Log')
                    logs += (logs[-1]) - math.log(float(input('  Log de: ')),
                                                  float(input('  Na base: '))),
                print('-=' * 14)
                print(f'O resultado da subtração é {logs[len(logs) - 1]}')
            elif x == 3:
                print('-=' * 16)
                escol = int(input('Quantos log irão se dividir?: '))
                print('-=' * 16)
                print('A seguir insira as informações:''\n''Obs. Atenção na ordem!')
                print('\n'' Digite as info do Log')
                logs = math.log(float(input('  Log de: ')),
                                float(input('  Na base: '))),
                while len(logs) <= escol - 1:
                    print('\n'' Info do outro Log')
                    logs += (logs[-1]) / math.log(float(input('  Log de: ')),
                                                  float(input('  Na base: '))),
                print('-=' * 14)
                print(f'O resultado da divisão é = {logs[len(logs) - 1]}')
            elif x == 4:
                print('-=' * 16)
                numero = int(input('Quantos Log irão se multiplicar?: '))
                print('-=' * 16)
                print('A seguir insira as informações:')
                print('\n'' Digite as info do Log')
                logs = math.log(float(input('   Log de: ')),
                                float(input('   Na base: '))),
                while len(logs) <= numero - 1:
                    print('\n'' Info do outro Log')
                    logs += logs[-1] * math.log(float(input('   Log de: ')),
                                                float(input('   Na base: '))),
                print('-=' * 14)
                print(f'O resultado da multiplicação é = {logs[len(logs) - 1]}')

            cont = input(f'{nome}, você gostaria de realizar mais alguma operação?''\n'
                         's/n: ')
            if cont == 'n':
                print('\n''   Ok! finalizamos as operações com log.')
                print('-=' * 15)
            elif cont == 's':
                print('-=' * 15)
                l(int(input(f'Ok {nome}! Escolha qual outra operação irá querer realizar: ''\n'
                            '   Soma de logaritmo ... (1)''\n'
                            '   Subtração de log. ... (2)''\n'
                            '   Divisão de log. ..... (3)''\n'
                            '   Multiplicação de log. (4)''\n'
                            'Sua opção é: ')))
            print('-=' * 15)
            return

        l(int(input(f'Ok {nome}! Escolha qual operação irá querer realizar: ''\n'
                    '   Soma de logaritmo ... (1)''\n'
                    '   Subtração de log. ... (2)''\n'
                    '   Divisão de log. ..... (3)''\n'
                    '   Multiplicação de log. (4)''\n'
                    'Sua opção é: ')))
        print('-=' * 15)
        # Logaritmo

    elif opcao == 10:
        def val(x, i, t):
            """
            Colocando um valor mensal todos os meses, mais a taxa de rendimento
            """
            i = i/100
            n = x + x * i,
            while len(n) <= t - 1:
                n += n[-1] + float(x + (x + n[-1]) * i),
            print('-='*15)
            f = n[len(n)-1]
            f = '%.2f' % f
            print(f'{nome}, o valor total disponível será {f} R$')
            return

        print(f'Ok {nome}! Digite as informações pedidas:''\n'
              'Obs. O calculo será feito somando os valores a cada mês, mais a taxa de rendimento''\n')
        val(float(input('Valor do capital que será depositado mensalmente: ')),
            float(input('Taxa de rendimento (sem vírgula e sem o %): ')),
            float(input('Quantidade de vezes que depositará: ')))
        print('-='*15)
        # Depositando mensalmente a uma taxa

    def cont_2(cont_2):
        """
        Finalizar ou Continuar?
        """
        if cont_2 == 'n':
            print('\n''   (: Acabamos por aqui! :)')
        elif cont_2 == 's':
            print('-=>' * 24)
            mehn(int(input(f'{nome}, o que mais gostaria de saber hj?''\n'
                           '  (1) Média................. (1)''\n'
                           '  (2) Tabuada............... (2)''\n'
                           '  (3) Equação de 1° grau.... (3)''\n'
                           '  (4) Equação de 2° grau.... (4)''\n'
                           '  (5) Regra de 3............ (5)''\n'
                           '  (6) Porcentagem........... (6)''\n'
                           '  (7) Montante - juros comp. (7)''\n'
                           '  (8) Pitágoras - hipotenusa (8)''\n'
                           '  (9) Operações com log..... (9)''\n'
                           ' (10) Depósito mensal....... (10)''\n'
                           'Sua opção é: ')))
        else:
            while cont_2 != ('s') or ('n'):
                print('Error! Nenhuma opção reconhecida. ')
                cont_2 = input('Digite apenas (s) para sim ou (n) para não: ')
                if cont_2 == 'n':
                    print('\n''   (: Acabamos por aqui! :)')
                    break
                elif cont_2 == 's':
                    print('-=>' * 24)
                    mehn(int(input(f'{nome}, o que mais gostaria de saber hj?''\n'
                                   '  (1) Média................. (1)''\n'
                                   '  (2) Tabuada............... (2)''\n'
                                   '  (3) Equação de 1° grau.... (3)''\n'
                                   '  (4) Equação de 2° grau.... (4)''\n'
                                   '  (5) Regra de 3............ (5)''\n'
                                   '  (6) Porcentagem........... (6)''\n'
                                   '  (7) Montante - juros comp. (7)''\n'
                                   '  (8) Pitágoras - hipotenusa (8)''\n'
                                   '  (9) Operações com log..... (9)''\n'
                                   ' (10) Depósito mensal....... (10)''\n'
                                   'Sua opção é: ')))
                    break
        return

    continuar = input('Vc gostaria de saber mais algo? s/n: ''\n')
    if continuar == 'n':
        print('\n''   (: Acabamos por aqui! :)')
    elif continuar == 's':
        print('-=>' * 24)
        mehn(int(input(f'{nome}, o que mais gostaria de saber hj?''\n'
                       '  (1) Média................. (1)''\n'
                       '  (2) Tabuada............... (2)''\n'
                       '  (3) Equação de 1° grau.... (3)''\n'
                       '  (4) Equação de 2° grau.... (4)''\n'
                       '  (5) Regra de 3............ (5)''\n'
                       '  (6) Porcentagem........... (6)''\n'
                       '  (7) Montante - juros comp. (7)''\n'
                       '  (8) Pitágoras - hipotenusa (8)''\n'
                       '  (9) Operações com log..... (9)''\n'
                       ' (10) Depósito mensal....... (10)''\n'
                       'Sua opção é: ')))
    else:
        cont_2(input('Ops! digite apenas (s) para sim ou (n) para não: ''\n'))

    return  # def mehn(opcao) #função inicial

print('-=>')
nome = input('Olá, Sr/Srta... ')
print('-=>' * 24)
mehn(int(input(f'{nome}, o que gostaria de saber hj?''\n'
               '  (1) Média................. (1)''\n'
               '  (2) Tabuada............... (2)''\n'
               '  (3) Equação de 1° grau.... (3)''\n'
               '  (4) Equação de 2° grau.... (4)''\n'
               '  (5) Regra de 3............ (5)''\n'
               '  (6) Porcentagem........... (6)''\n'
               '  (7) Montante - juros comp. (7)''\n'
               '  (8) Pitágoras - hipotenusa (8)''\n'
               '  (9) Operações com log..... (9)''\n'
               ' (10) Depósito mensal....... (10)''\n'
               'Sua opção é: ')))
# fim do show
