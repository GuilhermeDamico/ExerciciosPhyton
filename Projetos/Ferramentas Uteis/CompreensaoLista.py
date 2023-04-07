# Sintaxe basica da função

## [expr(item) for item in sequencia]

# Numeros elevados a 2

# potencias = []
# for item in range(1, 11):
#  potencias.append(item ** 2)
# print(potencias)

# Realizando o mesmo codigo com list comprehension

potencias = [item ** 2 for item in range(1, 11)]
print (potencias)

# Multiplicação por 10 dos numeros de 1 a 15

var = [n * 10 for n in range (1, 16)]
print (var)

# Cria lista com caracteres maiusculos

letras = [c.upper() for c in 'guilherme']
print (letras)

# Verificador de numero par

par = [(n % 2 == 0) for n in range (0, 10)]
print (par)

# Elevação dos numeros com verificação condicionar de numero impares

potencias = [item ** 2 for item in range (1, 11) if item % 2 != 0]
print (potencias)