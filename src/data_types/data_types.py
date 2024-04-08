"""
Run it as a test (doctest):
    python -m doctest src/data_types.py -v

List:
>>> list_example = ["apple", "banana", "cherry"]
>>> list_example
['apple', 'banana', 'cherry']
>>> type(list_example)
<class 'list'>
>>> list_example = list(("apple", "banana", "cherry"))
>>> list_example
['apple', 'banana', 'cherry']

Tuple:
>>> tuple_example = ("apple", "banana", "cherry")
>>> tuple_example
('apple', 'banana', 'cherry')
>>> type(tuple_example)
<class 'tuple'>
>>> tuple_example = tuple(("apple", "banana", "cherry"))
>>> tuple_example
('apple', 'banana', 'cherry')



Dictionary:
>>> dictionary_example = {"name" : "John", "age" : 36}
>>> dictionary_example
{'name': 'John', 'age': 36}
>>> type(dictionary_example)
<class 'dict'>
>>> dictionary_example = dict(name="John", age=36)
>>> dictionary_example
{'name': 'John', 'age': 36}

Set:
>>> set_example = {"apple", "banana", "cherry"}

Note: an order of elements is not preserved thus
there's a low chance of this test to pass 
>>> set_example == {'cherry', 'apple', 'banana'}
True
>>> type(set_example)
<class 'set'>
>>> set_example = set(("apple", "banana", "cherry"))
"""
