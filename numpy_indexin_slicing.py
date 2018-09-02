# -*- coding: utf-8 -*-
import numpy as np

a = np.array([1,2,3,4,5,6,7])
print a[0:4]
reverse_a = a[::-1] # Array'i tersten sıralar.
print reverse_a

b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print b[1,1]
print b[:,1]
print b[1,1:4]
print b[-1,:]
print b[:,-1]