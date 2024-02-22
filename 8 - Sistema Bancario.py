# Desafio: Criando um Sistema Bancário

# Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar
# suas operações e para isto escolheu a linguagem Python. Para a primeira versão do sistema devemos 
# implementar apenas 3 operações: Depósito, Saque e Extrato.

#Inicializando Variaveis
saldo = 0
depositos = []
saques = []
valorDepositado = 0
countDeposito = 0
countSaque = 0
countExtrato = 0
valorSaque = 0
limiteSaque = 500
limiteQtdSaque = 3
menu = True
menuInicial = """Digite a opção desejada:
[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - SAIR
R:"""

print(" Bem vindo a M10 Bank ".center(60,'#'))

while menu == True:
    # Menu Inicial
    opcao = input(menuInicial)

    #Funções
    if opcao.upper() == "D":
        print(" Função: DEPÓSITO ".center(60,'#'))
        valorDepositado = float(input("Digite o valor a ser depositado: "))
        countDeposito += 1
        saldo += valorDepositado
        depositos.append(valorDepositado)
        print(f' Depósito no valor de R${valorDepositado: .2f} realizado com sucesso! '.center(60,'#'))
        #input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))
    elif opcao.upper() == "S":
        print(" Funcão: SAQUE ".center(60,'#'))
        if countSaque < limiteQtdSaque:
            valorSaque = float(input("Digite o valor a ser sacado: "))
            if valorSaque > 0 or valorSaque <= limiteSaque:
                if valorSaque > saldo:
                    print(" Valor não permitido, saldo insuficiente! ".center(60,'#'))
                else:
                    countSaque += 1
                    saldo -= valorSaque
                    saques.append(valorSaque)
                    print(f' Saque no valor de R${valorSaque: .2f} realizado com sucesso!'.center(60,'#'))
            else:
                print(" Valor de saque não permitido! ".center(60,'#'))
                input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))
        else:
            print(" Limite de saque diário excedido! ".center(60,'#'))
            input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))
        #input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))
    elif opcao.upper() == "E":
        print(" Função: EXTRATO ".center(60,'#'))
        countExtrato = 0
        for valor in depositos:
            countExtrato += 1
            print(f'Deposito {str(countExtrato)} : R${valor: .2f}')
        countExtrato = 0
        for valor in saques:
            countExtrato += 1
            print(f'Saque {str(countExtrato)} : R${valor: .2f}')
        print(f'O Saldo atual de sua conta é de R${saldo: .2f}')
        input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))
    elif opcao.upper() == "Q":
        print(" Finalizando Sessão! ".center(60,'#'))
        print(" a M10 Bank sempre perto de voce ".center(60,'#'))
        menu = False
    else:
        print(" OPÇÃO INVÁLIDA ".center(60,'#'))
        input(" Pressione ENTER para voltar ao Menu ".center(60,'#'))