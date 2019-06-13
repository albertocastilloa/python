#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:26:19 2019

@author: albertocastillo
"""

import pandas as pn
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df = pn.read_csv("Spent.csv")
print(df.head())

#sns.barplot(data=df, x="Concentrado", y="Monto", hue="Nombre", estimator=np.median)
#sns.barplot(data=df, x="Concentrado", y="Monto", hue="Nombre", estimator=len)
sns.barplot(data=df, x="Nombre", y="Monto", hue="Concentrado")
plt.show()