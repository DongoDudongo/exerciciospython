n =[]
for c in range(0,5):
    n.append(int(input('Digite um valor:')))
print('-=-'*30)
print(f'O valores digitados foram : {n}')



# print(f'O maior valor da lista é {max(n)} e sua posição foi {n.index(max(n)) + 1}') infelizmente se tiver dois valores maiores não mostra
print(f'O maior valor da lista foi {max(n)} e sua posição foi ',end='')
for j , d in enumerate(n) :
    if d == max(n):
        print(f'{j + 1}...',end='' )
print()

#print(f'O menor valor da lista é {min(n)} e sua posição foi {n.index(min(n)) + 1}') se tiver dois valores minimos só mostra o primeiro
print(f'O menor valor da lista foi {min(n)} e sua posição foi ',end='')
for j,d in enumerate(n):
    if d == min(n):
        print(f'{j + 1}...',end='')

print()
print('-=-'*30)
print('resolução do curso em video')
print('-=-'*30)
print()
l = []
min = 0
max =0
for d in range(0,5):
    print(int(input(f'digite um valor na posição {d}:')))
    if c ==0:
        min = max =l[c]
    else:
        if l[c] > max:
            max = l[c]
        if l[c]< min:
            min = l[c]
print('-=-'*30)
print(f'Você digitou os valores: {l}')
print(f'O maior valor é {max} e sua posição é', end ='')
for i,v in enumerate(l):
    if v == max:
        print(f'{i}...',end='')
print()
print(f'O menor valor é {min} e sua posição é')
for i,v in enumerate(l):
    if v == min:
        print(f'{i}...',end='')
