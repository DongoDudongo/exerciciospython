from datetime import date
trabalhador = {}
ano = date.today().year

trabalhador['nome'] =str(input('Nome:'))
trabalhador['sexo'] = str(input('Sexo:')).strip().upper()[0]
trabalhador['ano'] = int(input('Ano de nascimento:'))
trabalhador['clt'] = int(input('Número da carteira (0 não tem):'))
if trabalhador['clt'] == 0:
    print('-='*30)
    for k,v in trabalhador.items():
        print(f'    -{k} tem o valor de {v}.')
else:
    trabalhador['ac'] = int(input('Ano que foi contratado:'))
    trabalhador['salario'] = float(input('Salário:'))
    if trabalhador['sexo'] in 'M':
        trabalhador['aposentadoria'] = 66 - ( ano - trabalhador['ac'])
    else:
        trabalhador['aposentadoria'] = 60 - (ano - trabalhador['ac'])
    print('-='*30)
    for k,v in trabalhador.items():
        print(f'    -{k}tem valor de {v}.')