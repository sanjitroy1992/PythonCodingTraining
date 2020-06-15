# -*- coding: utf-8 -*-
"""
find duplicates in an array with values from 0 to len(array)-1

Input: [1,2,2,2,3,4,5,5,5,6,6,7,7,7,8]
Output: [2, 5, 6, 7]
"""

def get_dups(array):
    ht = {}
    dups = []
    for x in array:
        if x in ht:
            dups.append(x)
        else:
            ht[x] = x
    return list(set(dups))

print(get_dups([1,2,2,2,3,4,5,5,5,6,6,7,7,7,8]))