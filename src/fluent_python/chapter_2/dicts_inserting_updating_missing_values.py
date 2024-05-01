"""
echo "python -c 'import this' > zen.txt" > zen.txt
echo "=================================" >> zen.txt
python -c 'import this' >> zen.txt


>>> def print_index(index):
...     for word in sorted(index, key=str.upper):
...         print(word, index[word])

>>> import re
>>> import sys
>>> WORD_RE = re.compile(f'\w+')

#================================
# Option 1 (ugly):
>>> index = {}
>>> with open('zen.txt', encoding='utf-8') as fp:
...     for line_no, line in enumerate(fp, 1):
...         for match in WORD_RE.finditer(line):
...             word = match.group()
...             column_no = match.start() + 1
...             location = (line_no, column_no)
...             # UGLY:
...             occurences = index.get(word, [])
...             occurences.append(location)
...             index[word] = occurences

>>> print_index(index) #doctest: +ELLIPSIS
a [(21, 48), (22, 53)]
Although [(13, 1), (18, 1), (20, 1)]
...
Zen [(3, 5)]

#================================
# Option 2, using dict's setdefault() method:
>>> index = {}
>>> with open('zen.txt', encoding='utf-8') as fp:
...     for line_no, line in enumerate(fp, 1):
...         for match in WORD_RE.finditer(line):
...             word = match.group()
...             column_no = match.start() + 1
...             location = (line_no, column_no)
...             # BETTER:
...             # get the list of occurences for word
...             # or set it to [] if not found
...             index.setdefault(word, []).append(location)

>>> print_index(index) #doctest: +ELLIPSIS
a [(21, 48), (22, 53)]
Although [(13, 1), (18, 1), (20, 1)]
...
Zen [(3, 5)]


#================================
# Option 3, using collections.defaultdict() method that
# handles missing keys automatically:
>>> import collections

>>> # create the defaultdict with list as a default factory:
>>> index = collections.defaultdict(list)

>>> with open('zen.txt', encoding='utf-8') as fp:
...     for line_no, line in enumerate(fp, 1):
...         for match in WORD_RE.finditer(line):
...             word = match.group()
...             column_no = match.start() + 1
...             location = (line_no, column_no)
...             # BETTER:
...             # if word is not in the index the default_factory is called
...             # to produce a missing value 
...             index[word].append(location)

>>> print_index(index) #doctest: +ELLIPSIS
a [(21, 48), (22, 53)]
Although [(13, 1), (18, 1), (20, 1)]
...
Zen [(3, 5)]


>>> from unittest.mock import Mock
>>> class my_dict(dict):
...     DEFAULT_VALUE_FOR_MISSING_KEY = Mock()
...     def __missing__(self, key: str):
...         self[key] = self.DEFAULT_VALUE_FOR_MISSING_KEY 
...         return self[key]

>>> dict_with_never_missing_keys = my_dict(existing_key=42)
>>> dict_with_never_missing_keys['existing_key']
42
>>> dict_with_never_missing_keys['missing_key'] # doctest: +ELLIPSIS
<Mock id='...'>


>>> class StrDictKey0(dict):
...     def __missing__(self, key):
...         if isinstance(key, str):
...             raise KeyError(key)
...         return self[str(key)]

...     def get(self, key, default = None):
...         try:
...             return self[key]
...         except KeyError:
...             return default

...     def __contains__(self, key):
...         return str(key) in self.keys() or key in self.keys()

>>> d = StrDictKey0([('2', 'two'), ('4', 'four')])
>>> d
{'2': 'two', '4': 'four'}

>>> d['2']
'two'
>>> d['4']
'four'
>>> d['3']
Traceback (most recent call last):
    ...
KeyError: '3'

>>> d.get('2')
'two'
>>> d.get('4')
'four'
>>> d.get('3', 'N/A')
'N/A'

>>> 2 in d
True
>>> 1 in d
False
"""