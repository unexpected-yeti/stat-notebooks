# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:01:58 2019

@author: cldio
"""

from pandas import Series
import numpy as np

methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03,
80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])

print("Mean:", methodeA.mean())
print("Std:", methodeA.std())

# Problem: Andere Messreihen haben andere Schätzwerte

