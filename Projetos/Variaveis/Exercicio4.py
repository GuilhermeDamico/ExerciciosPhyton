limiar = 5

menores = [] # Nova lista
maiores = []

# divisão de numeros de 1 a 10 em maiores e menores

for i in range(10):
    if (i < limiar):
        menores.append(i)
    elif (i > limiar):
        maiores.append(i)

print ('Resultado')
print ('Menores', menores)
print ('Maiores', maiores)