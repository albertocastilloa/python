#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:47:32 2019

@author: albertocastillo
"""

startGame = True

while startGame:
    counter = int(input("How many numbers: "))
    for i in range(1, int(counter)):
        print(i)
    continueScript = input("Do you want to continue y/n: ")
    if continueScript == "n":
        startGame = False
        