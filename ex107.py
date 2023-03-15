def area(a,b):
    m = a * b
    print(f'A área do terredo ne {a:.1f} x {b:.1f} é igual a {m}m²')
def lin():
    print('-'*30)
lin()
print('<<< CONTRILE DE TERRENOS >>>')
lin()
l = float(input('Largura(m):'))
c = float(input('Comprimento(m):'))
area(a = l,b = c)