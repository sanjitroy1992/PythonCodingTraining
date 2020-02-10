"""
check-string-substring-another


"""
def search(txt,pat):
    n=len(txt)
    m=len(pat)
    for i in range(n-m+1):
        flag = 0
        for j in range(m):
            if(txt[i+j]!=pat[j]):
                flag=1
                break
        if(flag==0):
            print("patter {} found at {}".format(pat,i))

txt = "BlUeBe1Bl*fjal9jkl"
pat = "Bl"
search(txt,pat)