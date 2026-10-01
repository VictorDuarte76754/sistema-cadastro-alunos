import json
import os


def carregar_alunos():
    if os.path.exists("alunos.json"):
        try:
            with open("alunos.json", "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    return []


def salvar_alunos():
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            alunos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


alunos = carregar_alunos()


def adicionar_aluno():
    print("\n--- ADICIONAR ALUNO ---")
    print("Digite 'cancelar' a qualquer momento para voltar ao menu.")

    nome = input("Digite o nome do aluno: ").strip()

    if nome.lower() == "cancelar":
        print("\nCadastro cancelado.")
        return

    while True:

        entrada_idade = input("Digite a idade do aluno: ").strip()

        if entrada_idade.lower() == "cancelar":
            print("\nCadastro cancelado.")
            return

        try:
            idade = int(entrada_idade)

            if idade > 0:
                break

            else:
                print("A idade deve ser maior que 0.")

        except ValueError:
            print("Digite uma idade válida.")

    while True:

        entrada_nota = input("Digite a nota do aluno (0 a 10): ").strip()

        if entrada_nota.lower() == "cancelar":
            print("\nCadastro cancelado.")
            return

        try:
            nota = float(entrada_nota)

            if 0 <= nota <= 10:
                break

            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)

    salvar_alunos()

    print(f"\nAluno {nome} cadastrado com sucesso!")


def listar_alunos():

    print("\n--- LISTA DE ALUNOS ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):

        print(
            f"{i}. Nome: {aluno['nome']} | "
            f"Idade: {aluno['idade']} | "
            f"Nota: {aluno['nota']:.1f}"
        )


def buscar_aluno():

    print("\n--- BUSCAR ALUNO ---")

    nome_busca = input("Digite o nome do aluno: ").strip()

    for aluno in alunos:

        if aluno["nome"].lower() == nome_busca.lower():

            print("\nAluno encontrado!")

            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Nota: {aluno['nota']:.1f}")

            return

    print("Aluno não encontrado.")


def remover_aluno():

    print("\n--- REMOVER ALUNO ---")

    nome_busca = input(
        "Digite o nome do aluno que deseja remover: "
    ).strip()

    for aluno in alunos:

        if aluno["nome"].lower() == nome_busca.lower():

            alunos.remove(aluno)

            salvar_alunos()

            print(
                f"Aluno {aluno['nome']} removido com sucesso!"
            )

            return

    print("Aluno não encontrado.")


def editar_aluno():

    print("\n--- EDITAR ALUNO ---")
    print("Digite 'cancelar' para voltar ao menu.")

    nome_busca = input(
        "Digite o nome do aluno que deseja editar: "
    ).strip()

    if nome_busca.lower() == "cancelar":
        print("\nEdição cancelada.")
        return

    for aluno in alunos:

        if aluno["nome"].lower() == nome_busca.lower():

            while True:

                print("\n--- DADOS ATUAIS ---")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Nota: {aluno['nota']:.1f}")

                print("\nO que deseja alterar?")
                print("1. Nome")
                print("2. Idade")
                print("3. Nota")
                print("4. Voltar ao menu")

                opcao_edicao = input(
                    "Escolha uma opção: "
                ).strip()

                if opcao_edicao == "1":

                    novo_nome = input(
                        "Digite o novo nome: "
                    ).strip()

                    if novo_nome.lower() == "cancelar":
                        print("\nAlteração cancelada.")
                        continue

                    if novo_nome == "":
                        print("\nO nome não pode ficar vazio.")
                        continue

                    aluno["nome"] = novo_nome

                    salvar_alunos()

                    print("\nNome atualizado com sucesso!")


                elif opcao_edicao == "2":

                    while True:

                        nova_idade = input(
                            "Digite a nova idade: "
                        ).strip()

                        if nova_idade.lower() == "cancelar":
                            print("\nAlteração cancelada.")
                            break

                        try:
                            nova_idade = int(nova_idade)

                            if nova_idade > 0:

                                aluno["idade"] = nova_idade

                                salvar_alunos()

                                print(
                                    "\nIdade atualizada com sucesso!"
                                )

                                break

                            else:

                                print(
                                    "A idade deve ser maior que 0."
                                )

                        except ValueError:

                            print(
                                "Digite uma idade válida."
                            )


                elif opcao_edicao == "3":

                    while True:

                        nova_nota = input(
                            "Digite a nova nota (0 a 10): "
                        ).strip()

                        if nova_nota.lower() == "cancelar":
                            print("\nAlteração cancelada.")
                            break

                        try:
                            nova_nota = float(nova_nota)

                            if 0 <= nova_nota <= 10:

                                aluno["nota"] = nova_nota

                                salvar_alunos()

                                print(
                                    "\nNota atualizada com sucesso!"
                                )

                                break

                            else:

                                print(
                                    "A nota deve estar entre 0 e 10."
                                )

                        except ValueError:

                            print(
                                "Digite uma nota válida."
                            )


                elif opcao_edicao == "4":

                    print("\nVoltando ao menu principal.")

                    return


                else:

                    print(
                        "\nOpção inválida. "
                        "Escolha uma opção de 1 a 4."
                    )

    print("\nAluno não encontrado.")


def mostrar_media():

    print("\n--- MÉDIA GERAL ---")

    if len(alunos) == 0:

        print(
            "Não há alunos cadastrados "
            "para calcular a média."
        )

        return

    soma_notas = 0

    for aluno in alunos:
        soma_notas += aluno["nota"]

    media = soma_notas / len(alunos)

    print(f"Média geral das notas: {media:.2f}")


def mostrar_menu():

    print("\n==============================")
    print("   SISTEMA DE ALUNOS")
    print("==============================")

    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Editar informações de aluno")
    print("6. Mostrar média geral das notas")
    print("7. Sair")

    print("==============================")


while True:

    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":

            adicionar_aluno()


        elif opcao == "2":

            listar_alunos()


        elif opcao == "3":

            buscar_aluno()


        elif opcao == "4":

            remover_aluno()


        elif opcao == "5":

            editar_aluno()


        elif opcao == "6":

            mostrar_media()


        elif opcao == "7":

            print("\nSistema encerrado.")

            break


        else:

            print(
                "\nOpção inválida. "
                "Escolha uma opção de 1 a 7."
            )


    while True:

        print("\n==============================")
        print("   O QUE DESEJA FAZER?")
        print("==============================")

        print("1. Reiniciar sistema")
        print("2. Fechar programa")

        print("==============================")

        escolha = input(
            "Escolha uma opção: "
        ).strip()

        if escolha == "1":

            print("\nReiniciando sistema...")

            break


        elif escolha == "2":

            print("\nPrograma finalizado.")

            exit()


        else:

            print(
                "\nOpção inválida. "
                "Escolha 1 ou 2."
            )