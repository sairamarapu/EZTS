'''a=[[1,2,13],
   [4,15,60],
   [70,8,9]]'''
a=[[1,2],[3,4]]
print
b=[]
for i in range(0,len(a),1):
    for j in range(i,len(a)):
        temp=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=temp
for i in a:
    i.reverse()
print(a)