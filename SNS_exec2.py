#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:22:27 2019

@author: albertocastillo

Propose: Create a script to plot gradebook from csv file.
Libraries: Pandas, Matplotlib, Seaborn
Seaborn: ci= "sd" Means standard deviation for Error bars presented into a plot
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

gradebook = pd.read_csv("gradebook.csv")
sns.barplot(data=gradebook, x="assignment_name", y="grade", ci="sd", estimator=np.median)
plt.show()