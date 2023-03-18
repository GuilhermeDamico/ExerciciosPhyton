# Utilização de Range para especificar uma faixa de valores e como será incrementada.
# range (inicio, fim, incremento)

print (list(range(1, 20, 3)))


for numero in range (1,int(input("Digite um numero para determinar o fim: ")),1):
    print ("  " + str(numero))

# Utilização de while ideal para momentos de preenchimento onde não sabemos o numero exato de execuções.
# Utilização de for para repetições pré-determinadas ou informadas pelo usuario.