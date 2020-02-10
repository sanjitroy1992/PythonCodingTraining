x=[10,19,18]
y=[11,15,9]

count=0
for i in range(len(x)):
    for j in range(len(y)):
        if (pow(x[i],y[j])>pow(y[j],x[i])):
            print("{} {}".format(x[i],y[j]))
            count+=1

print(count)
