from ex123.utilidadesCEV import moeda

#programa principal
n = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n,True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,True)}')
print(f'O aummento de 10%  de {moeda.moeda(n)} é de {moeda.aumentar(n,10,True)}')
print(f'O desconto de 50% de {moeda.moeda(n)} é de {moeda.diminuir(n,50,True)}')

#nesse exercicio foi a criação  do formato = False