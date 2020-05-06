"""
Have the function ArrayAddition(arr) take the array of numbers sorted in arr and return string true if any combination
of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array,
otherwise return the srting false.
For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4+6+10+3 = 23.
The array will not be empty, will not contain all the same elements, and may contain negative numbers.

Examples:
    Input: [5, 7, 16, 1, 2]
    Output: false

    Input: [3, 5, -1, 8, 12]
    Output: true

"""


def ArrayAdditionI(arr):
    arr.sort()
    print("sorted array: {}".format(arr))
    print("n: {}, sum: {}".format(len(arr)-1, arr[-1]))
    mem = dict()
    def check_sum(n, sum):
        if n == 0:
            return 'false'
        if n == 1:
            return arr[0] == sum
        print(mem.keys())
        if (n, sum) in mem.keys():
            return mem[(n, sum)]
        else:
            print(n)
            f = check_sum(n - 1, sum) or check_sum(n - 1, sum - arr[n - 1])

            mem[(n, sum)] = f
            print("mem: {}".format(mem))
            return f
    return check_sum(len(arr) - 1, arr[-1])

# arr = [3,5,-1,8,12]
# arr = [5,7,16,1,2]
# arr = [16, 16]
# arr = [1, 2, 6, 5]
# arr = [3, 5, -1, 8, 12]
# print(ArrayAdditionI(arr))


def array_addition(arr):
    arr.sort()
    max = arr[-1]
    isCombination = False
    print("\narr = " + str(arr))
    print("max = " + str(max))
    checkArr = arr[:len(arr)-1]
    print("checkarr: {}".format(checkArr))

    for i, a in enumerate(checkArr):
        sum = a
        for j, b in enumerate(checkArr[i + 1::]):
            sum += b
            if (sum == max):
                isCombination = True
                break
            if (sum > max):
                isCombination = False
                break
        if(isCombination): break
    return isCombination


arr1 = [4, 6, 23, 10, 1, 3]
arr2 = [5, 7, 16, 1, 2]
arr3 = [-1, 3, 5, 8, 12]
print(array_addition(arr1))
print(array_addition(arr2))
print(array_addition(arr3))