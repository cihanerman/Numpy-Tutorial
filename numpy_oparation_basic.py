# -*- coding: utf-8 -*-
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print a + b
print a - b
print a ** 2

print np.sin(a)
print a < 2

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print a * b
print a.dot(b.T)
print np.exp(a)

c = np.random.random((5,5))
print c
print c.sum()
print c.max()
print c.min()
print c.sum(axis=0)
print c.sum(axis=1)
print np.sqrt(c)
print np.square(c)

np.add(c,c)
print c