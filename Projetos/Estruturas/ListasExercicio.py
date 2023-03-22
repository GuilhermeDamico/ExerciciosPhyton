# Lista para 3 idades

idades = [19, 22, 54, 78, 21, 12, 99]

# Selecionar uma idade

maior_idade = idades[0]

# Percorrer a lista verificando a maior idade

for cont in idades:
    if cont > maior_idade:
        maior_idade = cont

print ('Maior idade é ', maior_idade)

# Adicionar um elemento na lista: Método append (Final da lista)
idades.append(112)

# Alterar o valor de um elemento
idades [6] = 11
idades [3] = idades [3] + 4

# Remover valor primeira ocorrencia
idades.remove(22)

# Operações de concatenação, repetição e filiação
# print (idades + outra lista)
print (idades * 2)
print (22 in idades)

# Funções uteis
# len: quantidade de elementos na lista
print (len(idades))

# sum: soma dos elementos
print (sum(idades))

# max: maior elemento
print (max(idades))

# Metodos para alterar valores
idades.reverse() #inverte a ordem

idades.extend([24,42,91]) #adiciona os elementos na lista

idades.sort() # ordenar valores

idades.insert (2, 'novo valor') # Adiciona um elemento em um indice especifico

idades.pop() # remove o ultimo elemento

# idades.clear() # limpa a lista

# Metodos para retorno de valor, sem alteração

print(idades.index(19)) # primeira ocorrencia do valor

print(idades.count(21)) # conta as ocorrencias do valor