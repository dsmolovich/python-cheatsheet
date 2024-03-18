# SRC: https://www.educative.io/answers/what-is-monkey-patching-in-python
class Power:
    def square(self, num):
        return f"Square of {num} is {num**2}"

if __name__ == '__main__':
    obj = Power()
    result = obj.square(3)
    print(result)
    assert result == "Square of 3 is 9"
