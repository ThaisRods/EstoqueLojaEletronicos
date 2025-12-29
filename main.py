estoque = {
    "Smartphone Galaxy A14": {
        "preco": 1200.00,
        "qtd": 15,
        "detalhes": "Tela 6.6', 128GB, 4GB RAM, Android"
    },
    "Notebook Lenovo IdeaPad 3": {
        "preco": 3500.00,
        "qtd": 8,
        "detalhes": "Intel i5, 8GB RAM, SSD 256GB"
    },
    "Mouse Sem Fio Logitech": {
        "preco": 120.00,
        "qtd": 30,
        "detalhes": "Conexão USB, alcance 10m"
    },
    "Teclado Mecânico Redragon": {
        "preco": 280.00,
        "qtd": 12,
        "detalhes": "Switch blue, RGB, ABNT2"
    },
    "Monitor LG 24 Polegadas": {
        "preco": 950.00,
        "qtd": 10,
        "detalhes": "Full HD, HDMI, 75Hz"
    },
    "Fone de Ouvido Bluetooth JBL": {
        "preco": 300.00,
        "qtd": 20,
        "detalhes": "Bateria 10h, microfone embutido"
    },
    "Caixa de Som Bluetooth": {
        "preco": 220.00,
        "qtd": 18,
        "detalhes": "À prova d'água, 20W"
    },
    "HD Externo 1TB Seagate": {
        "preco": 420.00,
        "qtd": 14,
        "detalhes": "USB 3.0, portátil"
    },
    "Pendrive 64GB Sandisk": {
        "preco": 80.00,
        "qtd": 40,
        "detalhes": "USB 3.1"
    },
    "Impressora HP Deskjet": {
        "preco": 650.00,
        "qtd": 6,
        "detalhes": "Jato de tinta, Wi-Fi"
    },
    "Webcam Logitech HD": {
        "preco": 260.00,
        "qtd": 9,
        "detalhes": "720p, microfone integrado"
    },
    "Roteador TP-Link": {
        "preco": 180.00,
        "qtd": 16,
        "detalhes": "300Mbps, 2 antenas"
    },
    "Carregador Portátil Power Bank": {
        "preco": 150.00,
        "qtd": 25,
        "detalhes": "10000mAh, USB-C"
    },
    "Cabo HDMI 2.0": {
        "preco": 45.00,
        "qtd": 50,
        "detalhes": "4K, 2 metros"
    },
    "Placa de Vídeo GTX 1660": {
        "preco": 1800.00,
        "qtd": 4,
        "detalhes": "6GB GDDR5"
    }
}

def menu():
    print("--------------------------------------------")
    print("\nSISTEMA DE CONTROLE DE ESTOQUE - ELETRÔNICOS\n")
    print("--------------------------------------------")
    print("\n1. ADICIONAR PRODUTO")
    print("2. ATUALIZAR PRODUTO")
    print("3. EXCLUIR PRODUTO")
    print("4. VISUALIZAR ESTOQUE")
    print("5. VISUALIZAR PRODUTO ESPECÍFICO")
    print("6. SAIR\n")
    print("--------------------------------------------")

def addProd():
    print("\n\n--------------------------------------------")
    print("\nADICIONAR NOVO PRODUTO\n")
    print("--------------------------------------------")

    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        print("Esse produto já existe no estoque! Você pode atualizar ou adicionar outro produto.")
        return
    
    while True:
        try: 
            preco = float(input("Valor unitário: "))
            if preco < 0:
                print("O valor uniitário precisa ser maior ou igual a R$ 00.00")
                continue
            break
        except ValueError:
            print("Esse não é um valor válido")

    while True:
        try:
            qtd = int(input("qtd no estoque: "))
            if qtd < 0:
                print("A quantidade precisa ser maior ou igual a 0")
                continue
            break
        except ValueError:
            print("Esse valor náo é um valor válido. \n Obs: É necessário ser um valor inteiro")

    detalhes = input("Especificações do produto: ")

    estoque[nome] = {
        'preco': preco,
        'qtd': qtd,
        'detalhes': detalhes
    }

    print("PRODUTO ADICIONADO NO ESTOQUE!\n")
    print(f"Produto: {nome}")
    print(f"Valor: R$ {preco}")
    print(f"Quantidade disponível no estoque: {qtd}")
    print(f"Especificações: {detalhes}")

def attProd():
    print("\n\n--------------------------------------------")
    print("\nATUALIZAR PRODUTO\n")
    print("--------------------------------------------")

    if not estoque:
        print("\n--O estoque está vazio! Não há produtos para excluir.\n")
        return
    
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("\n--Não existe esse produto no estoque! Adicione-o ou pesquise por outro.\n")
        return

    print("\nINFORMAÇÕES DO PRODUTO:\n")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {estoque[nome]['preco']:.2f}")
    print(f"Quantidade disponível: {estoque[nome]['qtd']}")
    print(f"Especificações do produto: {estoque[nome]['detalhes']}")
    print("--------------------------------------------")
    
    while True:
        try: 
            print("\nSelecione o que deseja alterar:")
            print("1. Quantidade no estoque")
            print("2. Preço unitário")
            print("3. Sair \n\n")
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                qtd = int(input("Digite a nova quantidade em estoque: "))
                if qtd < 0:
                    print("A quantidade precisa ser maior ou igual a 0")
                    continue
                estoque[nome]['qtd'] = qtd
                print("Quantidade atualizada comm sucesso!")
                break
            elif opcao == 2:
                preco = float(input("Digite o novo valor unitário: "))
                if preco < 0:
                    print("A quantidade precisa ser maior ou igual a 0")
                    continue
                estoque[nome]['preco'] = preco
                print("Valor atualizado comm sucesso!")
                break
            elif opcao == 3:
                print("Voltando ao MENU")
                break
            else:
                print("Opção inválida")
                continue

        except ValueError:
            print("Opção inválida")

def excProd():
    print("\n\n--------------------------------------------")
    print("\nEXCLUIR PRODUTO\n")
    print("--------------------------------------------")

    if not estoque:
        print("\n--O estoque está vazio! Não há produtos para excluir.\n")
        return
    
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("\n--Não existe esse produto no estoque! Adicione-o ou pesquise por outro.\n")
        return

    print("\nINFORMAÇÕES DO PRODUTO:\n")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {estoque[nome]['preco']:.2f}")
    print(f"Quantidade disponível: {estoque[nome]['qtd']}")
    print(f"Especificações do produto: {estoque[nome]['detalhes']}")
    print("--------------------------------------------")

    print("\nTEM CERTEZA QUE DESEJA EXLUIR ESSE PRODUTO?")
    opcao = input("(s/n): ").lower()

    if opcao == "s":
        del estoque[nome]
        print("\nProduto excluído com sucesso!")
        return
    elif opcao == "n":
        print("OK! Exclusão cancelada.")
        return
    else:
        print("Opção inválida")
        return
    
def verEstoque():
    print("\n\n--------------------------------------------")
    print("\nESTOQUE COMPLETO\n")
    print("--------------------------------------------")

    if not estoque:
        print("\n O estoque está vazio!\n")
        return
    
    print(f"\nQuantidade de produtos cadastrados: {len(estoque)}\n")
    print("--------------------------------------------")
    
    for nome, dados in estoque.items():
        print(f"\nProduto: {nome}")
        print(f"Quantidade: {dados['qtd']} | Valor unitário: R$ {dados['preco']:.2f}")
        print(f"Especificações do produto: {dados['detalhes']}")
        print("\n--------------------------------------------")

def verProduto():
    print("\n\n--------------------------------------------")
    print("\nVISUALIZAR PRODUTO\n")
    print("--------------------------------------------")

    if not estoque:
        print("\n--O estoque está vazio! Não há produtos para visualizar.\n")
        return
    
    nome = input("Nome do produto: ").strip()

    if nome not in estoque:
        print("\n--Não existe esse produto no estoque! Adicione-o ou pesquise por outro.\n")
        return
    
    print("\nINFORMAÇÕES DO PRODUTO:\n")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {estoque[nome]['preco']:.2f}")
    print(f"Quantidade disponível: {estoque[nome]['qtd']}")
    print(f"Especificações do produto: {estoque[nome]['detalhes']}\n")
    print("--------------------------------------------")
    
    voltar = input("aperte ENTER para voltar")
    return


def main():
    while True:
        menu()
        try:
            opcao = int(input("Escolha a opçao desejada (apenas o nº): "))

            if opcao == 1:
                addProd()
            elif opcao == 2:
                attProd()
            elif opcao == 3:
                excProd()
            elif opcao == 4:
                verEstoque()
            elif opcao == 5:
                verProduto()
            elif opcao == 6:
                print("Saindo....")
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite apenas números!")
            continue


if __name__ == "__main__":
    main()




    





        
