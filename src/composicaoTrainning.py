class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.num_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f'Fechando o pedido: {self.num_pedido}')
        print(f'valor do carrinho: {self.valor_carrinho}')
        print(f'nome do cliente: {self.cliente.nome}')


cliente = Cliente("joao", "4534534")

televisao = Produto("Televisão", 1000.90)
maquina_cafe = Produto("Máquina de Café", 89.80)
teclado = Produto("Teclado Mecânico", 175.20)

produtos = [televisao, maquina_cafe]

carrinho = CarrinhoCompras(cliente, produtos)

carrinho.adicionar_produto(teclado)
print(carrinho.fechar_carrinho())
