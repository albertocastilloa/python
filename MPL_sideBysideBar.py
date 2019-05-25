import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#First bar
n = 1 #Number of dataset (1 of 2)
t = 2
d = len(sales1)
w = 0.8
store1_x = [t*x + w*n for x in range(d)]
plt.bar(store1_x,sales1)

#Second bar
n = 2
t = 2
d = len(sales2)
w = 0.8
store2_x = [t*x + w*n for x in range(d)]
plt.bar(store2_x, sales2)
plt.show()