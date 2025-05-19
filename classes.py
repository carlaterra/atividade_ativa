import datetime

class Clientes ():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone 
    def __str__(self):
        return f"Nome Cliente: {self.nome} e Telefone: {self.telefone}"


class Produtos ():
    def __init__(self, nome, tamanho, quantidade, valor):
        self.nome = nome
        self.tamanho = tamanho
        self.quantidade = quantidade 
        self.valor = valor 
        self.total = 0
    def totalProduto (self, quantidade): 
        self.quantidade = quantidade
        self.total = self.quantidade * self.valor
    def __repr__(self):
        return f"Produto: {self.nome}, Tamanho: {self.tamanho}, Quantidade: {self.quantidade}, Valor: {self.valor}\n"
    def __str__(self):
        return f"Nome Produto: {self.nome} Tamanho: {self.tamanho} Quantidade: {self.quantidade} valor: {self.valor}"
        
class Pedidos ():
    def __init__(self, cliente, produtos ,produtoTotal, data):
        self.cliente = cliente
        self.produtos = produtos 
        self.produtoTotal = produtoTotal
        self.data = data

    def contaTotal(self): 
        self.produtoTotal = sum(self.produtoTotal)

    def __str__(self):
        return f"#### RESUMO DO PEDIDO ####\n\n---> {self.cliente}\n\n---> Total Conta = {self.produtoTotal}\n\n---> Data e Hora: {self.data}\n\nITENS SELECIONADOS\n\n{self.produtos}\n\n"

