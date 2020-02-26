"""
Use a stack data structure to convert nteger values to binary.

Example: 242
             -->Remainder
242/2 = 121  -->0
121/2 = 60.5 -->1
60/2  = 30   -->0
30/2  = 15   -->0
15/2  = 7.5  -->1
7/2   = 3.5  -->1
3/2   = 1.5  -->1
1/2   = 0.5  -->1
Please Note: here we are considering 0.5 value as 1
Hence the binary representation would be --> 11110010 (bottom to top)
cmd-->python--> int('11110010', 2) ->##(here we have taken base 2 to convert to integer) --> 242
"""

from PythonCodingTraining.DataStructure.Stack.Stack import Stack


def div_by_2(dec_num):
    s = Stack()
    while dec_num>0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num//2
    print(s.get_stack())
    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


print(div_by_2(242))

