row=int(input())
col=(2*row)-1
start,end=row-1,row-1
for i in range(row):
    count=1
    for j in range(col):
        if i==row-1 and j%2==0:
            print(count,end=' ')
            count=count+1
        elif j==start or j==end:
            print(count,end=' ')
            count=count+i
        else:
            print(' ',end=' ')
    print()
    start=start-1
    end=end+1