"""
# SRC: ChatGPT

Lists:
-   Lists are ordered collections of items, and they are mutable, meaning
    you can change the contents after creation.
-   Use lists when you need an ordered collection of items and you may need
    to add, remove, or modify elements frequently.
-   Lists are commonly used for storing homogeneous items (items of the same type)
    or heterogeneous items (items of different types) where the order of elements matters.

>>> my_list = [1, 2, 3, 4, 5]
>>> my_list
[1, 2, 3, 4, 5]

>>> my_list.append(0)
>>> my_list
[1, 2, 3, 4, 5, 0]

>>> my_list.append(0)
>>> my_list
[1, 2, 3, 4, 5, 0, 0]

>>> my_list.remove(3)
>>> my_list
[1, 2, 4, 5, 0, 0]

>>> my_list.remove(0)
>>> my_list
[1, 2, 4, 5, 0]

>>> my_list.append(4)
>>> my_list
[1, 2, 4, 5, 0, 4]

>>> my_list.remove(4)
>>> my_list
[1, 2, 5, 0, 4]

>>> my_list[2]
5
>>> my_list[2]=10
>>> my_list
[1, 2, 10, 0, 4]
"""