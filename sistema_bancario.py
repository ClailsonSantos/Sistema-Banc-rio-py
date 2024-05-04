# DESAFIO #
 ### 1-  Para a primeira versão do sistema devemos implementar apenas 3 operações:
 ### 1.1- depósito: Deve ser possível depositar valores positivos para a minha conta bancária. Todos os depósitos devem ser e exibidos na operação de extrato. 

### 2- saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser e exibidos na operação de extrato.

### 3- extrato: Essa operação deve listar todos depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx."""

menu = """
-=-=-=-=-=-= SEJA BEM VINDO AO SISTEMA BANCÁRIO D.I.O =-=-=-=-=-=-
              Insira a operação que deseja realizar!
    [D] - DEPÓSITO
    [S] - SAQUE
    [E] - EXTRATO
    [Q] - SAIR
=>"""
deposito = 0
saldo = 0
limite_por_saque = 500
numero_saque = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    opcao = input(menu).upper()
    if opcao == "D":
        valor_deposito = float(input("Insira o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito}.\n"
            deposito += 1
            print("-=-=-=-=-=-=-=-=-=-= DEPÓSITO =-=-=-=-=-=-=-=-=-=-")
            print(f"\nDeposito de R$ {valor_deposito} Realizado com Sucesso!")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    elif opcao == "S":
        valor_saque = float(input("Insira o valor que deseja Sacar: "))
        if valor_saque > 0:
            if valor_saque <= saldo:
                if numero_saque < LIMITE_SAQUE:
                    if valor_saque <= limite_por_saque:
                        saldo -= valor_saque
                        extrato += f"Saque: R$ {valor_saque}.\n"
                        numero_saque += 1
                        print("-=-=-=-=-=-=-=-=-=-= SAQUE =-=-=-=-=-=-=-=-=-=-")
                        print(f"\nSaque de R$ {valor_saque} Realizado com Sucesso!")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    else:
                        print("O valor limite por saque foi excedido!")
                else:
                    print("Você excedeu a quantidade de saque por dia!")
            else:
                print("Não há saldo suficiente!")
        else:
            print("Valor inserido inválido!")
    elif opcao == "E":
        print("-=-=-=-=-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-=-=-=-=-")
        print(extrato)
        print(f"Saldo atual {saldo:.2f}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    elif opcao == "Q":
        print(
            "Encerrando o sistema",
            end="..." "\nAgradecemos por utilizar nossos serviços!",
        )
        break
    else:
        print("Opção inválida!\n Por favor escolha novamente a opção desejada.")
