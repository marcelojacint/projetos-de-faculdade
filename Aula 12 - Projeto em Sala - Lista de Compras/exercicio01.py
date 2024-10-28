lista_compras = []

def adicionar_item():
    nome = input("Digite o nome do item: ")
    categoria = input("Digite a categoria do item: ")
    lista_compras.append({"nome": nome, "categoria": categoria})
    print(f"Item '{nome}' adicionado com sucesso!\n")

def remover_item():
    nome = input("Digite o nome do item a ser removido: ")
    encontrado = False
    for item in lista_compras:
        if item["nome"].lower() == nome.lower():
            lista_compras.remove(item)
            print(f"Item '{nome}' removido com sucesso!\n")
            encontrado = True
            break
    if not encontrado:
        print(f"Item '{nome}' não encontrado na lista.\n")

def exibir_lista():
    if lista_compras:
        print("Lista de Compras:")
        for item in lista_compras:
            print(f"- {item['nome']} ({item['categoria']})")
        print()
    else:
        print("A lista de compras está vazia.\n")

def menu():
    while True:
        print("Menu de Opções:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Exibir lista")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            exibir_lista()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
