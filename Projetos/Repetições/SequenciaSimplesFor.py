#

numero = '2941'
soma = 0

for c in numero:
    print (c)
    soma = soma + int(c)

print (f'Resultado da soma dos numeros é {soma}')

#

palavra = 'argentina'
contador = 0
contadorE = 0

for letra in palavra:
    if letra == 'a':
        contador = contador + 1
    if letra == 'e':
        contadorE = contadorE + 1


print(f'A palavra {palavra} possui {contador} letras a, e possui {contadorE} letras e.')

#

for num in range(220, 300):
    if num % 21 == 0:
        print('Numero encontrado', num)
        break # Se a condição for localizada, irá interromper a busca.

