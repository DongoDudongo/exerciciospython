from time import sleep

print('\033[1;34m-=\33[m' * 20)
print('Analisador de Triângulos')
print('\033[1;34m-=\33[m' * 20)
sleep(1)

r1 = float(input('primeiro segmento:'))
sleep(1)
r2 = float(input('segundo seguimento:'))
sleep(1)
r3 = float(input('terceiro seguimento:'))
print('ANALISANDO')
sleep(2)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 +r1:
    print('Esses seguimento \033[4;34mPODEM\033[m formar um Triânguilo')
else:
    print('Esses seguimento \033[4;31mNÃO PODEM\033[m formar um Triângulo')

