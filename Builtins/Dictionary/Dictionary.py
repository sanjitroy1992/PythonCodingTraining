"""
In this program we'll learn the performance of a list and a dictionary.
In the below example:
1. we have taken a list as class_names of first 10 alphabet's
2. created a def to generate 500000 random character from class_names list and writing it in data.txt file line by line.
3. in read dataset list and dict function for every line in data.txt file we are counting the ch present in the file.
4. At the end printing the performance of the code using time built in module
"""

class_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def create_dataset():
    import random
    number_entries = 500000
    f = open("data.txt", "w")
    for i in range(number_entries):
        current = random.choice(class_names)
        f.write(current + '\n')
    f.close()

def read_dataset_list():
    class_counts = []
    for _ in class_names:
        class_counts.append(0)
    print(class_names)
    print(class_counts)
    with open("data.txt", 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                class_counts[class_names.index(line)] += 1  # with the reference of class_names index position
                                                            # incrementing the value of class counts
    print(class_counts)

def read_dataset_dict():
    class_counts = {}
    for i in class_names:
        class_counts[i] = 0
    print(class_counts)
    with open("data.txt", 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                class_counts[line] += 1
    print(class_counts)


import time
#create_dataset()
t0 = time.time()
read_dataset_list()
t1 = time.time()
print("list took {} seconds to execute!".format(t1-t0))

t2 = time.time()
read_dataset_dict()
t3 = time.time()
print("Dict took {} seconds to execute!".format(t3-t2))
