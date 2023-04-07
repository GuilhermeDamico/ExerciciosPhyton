# Sintaxe

# lambda argumentos: <expressao>

# Declaração de função explicita

def area_quadrado(lado):
    return lado * lado

# Declaracao em lambda

area_quad = lambda lado: lado * lado
area_tri = lambda  base, altura: (base * altura)/2
triplo = lambda x: x*3

# Uso da função

print ('Area do quadrado: ', area_quad (4))
print ('Area do triangulo: ', area_tri(10,20))
lista = [4, 5 , 10, 22, 63]
print(list(map(triplo,lista))) # Função 'map', mapeia uma função.

# Uso da função lambda sem declaracao necessaria

print(list(map(lambda x: x ** 3, [4, 5, 10, 22, 63])))
