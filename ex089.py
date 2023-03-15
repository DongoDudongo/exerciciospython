test = list()
test.append('gustavo')
test.append(40)
print(test)
galera=list()
galera.append(test[:])
print(galera)
test[0] = 'maria'
test[1]=22
galera.append(test[:])
print(galera)