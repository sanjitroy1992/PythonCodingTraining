def FirstFactorial(num):
    if num > 1:
        num = num*FirstFactorial(num-1)
    return num

print(FirstFactorial(int(input())))
