# -*- coding: utf-8 -*-
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print a
print a.shape
b = a.reshape(3,5) # matris shape'i değiştirir var olan array'i etkilemez.
print b
print b.shape
print b.ndim
print b.dtype.name
print b.size
print type(b)
print np.zeros((3,4)) # 0'lardan oluşan 3'e 4'lük matris verir.
print np.ones((3,4)) # 1'lardan oluşan 3'e 4'lük matris verir.
print np.empty((3,4)) # Boş 3'e 4'lük matris verir.
c = np.arange(1,15,1.25) # 1'den 15'e kadar 1.25 toplayarak bir array oluşturur.
print c
print np.linspace(10,50,20) # 10 ile 50 dahil iki sayınında dahil olduğu 20 sayılı bir array oluşturur.