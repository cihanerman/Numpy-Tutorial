# -*- coding: utf-8 -*-
import numpy as np

liste = [1,2,3] # list
a = np.array(liste) # np.array
liste2 = list(a) # list

b = a # referans tutyorlar
c = a
print a
print b
print c
b[0] = 5
print a
print b
print c

d = a.copy() # memoryde yeni bir örneğini oluşturuyor.
f = a.copy()

print a
print d
print f
d[0] = 6
print a
print d
print f