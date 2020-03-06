A = [2,3,3,4,5,6]
B = [2,3,3,5,9]

# print(set(A).intersection(set(B)))
def intersection():
    i = 0
    j = 0
    intersectionlist = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
                if A[i] != A[i-1]:
                    intersectionlist.append(A[i])
                    i += 1
                    j += 1
                elif A[i]<B[j]:
                    i += 1
                else: ## A[i]>B[j]
                    j += 1
    print(intersectionlist)
# print(intersection())


# import requests
# import pprint
# url = 'http://maps.googleapis.com/maps/api/geocode/json'
# location = "delhi technological university"
# PARAMS = {'address':location}
# response = requests.get(url=url, params=PARAMS)
# json = response.json()
# print(json)

# import diff_pdf_visually as pd
# diff = pd.pdfdiff('D:\\TACOE_All_Projects\\PDFDiff\\Baseline.pdf', 'D:\\TACOE_All_Projects\\PDFDiff\\App.pdf')
# print(dict)

def returnvalue():
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    maxv = max(arr)
    l = list(filter(lambda x: x != maxv, arr))
    print(l)
    return (max(l))
print(returnvalue())