# Modulo Math - Funções matematicas

import math

print ('Função cosseno: ', math.cos(100))
print ('Função log: ', math.log(10))

# Modulo itertools - Construção de sequencias elaboradas

import itertools

# (conjunto entre elementos)

print(list(itertools.combinations([0,1,2,3,4], 2))) # combinação de 2 em 2

print(list(itertools.permutations(['a', 'b', 'c'], 2))) # permutação de 2 em 2

# Modulo datetime - Manipulação de timestamps

from datetime import datetime, timedelta
print ('Datetime atual: ', datetime.now())

print ('Datetime após 7 dias: ', datetime.now() + timedelta(days=7))

# Modulo Random - numeros e sequencias randomicas

import random
print ('Numero aleatorio entre 0 e 1:', random.random())
print('Numero inteiro entre 50 e 100:', random.randint(50,100))

# modulo os - Funcionalidades do sistema operacional

import os

os.mkdir('pasta') # criar um diretorio 'pasta'

nome_pasta = 'pasta'
print('Caminho completo:', os.path.join('/home/guilherme', nome_pasta, 'arquivo.txt'))

f'/home/guilherme/{nome_pasta}/arquivo.txt'