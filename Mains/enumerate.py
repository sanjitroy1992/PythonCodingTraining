#The enumerate() method adds counter to an iterable and returns it (the enumerate object).

names = ['sanjit','anmon','kartik']
## printing itrator with names using enumerate
print(list(enumerate(names)))

# using the help of itrator we are assigning the row no.
for count, name in enumerate(names, start=1):
    print("row no: {} and name : {}".format(count, name.upper()))