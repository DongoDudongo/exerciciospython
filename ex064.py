cont = 0

n = int(input('Digite um número [999 é para parar]:'))
s = n
while n != 999:

    n = int(input('Digite um número [999 é para parar]:'))
    cont += 1
    s += n

print('Você digitou {} com exceção do 999 ,e a soma deles é {}.'.format(cont,s ))