def sacar(saldo_atual, saque):
    if saque > saldo_atual:
        print("Valor de saque maior que o saldo. Tente novamente!")
        return saldo_atual
    elif saque <= 0:
        print("Valor de saque inválido!")
        return saldo_atual
    else:
        saldo_atual = saldo_atual - saque
        print(f"Seu atual saldo é: R${saldo_atual:.2f}")
        return saldo_atual


def depositar(saldo_atual, deposito):
    if deposito <= 0:
        print("Valor de deposito inválido!")
        return saldo_atual
    else:
        saldo_atual = saldo_atual + deposito
        print(f"O seu atual saldo é: R${saldo_atual:.2f}")
        return saldo_atual
def verificar_saldo(saldo_atual):
    print(f"Seu saldo atual é: R${saldo_atual:.2f}")
    return saldo_atual

banco = "BEM VINDO AO BANCO MAZZEN"
saldo_atual = 1000.0
print(banco.center(31, "-"))
while True:
    print("ESCOLHA UMA OPÇÃO: ")
    print("[ 1 ] Sacar ")
    print("[ 2 ] Depositar ")
    print("[ 3 ] Verificar saldo")
    print("[ 4 ] Sair")
    opcao = int(input("Qual opção você deseja?"))
    if opcao == 1:
        valor = float(input("Quanto você quer sacar?"))
        saldo_atual = sacar(saldo_atual, valor)
    elif opcao == 2:
        valor = float(input("Qual o valor do deposito?"))
        saldo_atual = depositar(saldo_atual, valor)
    elif opcao == 3:
        saldo_atual = verificar_saldo(saldo_atual)
    elif opcao == 4:
        break;
    else:
        print("OPÇÃO INVÁLIDA!")
