# Listar para guardar tarefas 
minhas_tarefas = []

while True:
    print("\n===MENU DE TAREFAS===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefas")
    print("4 - Sair")

    Escolha = input("Escolha uma opção: ")

    #Verificação da opção
    if Escolha =="1":
        tarefa = input("Digite a tarefa: ")

        if tarefa.strip() != "":
            minhas_tarefas.append(tarefa)
            print(" Tarefa Adicionada!")
        else:
            print(" Não pode ser vazio!")

    elif Escolha == "2":
        if len(minhas_tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")
            for i in range(len(minhas_tarefas)):
                print(f"{i+1} - {minhas_tarefas[i]}")

    elif Escolha == "3":
        if len(minhas_tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            print("\nTarefas:")
            for i in range(len(minhas_tarefas)):
                print(f"{i+1} - {minhas_tarefas[i]}")

                num = int(input("Digite o Número da tarefa que deseja remover:"))

                if 1 <= num <= len(minhas_tarefas):
                    removida = minhas_tarefas.pop(num -1)
                    print(f"tarefa '{removida}' removida!")
                else:
                    print("Número Inválido")

    elif Escolha == "4":
        print("Até logo e volte sempre!")
        break
    else:
        print(" Opção Inválida")