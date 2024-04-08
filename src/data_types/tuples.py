"""
SRC: ChatGPT + https://realpython.com/python-lists-tuples/#python-tuples

Tuples:
-   Tuples are ordered collections of items, similar to lists,
    but they are immutable, meaning you cannot change their contents after creation.
-   Use tuples when you need an ordered sequence of elements that
    should not be changed, such as coordinates, database records,
    or any other immutable sequences.
-   Tuples are typically used in situations where you want to ensure
    that the data remains constant throughout the program execution.

    
>>> t = ()
>>> type(t)
<class 'tuple'>

>>> t = 5,
>>> type(t)
<class 'tuple'>
>>> t
(5,)

>>> t = (1, 2)
>>> type(t)
<class 'tuple'>



>>> t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
>>> try:
...     t[2] = 'Bark!'
... except TypeError as exc_info:
...     print(exc_info)
...
'tuple' object does not support item assignment


Tuple unpacking
>>> t = ('James', 'Johnson', 'Toronto', 32, '+1.416.227.3451')

>>> first_name, last_name, city, *_ = t
>>> first_name
'James'
>>> last_name
'Johnson'
>>> city
'Toronto'
>>> _
[32, '+1.416.227.3451']
"""