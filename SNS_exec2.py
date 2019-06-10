#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:22:27 2019

@author: albertocastillo
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


gradebook = pd.read_csv("gradebook.csv")
assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]

print(assignment1)

asn1_median = np.median(assignment1["grade"])
print(asn1_median)