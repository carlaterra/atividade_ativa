from classes import Clientes, Produtos, Pedidos
import datetime

print ('Bem vindo ao Coffee Shop Tia Rosa')

nome = input ('Informe seu nome: ')
telefone = input ('Informe seu telefone:')
cliente = Clientes (nome, telefone)
print ('\n')

print ('Produtos disponiveis no Coffee Shop')

produto = Produtos('Coffe black', 'Large', 2 ,10.50)
dicionarioProdutos = {
    "1": Produtos('Coffe black', 'Large', 99 ,10.50),
    "2": Produtos('Muffin', 'Small', 99 , 8.50),
    "3": Produtos ('Agua mineral' , 'pequena', 99 , 3.50)
    }
print (dicionarioProdutos)
listaProdutosTotal = []
listaProdutos = []

idProduto = input ('Informe o id do produto:')
quantidadeProduto = float(input ('Informe a quantidade do produto:'))
produto = dicionarioProdutos[idProduto]
produto.totalProduto(quantidadeProduto)


listaProdutosTotal.append(produto.total)
listaProdutos.append(produto)

opcao = input ('Deseja informar outro produto: <s ou n>  ')
while opcao == 's':
    idProduto = input ('Informe o id do produto:')
    quantidadeProduto = float(input ('Informe a quantidade do produto:'))
    produto = dicionarioProdutos[idProduto]
    produto.totalProduto(quantidadeProduto)
    listaProdutosTotal.append(produto.total)
    listaProdutos.append(produto)
    opcao = input ('Deseja informar outro produto: < s ou n>  ')
    

contaTotal = sum(listaProdutosTotal)

pedido = Pedidos (cliente, listaProdutos, listaProdutosTotal, 
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
pedido.contaTotal()



       





print (pedido)