import pytest

from dataclasses import dataclass
@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'


def test_demo_data_class():
    assert DemoDataClass.__annotations__ == {'a': int, 'b': float}
    assert DemoDataClass.__doc__ == 'DemoDataClass(a: int, b: float = 1.1)'
    with pytest.raises(AttributeError) as exception_info:
        DemoDataClass.a
    assert str(exception_info.value) == \
        "type object 'DemoDataClass' has no attribute 'a'"
    assert DemoDataClass.b == 1.1
    assert DemoDataClass.c == "spam"

    dc = DemoDataClass(15)
    assert dc.a == 15
    assert dc.b == 1.1
    assert dc.c == "spam"

    dc.a = "Hello"
    assert dc.a == "Hello"
    assert type(dc.a) == str

    dc.b = 0
    assert dc.b == 0
    assert DemoDataClass.b == 1.1

    dc.z = "some value"
    assert dc.z == "some value"
