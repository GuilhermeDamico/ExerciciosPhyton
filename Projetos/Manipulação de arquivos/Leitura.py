# Leitura de arquivo e armazenamento do conteudo

arquivo = open('cidades.txt', 'r')
linhas = arquivo.read()
arquivo.close()
print (linhas)

# Leitura de arquivo e armazenamento de linhas (Lista)

arquivo = open('cidades.txt', 'r')
linhas = arquivo.readlines() # Lista de strings
arquivo.close()
print (linhas)

# Removendo a quebra de linha

novas_linhas = []
for linha in linhas:
    novas_linhas.append(linha.rstrip())
print (novas_linhas)

# Outra opção para leitura individual

arquivo = open('cidades.txt', 'r')
for linha in linhas:
    print (linha.rstrip()) # Removendo quebra de linha
arquivo.close()

#

arquivo = open('cidades.txt', 'r')
soma = 0
for linha in arquivo:
    cidade = linha.split(' ')
    populacao = int(cidade[-1])
    print (populacao)
    soma = soma + populacao
arquivo.close()
print ('Total da soma de população: ', soma)