#1. How about you create a function using which you could call another function.

def f1(func):
    def wrapper():
        print("Before")
        func()
        print("ended")
    return wrapper
#let's write a small function to print a value
@f1
def f():
    print("Hi")
# f()

#2. let's write a function to add two numbers

def f2(func):
    def wrapper(*args, **kwargs):
        print("Before")
        val = func(*args, **kwargs)
        print("after")
        return val
    return wrapper
@f2
def add(x,y):
    return x+y

print(add(2,3))
