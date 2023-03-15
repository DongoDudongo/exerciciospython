print('-=-'*30)
print('Digite uma expressão númerica com parenteses,')
print('irei verificar se os mesmos estão corretos.')
print('-=-'*30)
expr = str(input('Digite uma expresão:'))
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('Sua expressão é Válida!')
else:
    print('Sua expressão não é válida!')