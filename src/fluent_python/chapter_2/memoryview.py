"""
Handling 6 bytes (typecode 'B') of memory 
as 1x6, 2x3 and 3x2 views
>>> from array import array
>>> octets = array('B', range(6))
>>> m1 = memoryview(octets)
>>> m1.tolist()
[0, 1, 2, 3, 4, 5]
>>> m2 = m1.cast('B', [2, 3])
>>> m2.tolist()
[[0, 1, 2], [3, 4, 5]]
>>> m3 = m1.cast('B', [3, 2])
>>> m3.tolist()
[[0, 1], [2, 3], [4, 5]]
>>> m2[1,1] = 22
>>> m3[1,1] = 33
>>> octets
array('B', [0, 1, 2, 33, 22, 5])
"""

"""
Changing the value of 16-bit integer (bytecode 'h')
array item by poking one of its bytes
>>> numbers = array.array('h', [-2, -1, 0, 1, 2])
>>> numbers
array.array('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview(numbers)
>>> len[memv]
5
>>> memv[0]
-2
>>> memv_oct = memv.cast('B')
>>> memv_oct.tolist()
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
>>> memv_oct[5]
0
>>> memv_oct[5] = 4
>>> memv_oct[5]
4
>>> numbers
array.array('h', [-2, -1, 1024, 1, 2])
"""