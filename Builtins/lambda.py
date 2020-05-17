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