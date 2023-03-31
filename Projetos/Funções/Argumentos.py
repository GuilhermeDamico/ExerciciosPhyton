# Declaração explicita

# (argumento = variavel, ...)

# Argumento padrão (Default)

def exibe_pessoa (nome, idade = 30):
    print(f'Meu nome é {nome} e tenho {idade} anos.')

print(exibe_pessoa('Guilherme'))

print(exibe_pessoa('Guilherme', 52))