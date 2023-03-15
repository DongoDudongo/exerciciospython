n1 =  int(input('digite um número:'))
s = n1 +1
dim = n1 -1
d = n1*2
t = n1*3
q =n1**(1/2)

print('O número que você escolheu foi {}\nseu sucessor é {}\nseu antecessor {}'.format(n1,s,dim))
print('Seu dobro {} , seu triplo {} e sua raiz {:.1f}'.format(d,t,q))

nota1 = float(input('Qual foi sua nota de História?'))
nota2 = float(input('Qual foi sua nota de geografia?'))

sm = (nota1 + nota2)/2

print('sua média é {}'.format(sm))