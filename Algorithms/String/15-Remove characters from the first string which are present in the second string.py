s1 = "geeksforgeek"
s2 = "geek"
empty = ''
for i in range(len(s2)):
    if s2[i] in s1:
        s1 = s1.replace(str(s2[i]),'')
print(s1)