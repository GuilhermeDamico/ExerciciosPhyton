# Sintaxe basica da função

## {chave: valor for item in sequencia}

# Todos os numeros elevados a 2

#  dict_todos = {}
#  for item in range(1, 11):
#      dict_todos[item] = item ** 2
#  print(dict_todos)

# Função com dict comprehension

dict_todos = {item: item ** 2 for item in range(1, 11)}
print (dict_todos)

# Função com apenas numeros impares

dict_impares = {}
for item in range (1, 11):
    if item % 2 != 0:
        dict_impares[item] = item ** 2
print('Numeros impares: ', dict_impares)

# Função impares com comprehension

dict_impares = {item: item ** 2 for item in range (1, 11) if item % 2 != 0}
print('Numeros impares: ', dict_impares)