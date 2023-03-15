from time import sleep

print('-=-' * 40)
print('Olá sou Poli.A.I.,sua amiga do trânsito.')
print('-=-' * 40)
sleep(1)

carro = float(input('Vamos lá,sabendo que o limite de velocidade é 80Km\h. \nqual a velocidade do seu carro?'))
m = (carro - 80) * 7
m1 = (carro - 80)
print('PROCESSANDO')
sleep(2)
if carro <=80:
    print('PARABÉNS!Você dirige muito bem')
else:
    print('Infelizmente,Você ultrapassou o limite em {:.1f} Km\h \nterei que multar você em R$ {:.1f}'.format(m1,m))
