# Boas vindas

def boas_vindas(nome):
    print(f'Olá {nome}. Seja bem-vindo (a)!')

# Area de um quadrado

def area_quadrada(lado):
    return lado * lado

# Area de triangulo

def area_triangulo (base, altura):
    return (base * altura)/2

# Divisão

#def div (dividendo, divisor):
#    if divisor == 0:
#        print ('Erro: Divisor igual à zero!')
#
#    return dividendo / divisor

# Divisão e resto

#def div_qr(dividendo, divisor):
#    if divisor == 0:
#        print('Erro: Divisor igual à zero!')
#        return
#    quociente = dividendo // divisor
#    resto = dividendo % divisor
#    return (quociente, resto)


# Chamadas das funções

boas_vindas('Guilherme')

print (area_triangulo(4, 5))

print (area_quadrada(10))

#print (div(33,2))

#print (div_qr(26, 3))

# Atribuir os valores da função

#quociente, resto = div_qr(26,3)
#print(type(quociente), type(resto))

# Utilizando função dentro da função

def divisor_invalido(divisor):
    if divisor == 0:
        print ('Erro: Divisor igual a zero!')
        return True
    return False

def div(dividendo, divisor):
    if divisor_invalido(divisor):
        return
    return dividendo / divisor

def div_qr (dividendo, divisor):
    if divisor_invalido(divisor):
        return
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return (quociente, resto)

print(f'{div (10,0)}')