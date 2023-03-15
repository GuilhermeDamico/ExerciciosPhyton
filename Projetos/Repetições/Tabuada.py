tab = int(input("Digite o numero para a tabuada:"))
print("Tabuada do numero", tab)

for numero in range (1, 11, 1):
    print(str(tab) + " x " + str(numero) + " = " + str((tab * numero)))