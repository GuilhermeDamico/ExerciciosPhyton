# Conjunto Homogeneos e Heterogeneo

conjunto1 = {3, 0, 6, 5, 3, 2, True}
print (conjunto1)

conjunto2 = {2, 'b', 4.21, True, None}
print (conjunto2)

# Operações

print('Conjunto 1:', conjunto1)

# União (A u B)

print (' A | B => ', conjunto1|conjunto2)
print ('A.union(B) => ', conjunto1.union(conjunto2))

# Interseção ( A B )

print ('A & B =>', conjunto1 & conjunto2)
print ('A.intersection(B) =>', conjunto1.intersection(conjunto2))

# Diferença ( A - B )

print ('A - B =>', conjunto1 - conjunto2)
print ('A.difference(B) =>', conjunto1.difference(conjunto2))

# Adicionar um elemento ao conjunto

conjunto1.add(32)
print (conjunto1)

# Adicionar elementos de uma sequencioa iterável

conjunto1.update([6,25,92])
print (conjunto1)

# Descartar um elemento do conjunto, *não gera erro mesmo o elemento não existindo.

conjunto1.discard(5)
print(conjunto1)

# Verifica se os conjuntos são disjuntos (não possuem elementos em comum)

print (conjunto1.isdisjoint((conjunto2)))

# Verificar se o conjunto é subconjunto de outro

print((conjunto1.issubset(conjunto2)))

# Verificar se o conjunto contem outro conjunto

print(conjunto1.issuperset(conjunto2))