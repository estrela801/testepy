# Crie um sistema de consulta de preços
 
# Seu sistema deve:
 
# - Pedir para o usuário o nome de um produto
 
# - Caso o produto exista na lista de produtos, o programa deve
# retornar o preço do produto como resposta
 
# - Ex: O produto celular custa R$1500
 
# - Caso o produto não exista na lista de produtos, o programa deve
# printar uma mensagem para o usuário tentar novamente
 
# Celular: 1500, câmera: 1000, fone de ouvido: 800, monitor: 2000

# Caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto.
 
# Se ele responder sim, o programa deve pedir o nome do produto e o preço do produto e cadastrar no dicionário de preços.
 
# Em seguida do cadastro bem sucedido, o programa deve imprimir o
# dicionário de preços atualizado.




produtos = {'celular': 1500, 'câmera': 1000, 'fone de ouvido': 800, 'monitor': 2000}

fela = input('diga-me o produto fela da puta: ')
if fela in produtos:
    print(f'Essa méda {fela} custa: {produtos[fela]}')
else:
    print('Não tem seu fela. Cadastra ele ai desgraça')
    prodPreco = input(f'Me diz quando custa essa merda de {fela}: ')
    newProd = fela
    produtos[newProd] = prodPreco
    print('Ta aqui a disgraça da lista do que eu tenho')
    for produto in produtos:
        print(produto,produtos[produto])
    print('pronto seu merda')

 