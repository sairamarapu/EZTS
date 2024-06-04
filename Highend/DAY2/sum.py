def sum(li):
    sum=0
    for i in li:
        sum=sum+i
    return sum
n=int(input())
li=list(map(int,input().strip().split()))[:n]
a=sum(li)
print(a)