"""
>>> with open('/etc/hosts', 'r') as fp:
...     src = fp.read(60)
...

>>> len(src)
60

>>> fp
<_io.TextIOWrapper name='/etc/hosts' mode='r' encoding='UTF-8'>

>>> fp.closed, fp.encoding
(True, 'UTF-8')

>>> fp.read(60)
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.

>>> fp = open('/etc/hosts', 'r')
>>> fp
<_io.TextIOWrapper name='/etc/hosts' mode='r' encoding='UTF-8'>
"""