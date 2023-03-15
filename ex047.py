n = int(input('digite um número:'))

for c in range(0 , n+1):
    print(c)
print('FIM')

print('-=-' * 10)

i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))

for d in range(i, f+1 , p):
    print(d)
print('FIM')

print('-=-' * 10)

s = 0

for e in range(0,4):
    n = int(input('Digite um número:'))
    s += n

print('A soma de todos eles é {}'.format(s))


