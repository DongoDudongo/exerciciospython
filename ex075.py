from random import randint
n1 = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10))

print('Os valores sorteados foram: ',end = '')
for c in n1:
    print(f'{c} ',end ='')

print(f'\nO maior valor sorteado foi {max(n1)}')
print(f'O menor valor sorteado foi {min(n1)}')
