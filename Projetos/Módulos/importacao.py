# importar modulos (Preferencia)

import areas

print (areas.triangulo(5, 8))

print (areas.PI)

# importar apenas função

from areas import triangulo

print(triangulo(5,10))

# importar tudo

from areas import *

# importar com substituição de nome

import areas as ar

print(ar.elipse(10,33))
