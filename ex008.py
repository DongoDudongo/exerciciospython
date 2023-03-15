nome = input ('qual seu nome?')
print('É um enorme prazer {:=^20}!'.format(nome))

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
s = n1+n2
d = n1/n2
m = n1*n2
di =n1//n2
e =n1**n2

print('A soma é {} ,a divisão é {} e produto é {}'.format(s,d,m,))
print('A divisão inteira é {} e a Potência é {}'.format(di,e))

print('divisão é {:.2f}'.format(d))

print('para unir todo mundo agora')
print('A soma é {} ,a divisão é {} e produto é {}'.format(s,d,m,), end=' ')
print('A divisão inteira é {} e a Potência é {}'.format(di,e))