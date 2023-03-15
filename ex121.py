from ex123.utilidadesCEV import moeda

#programa principal
n = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O aummento de 10%  de {moeda.moeda(n)} é de {moeda.moeda(moeda.aumentar(n,10))}')
print(f'O desconto de 50% de {moeda.moeda(n)} é de {moeda.moeda(moeda.diminuir(n,50))}')