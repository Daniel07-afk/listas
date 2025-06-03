nomes = []

while True:
    print('Opções:')
    print('1-Cadastrar')
    print('2-Consultar')
    print('3-Excluir')
    print('4-Sair')
    
    opcao = input("Digite a opção que deseja:")
    if opcao == "1":
        nome = input("Digite o nome: ")
        nomes.append(nome)
        print("Contato cadastrado com sucesso!")

    elif opcao == "2":
        print("\nContatos cadastrados:")
        for i, nome in enumerate(nomes):
            print(f"{i + 1} - {nome}")
    elif opcao == "3":
        print("\nContatos cadastrados:")
        for i, nome in enumerate(nomes):
            print(f"{i + 1} - {nome}")
        num = int(input("Digite o número do contato que deseja excluir: "))
        if 0 < num <= len(nomes):
            excluido = nomes.pop(num - 1)
            print(f"Contato '{excluido}' excluído com sucesso!")
        else:
            print("Número inválido.")

    elif opcao == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente")