from time import sleep

print('\033[4;35m-=-\033[m' * 30)
print('\033[4;34mANALISADOR DE CADASTROS.\033[m')
print('\033[4;35m-=-\033[m' * 30)
sleep(1)
t = 0 #total de pessoas cadastradas
hc = 0 #homens cadastrados
mc = 0 #mulheres cadastrados
mi = 0 #maiores de 18 anos
mmi = 0 #mulheres com menos de 20 anos
p = 0
r = ''
while True:
    p = int(input('Você quer cadastrar quantas pessoas?'))

    if p >= 1:

        for c in range (1, p+1):

            print(f'\033[4;36m-+-+-+-+-+-+-+-\033[m'*5)

            n = str(input('Nome:'))
            i = int(input('Idade:'))
            s = str(input('Sexo:')).strip().upper()[0]
            t += 1
            if s == 'M':
                hc += 1
            elif s == 'F':
                mc += 1
            elif i >= 18:
                mi += 1
            elif i <= 20 and s == 'F':
                mmi +=1
        sleep(0.5)
    elif p == 0:
        print('\033[4;32mPROGRAMA ENCERRADO\033[m')
        break
        sleep(1)

    else:
        print('\033[4;31mOpção Inválida\033[m')

        sleep(0.5)

        print('\033[4;35m-=-\033[m' * 30)

        p = int(input('Você quer cadastrar quantas pessoas?'))

        print('\033[4;35m-=-\033[m' * 30)

    sleep(0.5)

    print('\033[4;35m-=-\033[m' * 30)

    while r not in 'SN':

        r = str(input('Você quer continuar [S/N] ?')).strip().upper()[0]


        if r == 'S':

            print('\033[4;35m-=-\033[m'* 30)
            p = int(input('Você quer cadastrar quantas pessoas?'))
            print('\033[4;35m-=-\033[m'*30)

            if p >= 1:

                for c in range(1, p + 1):

                    print(f'\033[4;36m-+-+-+-+-+-+-+-\033[m' * 5)
                    n = str(input('Nome:'))
                    i = int(input('Idade:'))
                    s = str(input('Sexo:')).strip().upper()[0]
                    t += 1

                    if s == 'M':

                        hc += 1
                    elif s == 'F':
                        mc += 1

                    elif i >= 18:
                        mi += 1
                    elif i <= 20 and s == 'F':
                        mmi += 1
                sleep(0.5)
        elif p == 0:
            print('\033[4;32mPROGRAMA ENCERRADO\033[m')
            break
            sleep(1)
        else:
            print('\033[4;32mPROGRAMA ENCERRADO\033[m')
            break
            sleep(1)

print('\033[4;35mANALISANDO DADOS\033[m')
sleep(2)
if t >=1:
    print(f'Teve o total de {t} pessoas cadastradas.')
    sleep(0.5)
elif hc >=1 and mc >=1:
    print(f'Teve {hc} homens cadastrados e {mc} Mulheres cadastradas.')
    sleep(0.5)
elif hc ==0 and mc >= 1:
    print(f'Nesse programa só teve {mc} de  mulheres cadastradas e nenhum homem.')
    sleep(0.5)
elif hc >= 1 and mc == 0:
    print(f'Nesse programa só teve {hc} de homens cadastrados e nenhuma mulher.')
    sleep(0.5)
elif mi >= 1:
    print(f'Teve o cadastro de {mi} pessoas maiores de 18 anos.')
    sleep(0.5)
elif mi == mmi == 0 and t >= 1:
    print('Teve o total de 0 pessoas maiores de 18 anos.')
elif mmi >= 1:
    print(f'Teve {mmi} cadastro de mulheres menores de 20 anos.')
    sleep(0.5)

elif t == hc == mc == mi == mmi == 0:
    print('Você não cadastrou ninguem.')
    sleep(1)
print('Agradeço a escolha como analisador.')
