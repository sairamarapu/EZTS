def mergesort(a):
    global c
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i += 1
                k += 1
            else:
                a[k]=right[j]
                c+=len(left)-i
                j += 1
                k += 1
        while(i<len(left)):
            a[k]=left[i]
            i=i+1
            k=k+1
        while(j<len(right)):
            a[k]=right[j]
            c+=len(left)-i
            j=j+1
            k=k+1
    return c
a=[12,45,6,89,2,32,21]
c=0
print(mergesort(a))
