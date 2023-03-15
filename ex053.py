frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto ='' .join(palavras)
inverso = ''
#inverso =junto[::] -> se usar esse comando vc elimina a linha de cima e de baixo,tornando o "fro" desnecessário

for letra in range (len(junto) - 1, - 1 , -1):
    inverso += junto[letra]
print(junto,inverso)
if inverso == junto:
    print(' é um palindromo')
else:
    print('não é um palindromo')