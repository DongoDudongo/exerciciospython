a = input('digite algo:')

print('o tipo primitico é', type(a))

print('só tem espaços:',a.isspace())
print('é um número?',a.isnumeric())
print('é uma letra?',a.isalpha())
print('é alfanúmerico?',a.isalnum())
print('Está em maiusculo?',a.isupper())
print('está em minusculo?',a.islower())
print('está capitalizada?',a.istitle())