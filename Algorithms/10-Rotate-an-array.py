"""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotate from right to left by 2 positions
Setps:
1. temp = A[len(A)-1] = [10]
2. [1, 1, 2, 3, 4, 5, 6, 7, 8, 9] --> Shift items by one to the right
3. A[len(A)-1] = temp --> [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
4. temp = A[len(A)-1] = [10]
5. [10, 10, 1, 2, 3, 4, 5, 6, 7, 8] --> Shift items by one to the right
6. A[len(A)-1] = temp --> [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
Output = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
"""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rotate_array_right_to_left():
    n = int(input("Enter the number of rotation: "))
    for i in range(n):
        temp = A[len(A)-1]      #save the last item in temp variable
        for j in range(len(A)-1, 0, -1):    #run this for loop backward from last element to first
            A[j] = A[j-1]       #Shift last value with it's prev value until it reaches to the first item.
        A[0] = temp     #get the temp value and replace it with the first item
    print(A)


"""
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotate from left to right by 2 positions
Setps:
1. temp = A[0] = [1]
2. [2, 3, 4, 5, 6, 7, 8, 9, 10, 10] --> Shift items by one to the left
3. A[len(A)-1] = temp --> [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
4. temp = A[0] = [2]
5. [3, 4, 5, 6, 7, 8, 9, 10, 1, 1] --> Shift items by one to the left
6. A[len(A)-1] = temp --> [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Output = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2] 
"""
def rotate_array_left_to_right():
    n = int(input("Enter the number of rotation: "))
    for i in range(n):
        temp = A[0]      #save the first item in temp variable
        for j in range(0, len(A)-1):    #run this for loop backward from last element to first
            A[j] = A[j+1]       #Shift last value with it's prev value until it reaches to the first item.
        A[len(A)-1] = temp     #get the temp value and replace it with the first item
    print(A)


# rotate_array_left_to_right()
rotate_array_right_to_left()