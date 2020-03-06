"""
Given a list of numbers, find all numbers divisible by 13.

Input : my_list = [12, 65, 54, 39, 102,
                     339, 221, 50, 70]
Output : [65, 39, 221]
Solution:
We could create a lambda function which will test the divisible of 13
and then in the filter we could pass the function and input sequence.
"""
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]
# use anonymous function to filter and comparing
# if divisible or not
function = lambda x: x % 13 ==0
numbers = list(filter(function, my_list))
# printing the result
for i in numbers:
    print(i)


"""
Given a list of strings, find all palindromes.
"""
# Python Program to find palindromes in
# a list of strings.
my_list = ["geeks", "geeg", "keek", "practice", "aa"]
# use anonymous function to filter palindromes.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
function = lambda x: (x == "".join(reversed(x)))

print(list(filter(function, my_list)))




