# gerenciador_tarefas.py

tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada.')

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")

def remover_tarefa(indice):
    try:
        tarefa_removida = tarefas.pop(indice - 1)
        print(f'Tarefa "{tarefa_removida}" removida.')
    except IndexError:
        print("Índice inválido. Tente novamente.")

def main():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(tarefa)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a ser removida: "))
                remover_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif escolha == '4':
            print("Saindo do gerenciador de tarefas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
