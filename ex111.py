from time import sleep

def maior(*num):
    cont= maior =0
    print('-='*30)
    print('Analisando valores...')
    for valores in num:
        print(f'{valores} ', end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valores
        else:
            if maior < valores:
                maior = valores
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(1,6,9,5,4,8,99)
maior(3,6,5,2)
maior(2,3,6)
maior(0)
maior()