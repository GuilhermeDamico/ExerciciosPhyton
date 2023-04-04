# Modo somente leitura

arquivo = open('arquivo_somente_leitura.txt', 'r')
arquivo.close() # Encerrar o arquivo

# Modo de escrita. Cria ou substitui.

arquivo = open ('valores.txt', 'w')
arquivo.close()

# Modo de escrita. Cria ou retorna erro.

arquivo = open ('valores.txt', 'x')
arquivo.close()

# Modo de escrita. Cria ou adiciona novas linhas ao fim do arquivo.

arquivo = open ('valores.txt', 'a')
arquivo.close()