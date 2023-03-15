def leiaint(msg):
    while True:

        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO:Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mErro: Digite um valor real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

num = leiaint('Digite um valor inteiro:')
num2 = leiafloat('Digite um valor real:')
print(f'O valor inteiro foi {num} e o valor real foi {num2}.')