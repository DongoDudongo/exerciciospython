from ex123.utilidadesCEV import moeda

#programa principal
n = float(input('Digite um valor :R$'))
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O aummento de 10%  de R${n} é de R${moeda.aumentar(n,10)}')
print(f'O desconto de 50% de R${n} é de R${moeda.diminuir(n,50)}')