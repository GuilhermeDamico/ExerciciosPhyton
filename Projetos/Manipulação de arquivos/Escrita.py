# Adicionar informação no arquivo

arquivo = open ('cidades.txt', 'a')
arquivo.write ('RJ ; São Gonçalo; 1031903\n')
arquivo.close()

# Adicionar varias linhas ao arquivo

linhas = [
    'AL; Maceió; 1005319\n'
    'RJ; Duque de Caxias; 878402\n'
]
arquivo = open ('cidades.txt', 'a')
arquivo.writelines(linhas)
arquivo.close()