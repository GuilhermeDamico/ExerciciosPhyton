nome = input("Digite um funcionario: ")
empresa = input("Digite uma empresa: ")
quantidade_funcionarios = int(input("Digite a quantidade de funcionarios: ")) #input captura apenas string, sendo necessaria a conversão.
mediaArmazenamento = float(input("Digite o armazenamento das maquinas: "))

print(nome + " trabalha na empresa " + empresa) # concatenação para string
print("Possui: ", quantidade_funcionarios, " funcionarios.") #final do texto sem converter int em string.
print("O armazenamento das maquinas é de: " + str(mediaArmazenamento)) #Para não considerar operação matematica é usado o "str()", transforma o valor de float em string.

print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [quantidade_funcionarios] é: ", type(quantidade_funcionarios))
print("O tipo de dado da variavel [mediaArmazenamento] é: ", type(mediaArmazenamento))
