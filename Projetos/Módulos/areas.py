# Definir valor de PI

PI = 3.141592

# Calculo area quadrado

def quadrado(l):
    return l ** 2

# Calculo area triangulo

def triangulo (b, h):
    return (b * h)/2

# Calculo area circulo

def circulo(r):
    return PI * (r ** 2)

# Calculo area elipse
def elipse (a, b):
    return PI + a + b

# Calculo area trapezio

def trapezio (B, b, h):
    return (B + b) * h /2