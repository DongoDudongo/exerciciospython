n1 = int(input('Escolha um número:'))
n2 = int(input('Escolha o segunda número:'))

if n1>n2:
    print('o primeiro número é maior')
elif n2>n1:
    print('o segundo número é maior')
elif n1 == n2 or n2 == n1:
    print('os número são iguais.')