n = 0

while True:
     n = int(input('Quer ver a tabuada de qual número?'))
     if n < n:
          break
     print('-=-' * 30)
     for c in range(1,11):
          print(f'{n} X {c} = {n * c}')
     print('-=-' * 30)
print('fim do programa')