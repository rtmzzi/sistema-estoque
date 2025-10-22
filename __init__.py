count = 0
ligado = True
ligadoVezes = 0


estoque = {
    "maca": {"quantidade": 10, "preco": 2.5},
    "banana": {"quantidade": 5, "preco": 3.0},
    "laranja": {"quantidade": 8, "preco": 4.0},
}


while ligado:
    ligadoVezes += 1
    print(f"inicio contagem: {ligadoVezes}\n")

    def getQuantFruta(fruta):
        for k,v in estoque.items():
            if fruta == k:
                print(f"o estoque de {fruta} atual :")
                return v['quantidade'] 


    opcao_str = input("digite a opção:\n"
        "1 - quantidade \n"
        "2 - adicionar produto novo \n"
        "3 - Vender produto \n"
        "4 - atualizar preço de algum produto \n"
        "5 - sair \n"
    )

    print(f"Você selecionou a opção {opcao_str}")
    opcao_int = int(opcao_str)




    if opcao_int == 1:
        print("As quantidades são:1")
        for fruta, dado in estoque.items():
            print(f"a {fruta} tem {dado['quantidade']} unidades e custa R$ {dado['preco']}")


    if opcao_int == 2:
        add_item = input("Qual fruta você deseja adicionar?\n")
        add_quantidade = int(input("Qual a quantidade dessa fruta?\n"))
        add_preco = float(input("Qual o preço R$ ?\n"))
        estoque[add_item] = {"quantidade": add_quantidade, "preco": add_preco}
        print(f"Fruta {add_item} adicionada com {add_quantidade} unidades a R$ {add_preco}")


    if opcao_int == 3:
        print("Qual produto voce quer vender?\n")
        for k,v in estoque.items():
            count += 1
            print(f"{count} - {k}")
            
        produtoVenda = input(f"Qual produto você quer vender? \n")
        for k,v in estoque.items():
            if produtoVenda == k:
                quantidadeVenda = int(input(f"qual a quantidade de {produtoVenda} que voce quer vender?\n"))
                v['quantidade'] -= quantidadeVenda
                print(getQuantFruta(produtoVenda))
            else:
                continue

    if opcao_int == 5:
        print("Voce saiu do programa")
        ligado = False