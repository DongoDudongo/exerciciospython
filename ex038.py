num =int(input('Digite um número:'))
print('''escolha uma das bases de conversão:
[1] binário
[2] octagonal
[3] hexadecimal''')
op =int(input('sua opção:'))

if op ==1:
    print('{}  convertido em binário fica {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('{} convertido em octagonal fica {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('{} convertido em hexadecimal fica {}'.format(num,hex(num)[2:]))
else:
    print('oção inválida')
