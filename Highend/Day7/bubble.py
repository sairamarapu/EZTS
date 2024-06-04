a=[6,8,9,5,4,3,26,2]
counter=0
flag=0
while(len(a)>counter):
    j=0
    for i in range(1,len(a)-counter):
        if a[j]>a[i]:
            a[j],a[i]=a[i],a[j]
            flag=1
        j=j+1
    print(a[i],end=" ") 
    if(flag==0):
        break    
    counter=counter+1
print(a)