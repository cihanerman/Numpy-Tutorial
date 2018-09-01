# -*- coding: utf-8 -*-
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print a
print a.shape
b = a.reshape(3,5)
print b
print b.shape
print b.ndim
print b.dtype.name
print b.size
print type(b)
print np.zeros((3,4))
print np.ones((3,4))
print np.empty((3,4))
c = np.arange(1,15,1.25)
print c
print np.linspace(10,50,20)