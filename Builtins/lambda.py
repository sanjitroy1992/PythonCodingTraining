"""
Sort the animals in the below example using lambda
"""
animals = [{'type': 'penguin', 'name': 'Stephanie', 'age': 8},
           {'type': 'elephant', 'name': 'Devon', 'age': 3},
           {'type': 'puma', 'name': 'Tommy', 'age': 5},]

s = sorted(animals, key=lambda animal: animal['age'])
print(s)
s1 = sorted(animals, key=lambda hello: hello['name'])
print(s1)

# sort names with second value in a nested list
names = [["Harry Potter",1], ["Sanjit Roy",0], ["Anmol Ratan",2], ["Karthik S",3], ["Sounak Saha",4]]
print(sorted(names, key=lambda name:name[1]))

# List of Odd numbers using filter and lambda
num = [1,2,3,4,5,6,7,8,9]
even_num = list(filter(lambda x:x%2!=0, num))
print(even_num)
