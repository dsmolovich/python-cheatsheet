"""
SRC: https://realpython.com/python-sets/

Sets:
-   Sets are unordered.
-   Set elements are unique. Duplicate elements are not allowed.
-   A set itself may be modified, but the elements contained in the set must be of an immutable type.
-   Use sets when you need to perform mathematical set operations like union, intersection, difference,
    etc., or when you need to quickly check for membership.


>>> my_set = {1, 2, 4, 5}
>>> my_set
{1, 2, 4, 5}

>>> my_set.add(3)
>>> my_set
{1, 2, 3, 4, 5}

>>> font_test_set = set('quick brown fox jumps over the lazy dog')

number of characters including space
>>> len(font_test_set)
27

>>> font_test_set.add('q')
>>> len(font_test_set)
27

>>> font_test_set.add('Q')
>>> len(font_test_set)
28
>>> 'Q' in font_test_set
True
>>> 'U' in font_test_set
False

Lists and dictionaries are mutable, they can't be set elements
>>> a = ['foo', 'bar', 'baz']
>>> try:
...     {a}
... except TypeError as exc_info:
...     print(exc_info)
... 
unhashable type: 'list'
>>> d = {'a': 1, 'b': 2}
>>> try:
...     {d}
... except TypeError as exc_info:
...     print(exc_info)
... 
unhashable type: 'dict'


Union:
>>> A = {1, 2, 3}
>>> B = {2, 3, 4}
>>> A | B
{1, 2, 3, 4}
>>> A.union(B)
{1, 2, 3, 4}

>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}

>>> a.union(b, c, d)
{1, 2, 3, 4, 5, 6, 7}

>>> a | b | c | d
{1, 2, 3, 4, 5, 6, 7}


Intersection:
>>> A = {1, 2, 3, 4}
>>> B = {2, 3, 4, 5}

>>> A & B
{2, 3, 4}

>>> A.intersection(B)
{2, 3, 4}


>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}

>>> a.intersection(b, c, d)
{4}

>>> a & b & c & d
{4}


Difference:
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.difference(x2) == {'foo', 'bar'}
True

>>> x1 - x2 == {'foo', 'bar'}
True

>>> a = {1, 2, 3, 30, 300}
>>> b = {10, 20, 30, 40}
>>> c = {100, 200, 300, 400}

>>> a.difference(b, c)
{1, 2, 3}

>>> a - b - c
{1, 2, 3}


Symmetric difference:
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

Expected difference is: {'foo', 'qux', 'quux', 'bar'}
Order is not preserved, thus asserting the length
>>> x1.symmetric_difference(x2) == {'foo', 'qux', 'quux', 'bar'}
True

>>> x1 ^ x2 == {'foo', 'qux', 'quux', 'bar'}
True

>>> a = {1, 2, 3, 4, 5}
>>> b = {10, 2, 3, 4, 50}
>>> c = {1, 50, 100}

>>> a ^ b ^ c == {100, 5, 10}
True


Determines whether or not two sets have any elements in common.
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.isdisjoint(x2)
False

>>> x2.remove('baz')
>>> x1.isdisjoint(x2)
True

Determine whether one set is a subset of the other.
x1 <= x2
x1.issubset(x2)

>>> x1 = {'foo', 'bar', 'baz'}
>>> x1.issubset({'qux', 'foo', 'bar', 'baz', 'quux'})
True

>>> x2 = {'baz', 'qux', 'quux'}
>>> x1 <= x2
False


Determines whether one set is a proper subset of the other.
x1 < x2
A proper subset is the same as a subset, except that the sets can’t be identical.
A set x1 is considered a proper subset of another set x2 if every element of
x1 is in x2, and x1 and x2 are not equal.

>>> x1 = {'foo', 'bar'}
>>> x2 = {'foo', 'bar', 'baz'}
>>> x1 < x2
True

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'bar', 'baz'}
>>> x1 < x2
False

>>> x = {1, 2, 3, 4, 5}
>>> x <= x # x is a subset of itself
True
>>> x < x # x is not a proper subset of itself as it is equal to itself :)
False


Determine whether one set is a superset of the other.
x1 >= x2
x1.issuperset(x2)

>>> x1 = {'foo', 'bar', 'baz'}

>>> x1.issuperset({'foo', 'bar'})
True

>>> x2 = {'baz', 'qux', 'quux'}
>>> x1 >= x2
False

>>> x = {1, 2, 3, 4, 5}
>>> x.issuperset(x) # x is a subset of itself
True
>>> x >= x
True

Determines whether one set is a proper superset of the other.
x1 > x2

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'bar'}
>>> x1 > x2
True

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'foo', 'bar', 'baz'}
>>> x1 > x2
False


Modifying a Set
x1 |= x2 [| x3 ...]
x1.update(x2[, x3 ...])

>>> x1 = {'foo', 'bar', 'baz'}

>>> x1.update(['foo', 'corge', 'garply'])
>>> x1 == {'foo', 'bar', 'baz', 'corge', 'garply'}
True


Removes an element from a set.
>>> x = {'foo', 'bar', 'baz'}
>>> x.discard('baz')
>>> x == {'bar', 'foo'}
True

>> x.remove('foo')
{'bar'}
"""