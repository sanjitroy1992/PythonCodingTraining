"""
Have the function PlusMinus(num) read the num
parameter being passed which will be a combination of 1 or more single digits, and determine if it's possible to
separate the digits with either a plus or minus sign to get the final expression to equal zero.
For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and
this expression equals zero. Your program should return a string of the signs you used, so for this example
your program should return -++-. If it's not possible to get the digit expression to equal zero,
return the string not possible. If there are multiple ways to get the final expression to equal zero,
choose the one that contains more minus characters. For example: if num is 26712
your program should return -+-- and not +-+-.

"""


def PlusMinus(num):
    arr = list(map(str, str(num)))
    signs = ""
    prev = int(arr[0])

    for a in arr[1:]:
        cur = int(a)

        if prev > 0:
            prev = prev - cur
            signs += "-"
        else:
            prev = prev + cur
            signs += "+"

    if prev == 0:
        return signs
    else:
        return "not possible"


print(PlusMinus(35132))  # -++-
print(PlusMinus(26712))  # -+--
print(PlusMinus(2671))  # not possible
print(PlusMinus(1212))