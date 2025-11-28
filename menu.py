from ufc import Campus

campi = []

def menu():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Adicionar Campus")
        print("2. Listar Campus")
        print("3. Gerenciar Campus")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Campus: ")
            campi.append(Campus(nome))
        elif escolha == "2":
            for i, campus in enumerate(campi):
                print(f"{i + 1}. {campus.nome}")
        elif escolha == "3":
            for i, campus in enumerate(campi):
                print(f"{i + 1}. {campus.nome}")
            idx = int(input("Escolha o número do Campus: ")) - 1
            if 0 <= idx < len(campi):
                gerenciar_campus(campi[idx])
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

def gerenciar_campus(campus):
    while True:
        print(f"\n--- Gerenciando Cursos do Campus {campus.nome} ---")
        print("1. Adicionar Curso")
        print("2. Listar Cursos")
        print("3. Atualizar Curso")
        print("4. Remover Curso")
        print("5. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Curso: ")
            campus.adicionar_curso(nome)
        elif escolha == "2":
            for i, nome in enumerate(campus.listar_cursos()):
                print(f"{i + 1}. {nome}")
        elif escolha == "3":
            for i, nome in enumerate(campus.listar_cursos()):
                print(f"{i + 1}. {nome}")
            idx = int(input("Qual curso atualizar? ")) - 1
            if 0 <= idx < len(campus.cursos):
                novo_nome = input("Novo nome do Curso: ")
                campus.atualizar_curso(idx, novo_nome)
        elif escolha == "4":
            for i, nome in enumerate(campus.listar_cursos()):
                print(f"{i + 1}. {nome}")
            idx = int(input("Qual curso remover? ")) - 1
            if 0 <= idx < len(campus.cursos):
                campus.remover_curso(idx)
        elif escolha == "5":
            break
        else:
            print("Opção inválida.")

menu()
