class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        #CONSTRUTOR DA CLASSE DOS PRODUTOS 

        self.nome = nome 
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self) -> None:
        #FUNÇÃO DE EXIBIR AS INFORMAÇÕES DOS PRODUTOS 

        print("Informações do produto:")
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco: float) -> None:
        #FUNÇÃO DE ATUALIZAR O PREÇO DOS PRODUTOS 

        self.preco = novo_preco
        print(f"Preço atualizado para R${self.preco:.2f}") 
        #MENSAGEM QUE IRÁ APARECER ASSIM QUE VOCÊ ATUALIZAR O PREÇO DO PRODUTO !

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        #FUNÇÃO DE ATUALIZAR A QUANTIDADE DOS PRODUTOS 

        self.quantidade = nova_quantidade
        print(f"Quantidade atualizada para {self.quantidade}") 
        #MENSAGEM QUE IRÁ APARECER ASSIM QUE VOCÊ ATUALIZAR A QUANTIDADE DO PRODUTO !