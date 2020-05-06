def squar_number(nums):
    for i in nums:
        yield (i*i)

squar = squar_number([1,2,3,4,5])
print(squar.__next__())
print(squar.__next__())
print(squar.__next__())
print(squar.__next__())
print(squar.__next__())

for value in squar_number([1,2,3,4,5]):
    print(value)