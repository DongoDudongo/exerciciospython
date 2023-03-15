n = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor:'))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print('-=-'*30)
print(f'Os número escolhidos foram : {sorted(n)}')
print(f'Os valores pares foram :{sorted(n[0])}')
print(f'Os valores impares foram: {sorted(n[1])}')
