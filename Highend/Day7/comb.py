a=[6,8,9,5,4,3,26,2]
target=13
sum=0
li=[]
for i in range(0,len(a)):
    if sum==target:
        print(li)
    sum=a[i]
    li.clear()
    li.append(a[i])
    for j in range(i+1,len(a)):
        if sum==target:
            print(li)
            li.clear()
            li.append(a[i])
            sum=a[i]
        elif sum+a[j]>target:
            continue
        elif sum+a[j]<=target:
            li.append(a[j])
            sum=sum+a[j]