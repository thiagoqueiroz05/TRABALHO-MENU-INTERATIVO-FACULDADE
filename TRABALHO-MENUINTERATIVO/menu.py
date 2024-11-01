from produto import Produto
#IMPORTAÇÃO DO PRODUTO.PY PRO MENU.PY PRA CONSEGUIR TRAZER OS DADOS !

def adicionar_produto(produtos):
#FUNÇÃO DE ADICIONAR OS PRODUTOS 


    nome = input("Nome do produto: ") 
    preco = float(input("Preço do produto: R$")) 
    quantidade = int(input("Quantidade do produto: "))  
    produto = Produto(nome, preco, quantidade) 
    produtos.append(produto)
    print("Produto adicionado com sucesso!") 
    #ASSIM QUE ADICIONAR O PRODUTO DAR ESSA MENSAGEM !

def exibir_produtos(produtos):
   #FUNÇÃO DE EXIBIR OS PRODUTOS 


    if not produtos:
        print("Nenhum produto cadastrado.") 
        #CASO NÃO TENHA NENHUM REGISTRADO IRÁ DAR ESSA MENSAGEM !
    else:
        for i, produto in enumerate(produtos):
            print(f"\nProduto {i + 1}:")
            produto.exibir_informacoes()

def atualizar_preco(produtos):
#FUNÇÃO DE ATUALIZAR O PREÇO DOS PRODUTOS 


    nome = input("Informe o nome do produto para atualizar o preço: ") #ISSO É OQUE IRÁ APARECER QUANDO FOR ADICIONAR PREÇO AO PRODUTO SELECIONADO
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            novo_preco = float(input("Novo preço: R$"))  #PREÇO NOVO ATUALIZADO !
            produto.atualizar_preco(novo_preco)
            return
    print("Produto não encontrado.") 
    #MENSAGEM DE ERRO CASO VOCÊ ESCREVA O NOME DO PRODUTO ERRADO !

def atualizar_quantidade(produtos):
    #ATUALIZA QUANTIDADE DO PRODUTOS !


    nome = input("Informe o nome do produto para atualizar a quantidade: ") 
    ##ISSO É OQUE IRÁ APARECER QUANDO FOR ADICIONAR QUANTIDADE AO PRODUTO SELECIONADO
    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            nova_quantidade = int(input("Nova quantidade: ")) 
            produto.atualizar_quantidade(nova_quantidade)
            return
    print("Produto não encontrado.") 
    #MENSAGEM DE ERRO CASO VOCÊ ESCREVA O NOME DO PRODUTO ERRADO !

def menu():
    #FUNÇÃO QUE CHAMA O MENU INTERATIVO
    produtos = []
    
    while True:
        print("\nMenu :") 
        print("1. Adicionar Produto")
        print("2. Exibir Produtos")
        print("3. Atualizar Preço")
        print("4. Atualizar Quantidade")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ") 
        #OPÇÕES QUE IRÃO APARECER NO MENU INTERATIVO 
        
        if opcao == "1":
            adicionar_produto(produtos)
        elif opcao == "2":
            exibir_produtos(produtos)
        elif opcao == "3":
            atualizar_preco(produtos)
        elif opcao == "4":
            atualizar_quantidade(produtos)
        elif opcao == "5":
            print("Saindo do programa.") 
            #MENSAGEM CASO VOCÊ SELECIONE A OPÇÃO 5 DO SEU TECLADO !
            break 
            #COMANDO PRA ENCERRAR O MENU !
        else:
            print("Opção inválida. Tente novamente.") 
            #MENSAGEM DE ERRO CASO VOCÊ NÃO SELECIONE O NÚMERO DO MENU CERTO !

if __name__ == "__main__":
    menu()