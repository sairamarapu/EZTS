a=[6,8,9,5,4,3,26,2]
for i in range(len(a)):
    j=i-1
    temp=a[i]
    while(j>=0 and temp<a[j]):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
print(a)