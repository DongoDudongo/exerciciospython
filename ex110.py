from time import sleep

def lin():
    print('~'*30)
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'A contagem de  {i} até {f} de {p} em {p}.')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
        sleep(0.5)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end = '', flush = True)
            sleep(0.5)
            cont -= p
        print('FIM')



lin()
contador(1,10,1)
lin()
contador(10,0,2)
lin()
print('Agora é sua vez de fazer sua contagem.')
ini = int(input('Inicio:'))
fini = int(input('Fim'))
pas = int(input('Passo:'))
lin()
contador(ini,fini,pas)
lin()
