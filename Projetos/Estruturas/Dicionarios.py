# Sintaxe de criação de dicionario

# {chave:valor, chave2:valor2...}

# Meu teste

dicionario = {'Nome' : 'Guilherme', 'Idade' : '30', 'Sexo' : 'Masculino', 'Altura' : 1.71, 'Oculos' : True}
print (dicionario)

# Acesso ao dicionario

print (dicionario['Altura'])

print (f'\nMeu nome é {dicionario["Nome"]} e tenho {dicionario["Idade"]} anos.')

# Atualização de chave

dicionario['Idade'] = '31'
print(dicionario['Idade'])

# Adicionar chave

dicionario['Curso'] = 'Phyton'
# dicionario.update({'Curso' : 'Phyton', 'Pais' : 'Brasil'})
print(dicionario)

# Encontrar maior e menor chave
print (max(dicionario), min(dicionario))

# Localizar chave (in)

print ("A chave 'Nome' está no dicionario? ", 'Nome' in dicionario)

# Remover o elemento

dicionario.pop('Curso')

# Iteração

for key in dicionario:
    if key == 'Sexo':
        print (dicionario[key], ' < Chave encontrada!')
        break
    print(dicionario[key])

# Iteração sobre os itens (sum.(dicionario.values())

#soma = 0
#for valor in dicionario.values():
#    soma = soma + valor
#print('Soma: ', soma)



# Iteração sobre os itens (Mostrar)

for key, valor in dicionario.items():
    print (key, valor)