import numpy as np

a = np.random.binomial(10, 0.30, size=100)

b = np.std(a)
print(b)
print("<=========>")
print(a)