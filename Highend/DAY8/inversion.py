a=[12,45,6,89,2,32,21]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            count=count+1
print(count)