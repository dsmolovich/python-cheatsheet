registry = []

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func

@register
def f1():
   print('funning f1()')

@register
def f2():
   print('funning f2()')

def f3():
   print('funning f3()')
   
def main():
   print('running main()')
   print('registry ->', registry)
   f1()
   f2()
   f3()

if __name__ == '__main__':
   main()

"""
Expected output:

running register(<function f1 at 0x106f2ef80>)
running register(<function f2 at 0x106fdea70>)
running main()
registry -> [<function f1 at 0x106f2ef80>, <function f2 at 0x106fdea70>]
funning f1()
funning f2()
funning f3()

And when importing:
>>> from src.fluent_python.chapter_9_decorators_n_closures import when_python_executes_decorators
running register(<function f1 at 0x109582290>)
running register(<function f2 at 0x109582200>)
"""