"""
if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3,
she will be able to blow out 2 candles successfully,
since the tallest candles are of height 4 and there are 2 such candles.

Input:
4
4 4 1 3

Output:
2
"""


def candle():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    sort_list = sorted(arr, reverse=True)
    first_ele = sort_list[0]
    dict1 = {}
    for i in range(n):
        if sort_list[i] in dict1.keys():
            dict1[sort_list[i]] += 1
        else:
            dict1[sort_list[i]] = 1
    candles = dict1[first_ele]
    print(candles)


candle()
