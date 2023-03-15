n = s = cont =0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
    cont += 1
print('A soma dos números é {}'.format(s))
print(f'A soma é {s}.') # f strings
print(f'Você digitou {cont} números.')