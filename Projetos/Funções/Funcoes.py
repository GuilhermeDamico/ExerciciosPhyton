# def nome_da_funcao (argumento1, argumento2, ...):
#     <bloco de código>
#     return resultado

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 1, 5, 7, 0]
lista_3 = [22, 11, 54, 32]

soma_1 = 0
for item in lista_1:
    soma_1 = soma_1 + item

soma_2 = 0
for item in lista_2:
    soma_2 = soma_2 + item

soma_3 = 0
for item in lista_3:
    soma_3 = soma_3 + item

print (f'Resultado: lista 1 = {soma_1}, lista 2 = {soma_2}, lista 3 = {soma_3}')


# Função para realizar o procedimento de soma acima

def funcao_soma (lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

# chamada da função

# lista_1 = funcao_soma(lista_1)
# lista_2 = funcao_soma(lista_2)
# lista_3 = funcao_soma(lista_3)


# print(f'\n Resultado das 3 listas: {lista_1, lista_2, lista_3}')

# Função multi

def funcao_mult (lista):
    mult = 1
    for item in lista:
        mult = mult * item
    return mult

# Chamada da função

lista_1 = funcao_mult(lista_1)

print (f'Multiplicação da lista 1 = {lista_1}')