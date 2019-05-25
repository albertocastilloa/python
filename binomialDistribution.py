#import codecademylib
import numpy as np
from matplotlib import pyplot as plt


emails = np.random.binomial(500, 0.05, size=1000)

plt.hist(emails, range(0,525), bins=100, normed=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc=2)
plt.show()