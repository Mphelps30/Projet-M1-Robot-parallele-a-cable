"""
# Giordano Dylan
# M1 EEA
# Code robot parrallele a cable-
"""

import numpy as np
import os
from control.matlab import *
import matplotlib.pyplot as plt
from sympy import symbols

# Déclaration de symboles
a1,a2,a3,a4 = symbols('a1 a2 a3 a4')
b1,b2,b3,b4 = symbols('b1 b2 b3 b4')
l1,l2,l3,l4 = symbols('l1 l2 l3 l4')

A=np.array([a1,a2,a3,a4]) #Drawing points
B=np.array([b1,b2,b3,b4])#attachment points

L=np.array([l1,l2,l3,l4])#Vecteur associé a la longueur des cables

print("la matrice A = \n" , A)
print("\n la matrice B = \n",B)






