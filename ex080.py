valores = []
valores.append(4)
valores.append(5)
valores.append(10)

for v in valores:# representa a lista
    print(f'{v}...',end='')
print('cheguei ao fim da lista')
valor = []
for cont in range(0,5):
    valor.append(int(input('\nDigite um valor:')))

for c, v in enumerate(valor): # através de enumeração ,representando a lista
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao fim da lista')