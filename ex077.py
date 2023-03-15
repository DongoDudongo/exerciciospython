produtos = ('Lápias',1.75,
            'borracha',2,
            'caderno',15.90,
            'estojo', 25 ,
            'transferidor',4.20,
            'compasso',9.99,
            'mochila',120.32,
            'caneta',2.30,
            'livro',34.9)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')