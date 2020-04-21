"""
Input: Python3.com
Output: pYTHON3.COM
"""

def swap_case(s):
    list1 = []
    for ch in s:
        print(ch)
        if ch.isalpha():
            if ch == str(ch).lower():
                list1.append(str(ch).upper())
            elif ch == str(ch).upper():
                list1.append(str(ch).lower())
        else:
            list1.append(ch)
    return ''.join(list1)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)