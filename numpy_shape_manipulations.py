# -*- coding: utf-8 -*-
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a.ravel()
print a
print b
c = b.reshape(3,3) # array'i değiştirmiyor
print c
print c.T
d = np.array([[1,2],[3,4],[5,6]])
print d.reshape(2,3)
print d
d.resize(2,3) # array'i değiştiriyor
print d