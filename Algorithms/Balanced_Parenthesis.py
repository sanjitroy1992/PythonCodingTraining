"""
Balanced: ({[]})
Not Balanced: ({[}})
"""
        
def balanced_parenthesis():
    expr = "({[]})"
    s = []
    for i in range(len(expr)):
        if expr[i] in "({[":
            s.append(expr[i])
        elif len(s) == 0:
            return False
        elif expr[i] == ')':
            top = s.pop()
            if (top == '{' or top=='['):
                return False
        elif expr[i] == '}':
            top = s.pop()
            if (top == '(' or top=='['):
                return False
        elif expr[i] == ']':
            top = s.pop()
            if (top == '(' or top=='{'):
                return False
    if len(s) == 0:
        return True
    else:
        return False

print(balanced_parenthesis())