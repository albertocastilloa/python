import codecademylib
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
y_lower = [0.9 * i for i in revenue]
y_upper = [1.1 * i for i in revenue]
ax = plt.subplot()
plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.plot(months, revenue)
ax.set_xticks(range(12))
ax.set_xticklabels(month_names)
plt.show()