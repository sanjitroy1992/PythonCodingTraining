#The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print("arr : {}".format(arr))
    count = n-1
    for i in range(n):
        # print("i : {}".format(i))
        print(arr[count], end=" ")
        count -= 1
