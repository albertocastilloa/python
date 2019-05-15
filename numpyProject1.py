import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')
#print("Complete CSV:")
#print(recipes)
#print("==============")
eggs = recipes[:,2]
#print("Eggs => ", eggs)
cookies = recipes[2,:]
#print("Cookies => ")
#print(cookies)

double_batch = cookies * 2
#print(double_batch)

grocery_list = cookies + double_batch
print(grocery_list)