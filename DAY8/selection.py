a=list(map(int,input().split()))
for i in range(len(a)):
    min=i
    for j in range(i,len(a)):
        if(a[min]>a[j]):
            min=j
    a[min],a[i]=a[i],a[min]
print(a)