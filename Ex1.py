numeros = []
pares = []
impares = []
while True:
  numero = input('Digite um numero ou sair: ')
  if numero == 'sair':
    break
  numeros.append(int(numero))

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)

pares.sort()
impares.sort()

print('Pares:', pares)
print('Impares:', impares)

soma_pares = sum(pares)
soma_impares = sum(impares)

print('Soma dos pares:', soma_pares)
print('Soma dos impares:', soma_impares)