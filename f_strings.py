# src: https://realpython.com/python-format-mini-language/
from math import pi
from datetime import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

jane = Person(name="Jane 😀", age=25)

# !s = str
assert "Hi! {!s}".format(jane) == "Hi! I'm Jane 😀, and I'm 25 years old."
assert f"Hi! {jane!s}" == "Hi! I'm Jane 😀, and I'm 25 years old."

# !r = repr
assert "An instance: {!r}".format(jane) == "An instance: Person(name='Jane 😀', age=25)"
assert f"An instance: {jane!r}" == "An instance: Person(name='Jane 😀', age=25)"

# !a = ascii
assert "ASCII: {!a}".format(jane) == "ASCII: Person(name='Jane \\U0001f600', age=25)"
assert f"ASCII: {jane!a}" == "ASCII: Person(name='Jane \\U0001f600', age=25)"

text = "Hello"
assert f"{text:30}"   == "Hello                         "
assert f"{text:<30}"  == "Hello                         "
assert f"{text:>30}"  == "                         Hello"
assert f"{text:^30}"  == "            Hello             "
assert f"{text:=^30}" == "============Hello============="

try:
    f"{42:s}"
except Exception as ex:
    assert type(ex) is ValueError
    assert str(ex) == "Unknown format code 's' for object of type 'int'"

number = 42
assert f"{number:d}" == "42"
assert f"{number:b}" == "101010"
assert f"{number:o}" == "52"
assert f"{number:x}" == "2a"

billion = 1_000_000_000
assert f"{billion:e}" == "1.000000e+09" # scientific notation
assert f"{billion:f}" == "1000000000.000000" # fixed point notation
assert f"{billion:g}" == "1e+09" # fixed point notation
assert f"{billion:n}" == "1000000000" # fixed point notation

assert f"{pi}"      == "3.141592653589793"
assert f"{pi:.4f}"  == "3.1416"
assert f"{pi:.8f}"  == "3.14159265"

assert f"{billion:,}" == "1,000,000,000"
assert f"{billion:_}" == "1_000_000_000"
assert f"{billion:,.2f}" == "1,000,000,000.00"

positive, negative = 42, -42
assert f"{positive:+}" == "+42"
assert f"{negative:+}" == "-42"
assert f"{positive:-}" == "42"
assert f"{negative:-}" == "-42"
assert f"{positive: }" == " 42"
assert f"{negative: }" == "-42"

total = 123456.99
width = 30
align = ">"
fill = "."
precision = 2
sep = ","
assert f"Total{total:{fill}{align}{width}{sep}.{precision}f}" \
    == "Total....................123,456.99"

inventory = [
    ("Apple", 5.70),
    ("Orange", 4.50),
    ("Banana", 6.00),
    ("Mango", 8.60),
    ("Pepper", 4.20),
    ("Carrot", 3.57),
]
pricelist = ""
for item in inventory:
    product,price = item
    pricelist += f"{product:.<30}${price:.2f}\n"
assert pricelist == \
"""Apple.........................$5.70
Orange........................$4.50
Banana........................$6.00
Mango.........................$8.60
Pepper........................$4.20
Carrot........................$3.57
"""

date = datetime(2024, 2, 17, 20, 35, 53, 251170)
assert f"Today is {date:%a %b %d, %Y} and it's {date:%H:%M} hours" == \
        "Today is Sat Feb 17, 2024 and it's 20:35 hours"

number = 0.25
assert f"{number:.2%}" == "25.00%" # percentage

