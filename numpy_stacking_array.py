# -*- coding: utf-8 -*-
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[-1,-2],[-3,-4]])

c = np.vstack((a,b)) # vertical birleştirme
print c
d = np.hstack((a,b)) # horizonal birleştirme
print d