# Criação de listas de alunos

ingles = {'Gabriel', 'Caio', 'João', 'Ana', 'Bruna'}
espanhol = {'Caio', 'Bruna', 'Maria', 'Paula', 'Beatriz'}
frances = {'Bruna', 'Henrique', 'Maria', 'Gustavo'}

# Concatenação geral (Lista)

# todos = ingles + espanhol + frances
# print ('Nome de todos alunos: ', todos)

# Ordenação

# todos.sort()
# print('Nomes ordenados:', todos)

# Alunos sem repetição (Tuplas - União)

# todos = ingles | espanhol | frances
# print('Nomes dos alunos sem repetição:', todos)

# Alunos que estão matriculados em mais de uma turma (Interseções)

todos = (ingles & espanhol) | (ingles & frances) | (espanhol & frances)
print ('Alunos matriculados em mais de uma materia: ', todos)