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




produtos = {'celular': 1500, 'camera': 1000, 'fone de ouvido': 800, 'monitor': 2000}

userAns = input('Digite um produto: ')
userAns = userAns.lower()
cadastrar = False 

if userAns in produtos:
   print(f'O produto selecionado foi {userAns} e o valor é {produtos[userAns]}')
elif userAns !=produtos : 
   print('Talvez o produto não esteja cadastrado')
   newItem = input('cadastrar:')
   cadastrar = True
   produtos.append(newItem)
   print(produtos)
else: 
   print('Obrigado por nos procurar')

for produto in produtos:
    print(f'Produto: {produto}, Preço: {produtos[produto]}')