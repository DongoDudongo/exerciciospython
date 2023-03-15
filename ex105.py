time = []
jogador ={}
partida = []
while True:
    jogador.clear()
    partida.clear()
    jogador['nome'] = str(input('Nome:'))
    p = int(input('quantas partidas jogou?'))
    for c in range(0,p):
        partida.append(int(input(f'   Quantos gols na partida {c+1}:')))
        jogador['gols'] = partida[:]
        jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp =str(input('Quer continuar [S/N]?')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro!por faor responda S ou N.')
    if resp == 'N':
        break
print('-'*40)
print('cod ' ,end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v  in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 interrompe)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!não existe jogador com código {busca}.')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i ,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')