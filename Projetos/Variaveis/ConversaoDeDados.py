idade = 30
saida = 'Eu tenho ' + str(idade) + ' anos'
print (saida)

saida2 = str(idade)
print (int(saida2) - 3)

# Conversão do tipo int
print (float(10))
print(bool(0)) # Diferente de 0 será True

# Conversão do tipo float
print (int(9.99))
print (bool(-0.99))

#  Conversão do tipo bool
print (int(True)) # Igual a 1 ou 0
print (float(False))
print (str(True))

# Conversão string
print (int ('-99'))
print (float ('0.01'))
print (bool ('')) # Palavra vazia é false
print (int(float('1.99'))) # Separador decimal, sempre '.'

#  Tipo None é só convertido em str ou bool
print (str(None))
print (bool(None))

# Formatação com f-strings
variavel = 5
f'Teste de f-string com valor {variavel} e uma expressão {10 == 15}'

print(f'Eu tenho {variavel} anos')
print(f'Eu tenho {idade - variavel} anos')
print(f'{saida.upper()}')
print(f'Eu tenho {idade - variavel} anos')

# Utilização de .f para casas decimais após o float.
# Utilização de .% para amostragem como porcentagem.