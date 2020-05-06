s = "Was it a cat i saw?"
s = s.replace(" ","").lower()
s1 = ''
for i in range(len(s)):
    if s[i].isalpha():
        s1 += s[i]

if s1[:] == s1[::-1]:
    print(True)