"""Write a program that prints the numbers from 1 to 100. But for multiples of
three print “Lorem” instead of the number and for the multiples of five print “Ipsum”.
For numbers which are multiples of both three and five print “LoremIpsum”."""


for i in range(1, 101):
  if (i%3 == 0 and i%5 == 0):
    print("LoremIpsum")
  elif i%3 == 0:
    print("Lorem")
  elif i%5 == 0:
    print("Ipsum")
  else:
    print(i)