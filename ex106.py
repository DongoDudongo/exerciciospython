def lin():
    print('-'*30)
lin()
print('     curso em video      ')
lin()

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

titulo('    curso em video      ')

def soma(a,b):
    s = a + b
    print(s)

print(1,5)
print(3,4)

def sum(a,b):
    print(f'A = {a} e B = {b}')
    s = a +b
    print(f'A soma de A + B = {s}')

sum(5,9)
sum(b =99 , a =1)#pode-se inverter as ordens ,desde que definidos as variaveis.

def contador(*num):# esse * é o simbolo de descompactamento,para quando a mts numeros ou obejtos.
    print(num)

contador(9,6,5,4,2)
contador(9,5,6,7)

def contador(*num):
    for valor in num:
        print(valor,end='')
    print('FIM')

contador(9,6,5,4)
contador(5,6,9,8,2,3)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(1,2,3,5,6,9)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

contador(1,5,6,9,8)
def som(*num):
    s = 0
    for valores in num:
        s += valores
    print(f'somando os valores {num} é igual a {s}')
som(1,2,5,6,9)
