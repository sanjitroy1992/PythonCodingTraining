"""Recursion of Two Numbers
Youtube:https://youtu.be/VapDVrsERsA?list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm"""
def recursive_multiply(x, y):
    ## In order to maximum recursion depth exceeded in comparison
    if y > x:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)
print(recursive_multiply(500, 2000))