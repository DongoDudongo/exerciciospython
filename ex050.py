from  time import sleep
print('informe seis número,porém só somarei os pares.')
sleep(1)
s = 0
cont = 0
for c in range(0 ,6):
    n = int(input('escolha um número:'))
    if n % 2 == 0:
        cont +=1
        s +=n
        sleep(1)
        print('você informou {} e a soma desses valores é {}.'.format(cont, s))
else:
    print('você só informou números impares.')




