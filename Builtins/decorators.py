"""
Decorators in Python are essentially functions that add functionality to an existing function in Python without
changing the structure of the function itself. They are represented by the @decorator_name in Python and are called
in bottom-up fashion.
"""
# decorator function to check if b == 0
def check(func):
    def wrapper(a, b):
        if b == 0:
            print("Can't divide by 0")
            return
        return func(a, b)
    return wrapper


@check
def divide(a, b):
    return a/b

print(divide(3,4))