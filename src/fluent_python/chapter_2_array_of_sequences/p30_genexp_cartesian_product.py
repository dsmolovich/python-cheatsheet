"""
Available sizes and colors:
to test it use the next command:
```
python -mdoctest src/genexp_cartesian_product.py -v
```

>>> sizes = ['S', 'M', 'L']
>>> colors = ['black', 'white']
>>> for tshirt in (f"{color}, {size}" for color in colors for size in sizes):
...     print(tshirt)
...
black, S
black, M
black, L
white, S
white, M
white, L
"""