palavras =('aprender','programar','linguagem','python','curso','futuro','pituca','mercado',
           'tico','kamen','rider')

for p in palavras:
    print(f'\nNa palvra {p.upper()} temos: ', end ='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')