palavra = 'Hospital'
palavra2 = 'Azul'
palavra3 = 'tal'

# Listar indice positivo
print ('Primeiro caracter', palavra[0])

# Listar indice negativo
print ('Ultimo caracter0', palavra[-1])

# Intervalo

print (palavra[3:7])

# Concatenação

palavra2 = 'Azul'
print (palavra , palavra2 * 2)

# Filiação

print (palavra2 in palavra)
print (palavra3 in palavra)
print ('tal' not in palavra2)

# len - tamanho

print (len(palavra))

# Outros metodos
# .upper() - Letras Maiusculas
# .lower() - Letras Minusculas
# .title - Letra inicial da palavra maiuscula

# var.replace('X' , 'Y') - Substituição de palavra
# .startswitch('x') - Verifica se a string começa com X
# .endswitch('x') - Verifica se termina com x
# .find ('') - retorna o indice da primeira ocorrencia da palavra
# .split() - particiona a string em outras, que são separadas por espaço
# .split (',') - particiona a string em outras, que são separadas por ,

# .strip () - remove espaços extras no inicio e fim da string