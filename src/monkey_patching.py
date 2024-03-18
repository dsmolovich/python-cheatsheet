# SRC: https://www.educative.io/answers/what-is-monkey-patching-in-python
from original_package.monkey_patch_me import Power

def cube(self, num):
    return f"Cube of {num} is {num **3}"

# monkey patch original Power.square() with cube()
Power.square = cube

if __name__ == '__main__':
    obj = Power()
    result = obj.square(3)
    print(result)
    assert result == "Cube of 3 is 27"
