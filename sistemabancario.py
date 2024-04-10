conta = 00000-00
agencia = 0000

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

menu = f"""
### Agência: {agencia} ## Conta: {conta} #
#####  LIMITE POR SAQUE = R$ {limite}.00
#####  LIMITE DE SAQUE = {LIMITE_SAQUE}
### Para movimentar a sua conta selecione as opções Abaixo ###
##### MENU #####

#[1] Depositar #
#[2] Sacar #####
#[3] Extrato ###
#[0] Sair ######
"""


while True:

    opcao = input(menu)
        
    if opcao == '1':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Deposito: R$ {valor:.2f} REALIZADO COM SUCESSO ")
        
        else:
            print("Operação falhou! Valor informado invalido")
    
    elif opcao == '2':
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo Suficiente.")
        
        elif excedeu_limite:
            print( "Operação falhou! O Valor do saque excedo o limite.")

        elif excedeu_saques:
            print( "Operação falhou! Número maximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque: R$ {valor:.2f}, REALIZADO COM SUCESSO")
        
        else:
            print("Operação falhou! O Valor Informado é inválido")


    elif opcao == '3':
         print("\n################ EXTRATO ################ ")
         print("Não foram realizados movimentações." if not extrato else extrato)
         print(f"\n Saldo: R$ {saldo:.2f}")
         print("###########################################")

    elif opcao == '0':
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")

    