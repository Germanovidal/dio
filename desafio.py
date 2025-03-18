menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor a Despositar: '))
        
        if valor > 0:
            print(f'Você depositou R$ {valor:.2f}')
            saldo += valor
            extrato += f'\nDepósito: R$ {valor:.2f}\n'
            
        
        else:
            print('Operação falhou! O valor informado é invalido!')

    elif opcao == 's':
        valor = float(input('Digite o valor a Sacar: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite por transação.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de transações excedido.')

        elif valor > 0:
            print(f'Você sacou R$ {valor:.2f}')
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}'
            numero_de_saques += 1
        
        else:
            print('Operação falhou! O valor informado é invalido')
    
    elif opcao == 'e':
        print('\n========== EXTRATO ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================')
    
    elif opcao == 'q':
        break

    else:
        print('Opção inválida, por favor selecione novamente a opção desejada.')