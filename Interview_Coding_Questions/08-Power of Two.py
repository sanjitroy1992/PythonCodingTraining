"""
WAP to check if a number is a power of 2 or not
 
Example:
    input = 1
    output= True (2 power 0 is 1)
    
    input = 33
    output= False
"""
import sys
def power_of_two():
    number = int(input("Enter the number to check if it's power of two: "))
    max_num = sys.maxsize
    for i in range(max_num):
        power = 2**i
        if number == power:
            return True
        elif (number< power):
            return False

print(power_of_two())


