"""
Available sizes and colors:
to test it use the next command:
```
python -mdoctest src/listcomp_cartesian_product.py -v
```

>>> sizes = ['S', 'M', 'L']
>>> colors = ['black', 'white']

Cartesian product
Arranged by color then size

>>> tshirts = [(color, size) for color in colors \
                             for size in sizes]
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), \
('white', 'S'), ('white', 'M'), ('white', 'L')]

Arranged by size then color

>>> tshirts = [(color, size) for size in sizes \
                             for color in colors]
>>> tshirts
[('black', 'S'), ('white', 'S'), ('black', 'M'), \
('white', 'M'), ('black', 'L'), ('white', 'L')]
"""