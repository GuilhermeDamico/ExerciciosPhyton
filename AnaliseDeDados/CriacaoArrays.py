import numpy as np

# Criação de um array 1D

l = [1, 2, 3]
x = np.array(l)
print ("x: ", x)
print ("Shape: ", x.shape)

# Criação de um array 2D

m = [[1,2], [3, 4]]
y = np.array((m))
print("x:\n", y)
print("Shape:", y.shape)

# Criação de arrays zerados

dim = (2, 2)
x = np.zeros(dim)
print ("x:\n", x)
print ("Shape: ", x.shape)

# Criação de arrays de '1'

n = (2,2)
u = np.ones(n)
print ("x: \n", u)
print ("Shape: ", u.shape)

# Criação de valores em intervalos (Uniformes)

x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6) # (Max, Min, espaçamento)
print ("x:", x)
print ("shape:", x.shape)

# Criação e matriz identidade

n = 4
x = np.eye(n)
print("x:\n", x)
print("Shape:", x.shape)

# Criação com valores aleatorios

x = np.random.random(size=(2,3))
print ("x: \n", x)
print("Shape:", x.shape)