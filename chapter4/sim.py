# -*- coding: utf-8 -*-
"""
Simulates new data series with similiar values to Methode A.

@author: cldio
"""

import numpy as np
from pandas import Series
from scipy.stats import norm

# Ensure randomness is reproducable
np.random.seed(17)

for i in range(5):
    random_vars = norm.rvs(size=6, loc=80, scale=0.02)
    methodeA_sim1 = Series(np.round(random_vars, 2))

    print("Mean:", methodeA_sim1.mean())
    print("Std:", methodeA_sim1.std())