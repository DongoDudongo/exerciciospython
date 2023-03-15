galera =list()
dados = list()
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('nome:')))
    dados.append(int(input('Idade:')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
if totmai >=1 and totmen >= 1:
    print(f'Temos {totmai} maiores e {totmen} menores de idade.')
elif totmai >=1 and totmen ==0:
    print(f'temos {totmai} maiores de idade e não possuimos nenhum menor de idade')
elif totmen >= 1 and totmai == 0:
    print(f'Temos {totmen} menores de idade e nenhum maior de idade.')