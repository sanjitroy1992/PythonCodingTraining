"""
Count Inversions in an array | Set 1 (Using Merge Sort)
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

METHOD 1 (Simple)
For each element, count number of elements which are on right side of it and are smaller than it.


"""

l1=[2,4,1,3,5]
count=0
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            count+=1
            print("{} {}".format(l1[i],l1[j]))

print(count)

