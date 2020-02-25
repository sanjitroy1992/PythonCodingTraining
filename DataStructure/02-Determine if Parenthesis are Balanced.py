"""
Use a stack to check whether or not a string has balanced usage of parenthesis.
Example:
    (), ()(), (({[]})) --> Balanced.
    ((), {{{)}], [][]] --> Not Balanced.

Balanced Example: {[]}

Non-Balanced Example: (()

Non-Balanced Example: ))

Youtube: https://youtu.be/TC7apM-xGaU?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV

"""
from PythonCodingTraining.DataStructure.Stack import Stack

def if_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        ## if paren string is "({[" then push it into the stack and keep continue for all the opening parenthesis.
        if paren in "({[":
            s.push(paren)
        else:
            ### This means the first parenthesis starts with a closing parenthesis. Hence, the parenthesis are not balanced
            if s.is_empty():
                is_balanced = False
            else:
                ### retrieve the top element from the stack and check if it matches with the current parenthesis using a function called is_matche.
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        ### keep continue the while loop by incrementing index
        index += 1
    ### At the end if the stack parenthesis are empty and is_balanced paramenter is still True then it's a valid case.
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def is_match(p1, p2):
    return True if (p1 + p2) in ['()', '{}', '[]'] else False

### Positive scenario
print(if_paren_balanced('(())'))

## Negative Scenario
print(if_paren_balanced('(()'))