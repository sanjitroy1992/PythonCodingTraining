"""
Video: https://youtu.be/mGaamvgPqpw
For example, for the array:
[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

with target = 108, the algorithm would return 3, as the first occurrence of 108 in the above array is located at index 3.

Complexity:
Time: O(logn)
"""

def find():
    list1 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    low = 0
    high = len(list1)
    while(low<=high):
        mid = (low+high)//2
        if(target>list1[mid]):
            low = mid+1
        elif(target<list1[mid]):
            high = mid-1
        else:
            if (mid-1<0):
                return mid
            elif(list1[mid-1]!=target):
                return mid
            else:
                high = mid - 1

print(find())
