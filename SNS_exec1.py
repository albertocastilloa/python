import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("myCSV.csv")
print(df)

#Plot using Seaborn
sns.barplot(data=df, x="Gender", y="Mean Satisfaction")
plt.show()



#Example of plotting using matplotlib
"""ax = plt.subplot()
plt.bar(range(len(df)), df["Mean Satisfaction"])
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df.Gender)
plt.xlabel("Gender")
plt.ylabel("Mean Satisfaction")"""
