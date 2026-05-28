lista = []
def adicionar_tarefa():
    tarefa = input("O que você deseja adicionar a lista de tarefas?")
    lista.append(tarefa)
    print("Adicionando tarefa...")
def remover_tarefa():
    if len(lista) == 0:
        print("Lista vazia!")
        return
    else:
        for indice, tarefa in enumerate(lista):
            print(f"[{indice + 1}] - {tarefa}")

        tarefa = int(input("Qual tarefa você deseja retirar? "))
        posicao_real = tarefa - 1

        posicao_real = tarefa - 1
        if 0 <= posicao_real < len(lista):
            tarefa_removida = lista.pop(posicao_real)
            print(f"Tarefa {tarefa_removida}removida com sucesso!")
        else:
              print("Tarefa inválida!")
def ver_tarefa():
    if len(lista) == 0:
        print("A sua lista está vazia!")
        return
    print("SUAS TAREFAS: ")
    for indice, tarefa in enumerate(lista):
        print(f"[{indice + 1}] - {tarefa}")
    total_de_tarefas = len(lista)
    print(f"Você tem {total_de_tarefas} para fazer")

print("BEM VINDO AO TO DO LIST")
while True:
    print("O que você deseja fazer?")
    print("[ 1 ] Adicionar tarefa")
    print("[ 2 ] Remover tarefa")
    print("[ 3 ] Ver tarefa")
    opcao = int(input(""))
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        remover_tarefa()
    elif opcao == 3:
        ver_tarefa()
    else:
        break