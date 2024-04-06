"""

Basic operations with rows and columns

>>> import numpy as np
>>> a = np.arange(12)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> type(a)
<class 'numpy.ndarray'>
>>> a.shape
(12,)
>>> a.shape = 3, 4
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[2]
array([ 8,  9, 10, 11])
>>> a[2,0]
8
>>> a[:,1]
array([1, 5, 9])
>>> a.shape = 4, 3
>>> a
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
>>> a.shape = 6, 2
>>> a
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> a.transpose()
array([[ 0,  2,  4,  6,  8, 10],
       [ 1,  3,  5,  7,  9, 11]])
       
Loading, saving and operating on all elements

>>> floats = np.loadtxt('floats.txt')
>>> floats[-3:]
array([ 3454.5466454 ,   224.4334334 , -3124.43434875])
>>> floats *= .5
>>> floats[-3:]
array([ 1727.2733227 ,   112.2167167 , -1562.21717438])
>>> from time import perf_counter as pc
>>> floats /= 3
>>> floats[-3:]
array([ 575.75777423,   37.40557223, -520.73905813])
>>> np.save('floats.npy', floats)
>>> floats_loaded = np.load('floats.npy', 'r+')
>>> floats_loaded[-3:]
memmap([ 575.75777423,   37.40557223, -520.73905813])
"""
