"""
SRC: ChatGPT + https://realpython.com/python-dicts/

Dictionaries:
-   Dictionaries are collections of key-value pairs. They are unordered, mutable,
    and each key within a dictionary must be unique.
-   Use dictionaries when you need to associate values with keys for efficient
    retrieval based on those keys.
-   Dictionaries are commonly used for representing data in a structured way,
    such as storing user information (username, email, etc.), or for representing
    relationships between objects.

>>> my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

>>> my_dict['name']
'John'

>>> my_dict['age'] += 1
>>> my_dict['age']
31

>>> del(my_dict['city'])
>>> my_dict
{'name': 'John', 'age': 31}


>>> another_dict = dict(name='James', age=35, city='Toronto')
>>> another_dict
{'name': 'James', 'age': 35, 'city': 'Toronto'}


Almost any type of value can be used as a dictionary key in Python
while it is immutable

>>> foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
>>> foo
{42: 'aaa', 2.78: 'bbb', True: 'ccc'}

>>> d = {int: 1, float: 2, bool: 3}
>>> d
{<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}
>>> d[float]
2

>>> d = {bin: 1, hex: 2, oct: 3}
>>> d[oct]
3

>>> d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
>>> d[(1,1)]
'a'
>>> d[(2,1)]
'c'

Mutable (e.g. lists) cause TypeError as they can't be hashed:
>>> try:
...     d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
... except TypeError as exc_info:
...     print(exc_info)
...
unhashable type: 'list'


d.update(<obj>)

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d2 = {'b': 200, 'd': 400}
>>> d1.update(d2)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}


>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update(b=200, d=400)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}


"""