a=[1,3,2,1,3,0,5,1]
b=[0]*len(a)
result=[0]*len(a)
for i in a:
    b[i] += 1
for i in range(1,len(b)):
    b[i]=b[i]+b[i-1]
for i in a:
    b[i]=b[i]-1
    result[b[i]]=i
print(result)